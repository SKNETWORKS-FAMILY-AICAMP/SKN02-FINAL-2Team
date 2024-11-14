# SKN02-FINAL-2Team
SKN2기 최종 단위프로젝트



#  팀 소개
👩‍🏫 <strong>팀 구성</strong> </br></br>
**[팀장]** 송문영 <br/>
**[팀원]** 김서연, 전유빈, 정영재, 정인교
<br/><br/>


#  프로젝트


👨‍🏫 <strong>프로젝트 개요</strong></br></br>
우리 사회를 살아가는데 있어서 경제는 밀접하게 연관되어 있는 중요한 요소 중 하나입니다. 모든 사회 구조와 비즈니스 모델은 경제 지식을 베이스로 설계됩니다. 따라서, 서비스를 공급하는 사람과 이용하는 사람 모두 경제 지식을 갖추고 있어야 합니다. </br></br>
특히나 몇 년 전부터 실물 자산 없이 거래할 수 있는 핀테크 환경이 구축되기 시작하면서 추상성이 강화된 경제구조로 바뀌고 있습니다. 해당 프로젝트는 변화하는 경제 구조에 사람들이 적응할 수 있도록, 경제 지식을 쉽게 설명하는 AI 인플루언서를 매개로 한 웹 페이지 구현을 목표로 합니다.</br></br>
저희 프로젝트 팀은 기업에서 원하는 방향으로 경제 지식을 제공할 수 있도록 AI 인플루언서를 앞세운 웹 페이지 솔루션 형태로 제작했습니다. 이러한 솔루션을 통해 이용자들의 경제 이해도를 높임으로써 간접 이익을 챙길 수 있을 뿐 아니라, 출판/광고 게시로 연계하며 직접 이익 또한 획득할 수 있을 것으로 기대합니다.</br></br>

👩‍🏫 <strong>서비스 목표</strong></br></br>
현 경제 상황에서는 예/적금만으로 기업과 소비자 모두 수익을 내기 어렵습니다. 소비자에게 난해한 경제 지식을 쉽게 설명함으로써 미래 고객에게 경제 구조를 납득시킬 수 있어야, 장기적인 관점에서 기업이 수익을 낼 수 있습니다. 이는 간접 이익 효과에 해당합니다.</br></br> 
또한 게시글을 편집하여 도서 형태로 출판하거나 게시글에 광고를 부착함으로써 직접적인 수익 창출 또한 가능할 것으로 전망하고 있습니다.</br></br>


🔨 <strong>기술 스택</strong>
<div align=left><h3>🕹️ Frontend</div>
<div align=left>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">
  <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=Bootstrap&logoColor=white">
</div>

<div align=left><h3>🕹️ Backend</div>
<div aling=left>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
  <img src="https://img.shields.io/badge/postgresql-4169E1?style=for-the-badge&logo=Postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/gunicorn-499848?style=for-the-badge&logo=Gunicorn&logoColor=white">
  <img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=Nginx&logoColor=white">
  
  <img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=Linux&logoColor=white">
</div>
  
<div align=left><h3>🕹️ AI</div>
<div align=left>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=OpenAI&logoColor=white">
  <img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=LangChain&logoColor=white">
  <img src="https://img.shields.io/badge/Faiss-0467DF?style=for-the-badge&logo=Meta&logoColor=white">
  <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=Pytorch&logoColor=white">
  
</div>

<div align=left><h3>🕹️ Infra </div>
<div align="left">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white"><br/><br/>

<br/>
📝 <strong>WBS</strong> (https://docs.google.com/spreadsheets/d/1jcKlFxyC9QGutLGy6v7sRdCaukjxnwxW-72Tx2Wmcz8/edit?usp=sharing)

<br/><br/>
💻 <strong>DB 테이블 - ERD 및 DDL</strong>
![my_project_visualized](https://github.com/user-attachments/assets/163b9587-b109-4c53-a257-7014fa0213a1)


📚 <strong>주요 프로시저</strong><br/><br/>
**[ Post 작성 ]**
1. 전처리 파일 불러오기
2. Title로 사용할 글 소재 불러오기
3. Search 버튼 클릭해서 RAG 기반으로 Content 내용 생성하기
4. Content에서 AI 인플루언서가 작성한 내용 확인하기
5. Debug Output에서 Retrieved 문서 확인하기
6. Generate Image 버튼 클릭해서 Content 내용 기반으로 이미지 예시 생성하기
7. Submit 버튼 클릭하기

<br/>

**[ 오늘의 단어 ]**
1. 전처리 파일 불러오기
2. Title로 사용할 단어 소재 불러오기
3. Search 버튼 클릭해서 RAG 기반으로 Content 내용 생성하기
4. Content에서 AI 인플루언서가 작성한 내용 확인하기
5. Debug Output에서 Retrieved 문서 확인하기
6. Submit 버튼 클릭하기
* 상기의 과정은 정해진 시간에 AI Agent가 자동으로 수행

<br/>

**[ 최신 News로 보는 경제 트렌드 ]**
1. 크롤링한 최신 뉴스 데이터 불러오기
2. LangChain으로 엮은 LLM 기반으로 최신 뉴스 데이터 요약하기
* 상기의 과정은 정해진 시간에 AI Agent가 자동으로 수행

<br/>

📚 <strong>수행결과</strong>


📚 <strong>한줄 회고</strong>
- 송문영 : 
- 김서연 : 경제 전문가로 거듭나 안락함을 누린다!
- 전유빈 : 
- 정영재 : 
- 정인교 :
