from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from articles.models import Article, Category



class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'
    ordering = '-date_created'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView,
                        self).get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView,
                        self).get_context_data(*args, **kwargs)

        context['categories'] = Category.objects.all()
        return context

class ArticleCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Article
    fields = ['title','category','body','featured','thumbnail']
    success_message = 'An article has been created!'
    redirect_field_name = 'redirect_to'
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        context = super(ArticleCreateView,
                        self).get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context
    

    
class ArticleUpdateView(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    fields = ['title','category','body','featured','thumbnail']
    success_message = 'An article has been updated!'
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
  
    def test_func(self):
        article = self.get_object()
        if article.author == self.request.user:
            return True
        return False
    
    def get_context_data(self,*args,**kwargs):
        context = super(ArticleUpdateView,self).get_context_data(*args,**kwargs)
        context['article'] = self.get_object()
        context['categories'] = Category.objects.all()
        return context
    
class ArticleDeleteView(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    success_message = 'An article has been deleted!'
    success_url = '/'
    
    def delete(self,request,*args,**kwargs):
        messages.success(self.request,self.success_message)
        return super(ArticleDeleteView,self).delete(request,*args,**kwargs)
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        article = self.get_object()
        if article.author == self.request.user:
            return True
        return False
    
    def get_context_data(self,*args,**kwargs):
        context = super(ArticleDeleteView,self).get_context_data(*args,**kwargs)
        context['article'] = self.get_object()
        context['categories'] = Category.objects.all()
        return context
    
#Category
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/category_detail.html'
  
    def get_context_data(self,*args,**kwargs):
        context = super(CategoryDetailView,self).get_context_data(*args,**kwargs)
        category = self.get_object()
        context['articles'] = Article.objects.filter(category=category)
        context['categories'] = Category.objects.all()
        return context
