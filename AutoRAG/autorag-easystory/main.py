import os
import click
import asyncio
import time
import logging
import nest_asyncio
from autorag.evaluator import Evaluator
from dotenv import load_dotenv
import backoff
from openai import RateLimitError
import torch  # MPS 확인을 위해 필요

# nest_asyncio 적용
nest_asyncio.apply()

# MPS 장치가 사용 가능한지 확인
use_mps = torch.backends.mps.is_available()
if use_mps:
    logging.info("MPS 장치가 사용 가능합니다. PyTorch에서 MPS 가속을 사용합니다.")
else:
    logging.warning("MPS 장치를 사용할 수 없습니다. CPU를 사용합니다.")

root_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(root_path, 'data')

# 로깅 설정
logging.basicConfig(level=logging.INFO)

# .env 파일 로드
load_dotenv()

# OpenAI API 키 리스트 초기화
api_keys = [os.getenv("OPENAI_API_KEY_1"), os.getenv("OPENAI_API_KEY_2")]
api_key_index = 0  # 현재 사용 중인 API 키 인덱스

def get_next_api_key():
    """다음 API 키를 가져오는 함수"""
    global api_key_index
    api_key_index = (api_key_index + 1) % len(api_keys)
    return api_keys[api_key_index]

@backoff.on_exception(backoff.expo, RateLimitError, max_tries=6)
def rate_limited_request(evaluator, config):
    """동기 함수로 API 요청, RateLimitError 발생 시 다른 키로 전환"""
    global api_key_index
    while True:
        try:
            # 현재 API 키 설정
            os.environ["OPENAI_API_KEY"] = api_keys[api_key_index]
            
            # 평가 실행 (MPS가 활성화되었는지 확인)
            if use_mps:
                with torch.device("mps"):
                    evaluator.start_trial(config)
            else:
                evaluator.start_trial(config)
            break
        except RateLimitError:
            logging.warning("Rate limit 초과 발생. API 키를 전환하여 재시도합니다.")
            
            # 다른 API 키로 전환
            os.environ["OPENAI_API_KEY"] = get_next_api_key()
            
            # 지수 백오프에 따라 잠시 대기
            time.sleep(5)
            
        except Exception as e:
            logging.error(f"API 요청 중 오류 발생: {e}")
            break

@click.command()
@click.option('--config', type=click.Path(exists=True))
@click.option('--qa_data_path', type=click.Path(exists=True), default=os.path.join(data_path, 'generate_QA.parquet'))
@click.option('--corpus_data_path', type=click.Path(exists=True), default=os.path.join(data_path, 'generate_Corpus.parquet'))
@click.option('--project_dir', type=click.Path(exists=False), default=os.path.join(root_path, 'benchmark'))

def main(config, qa_data_path, corpus_data_path, project_dir):
    if api_keys[0] is None or api_keys[1] is None:
        raise ValueError("OPENAI_API_KEY가 .env 파일에 설정되지 않았습니다.")
    
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)

    evaluator = Evaluator(qa_data_path, corpus_data_path, project_dir=project_dir)

    # 비동기 호출 대신 동기 호출
    rate_limited_request(evaluator, config)

if __name__ == '__main__':
    main()