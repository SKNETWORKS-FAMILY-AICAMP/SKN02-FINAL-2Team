from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Tag, Comment, Word, Word_Tag, News

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Subject, RelatedWord

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Word, MarkdownxModelAdmin)
admin.site.register(News, MarkdownxModelAdmin)

admin.site.register(Comment)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

# admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
# admin.site.register(Word_Category, CategoryAdmin)
admin.site.register(Word_Tag, TagAdmin)

# Subject 모델 설정
class SubjectResource(resources.ModelResource):
	class Meta:
		model = Subject
   
@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
	resource_class = SubjectResource


# RelatedWord 모델 설정
class RelatedWordResource(resources.ModelResource):
	class Meta:
		model = RelatedWord

@admin.register(RelatedWord)   
class RelatedWordAdmin(ImportExportModelAdmin):
	resource_class = RelatedWordResource
 

# `is_active` 필터와 디스플레이 추가
class CustomUserAdmin(DefaultUserAdmin):
    list_filter = ('is_active', 'is_staff', 'is_superuser')  # 필터에 is_active 추가
    list_display = ('username', 'email', 'is_active', 'is_staff')  # 목록에 is_active 표시

# 기본 UserAdmin을 CustomUserAdmin으로 덮어쓰기
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)