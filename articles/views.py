from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
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

@login_required
def like(request):
    if request.method == 'POST':
        result = ''
        id = int(request.POST.get('article_id'))
        article = get_object_or_404(Article, id=id)
        if article.likes.filter(id = request.user.id).exists():
            article.likes.remove(request.user)
            article.like_count -=1
            result = article.like_count
            article.save()
        else:
            article.likes.add(request.user)
            article.like_count += 1
            result = article.like_count
            article.save()
        return JsonResponse({'result':result,})
    
def about(request):
    return render(request,'about.html',{'categories':Category.objects.all})