from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    CategoryDetailView,
)

urlpatterns = [
    path('',ArticleListView.as_view(), name='index'),
    path('article/detail/<slug:slug>/',ArticleDetailView.as_view(), name='article-detail'),
    path('article/create/',ArticleCreateView.as_view(), name='article-create'),
    path('article/update/<slug:slug>/',ArticleUpdateView.as_view(), name='article-update'),
    path('article/delete/<slug:slug>/',ArticleDeleteView.as_view(), name='article-delete'),
    path('category/detail/<slug:slug>/',CategoryDetailView.as_view(), name='category-detail'),
    
]