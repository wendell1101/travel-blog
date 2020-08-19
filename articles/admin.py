from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from articles.models import Article, Category
# Register your models here.

admin.site.register(Category)
admin.site.register(Article)

# class ArticleAdmin(SummernoteModelAdmin):
    
#     summernote_fields = ('body',)
# admin.site.register(Article,ArticleAdmin)