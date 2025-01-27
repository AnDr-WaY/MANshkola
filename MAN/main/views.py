import os
from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.conf import settings

from .models import Articles, News
from .forms import LoginForm, CreateArticleForm, CreateNewsForm
from .services.gnews_service import GNewsService



def main(request):
    return render(request, 'main/home.html',  {"articles": Articles.objects.all().order_by('-date')[:3], 'news': News.objects.all().order_by('-date')[:3]})

def articles(request):
    return render(request, 'main/articles.html', {"articles": Articles.objects.all().order_by('-date'), "news": News.objects.all().order_by('-date')})

def news(request):
    return render(request, 'main/news.html', {"articles": Articles.objects.all().order_by('-date'), "news": News.objects.all().order_by('-date')})

class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'main/article.html'
    context_object_name = 'article'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allArticles"] = Articles.objects.all()
        return context
    
class NewDetailView(DetailView):
    model = News
    template_name = 'main/new.html'
    context_object_name = 'new'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allNews"] = News.objects.all()
        return context


# def handle_uploaded_file(uploaded_file):
#     upload_folder = os.path.join(settings.STATICFILES_DIRS[0], 'ArticleImgs')
#     os.makedirs(upload_folder, exist_ok=True)
#     file_path = os.path.join(upload_folder, uploaded_file.name)
#     with open(file_path, 'wb+') as destination:
#         for chunk in uploaded_file.chunks():
#             destination.write(chunk)

#     return file_path


def publications(request):
    if request.user.is_authenticated:
        return render(request, 'main/publications.html', {"articles": Articles.objects.all().order_by('-date'), "news": News.objects.all().order_by('-date')})
    else:
        return redirect('home')
    
@login_required
def create_article(request):
    if request.method == 'POST':
        form = CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.date = request.POST.get('dateAndTime')
            form.instance.author = request.user
            form.save()
            return redirect('publications')
    else:
        form = CreateArticleForm()

    return render(request, 'main/create_A.html', {'form': form})
    
@login_required
def create_news(request):
    if request.method == 'POST':
        form = CreateNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.date = request.POST.get('dateAndTime')
            form.instance.author = request.user
            form.save()
            return redirect('publications')
    
    else:
        form = CreateNewsForm()

    return render(request, 'main/create_N.html', {'form': form})




class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Articles
    template_name = 'main/create_A.html'
    
    form_class = CreateArticleForm
    
class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = News
    template_name = 'main/create_N.html'
    
    form_class = CreateNewsForm


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Articles
    success_url = '/mypublications'
    template_name = 'main/delete.html'
    
class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    success_url = '/mypublications'
    template_name = 'main/delete.html'




def SearchAcricles(request):
    if request.method == 'GET':
        search_query = request.GET.get("q", "")
        if search_query:
            allarticles = Articles.objects.filter(name__icontains=search_query).order_by('-date')
        else:
            allarticles = Articles.objects.all()
            
        return render(request, 'main/articles.html', {"articles": allarticles, "news": News.objects.all().order_by('-date')})
    
def SearchNews(request):
    if request.method == 'GET':
        search_query = request.GET.get("q", "")
        if search_query:
            allnews = News.objects.filter(name__icontains=search_query).order_by('-date')
        else:
            allnews = News.objects.all()
            
        return render(request, 'main/news.html', {"news": allnews, "articles": Articles.objects.all().order_by('-date')})



# 
# class SearchAcricles(ListView):
#     def get_queryset(self):
#         return Articles.objects.filter(name__icontains=self.request.GET.get("q", ''))

#     # Для пагінації в майбутньому 
#     def get_context_data(self, *args, **kwargs: Any):
#         context = super().get_context_data(*args, **kwargs)
#         context['articles'] = self.request.GET.get("q")
#         return context
        
        
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def fetch_news(request):
    if not request.user.is_staff:
        messages.error(request, "У вас немає прав для цієї дії")
        return redirect('publications')
    
    service = GNewsService()
    result = service.fetch_news(query="Ukraine", max_articles=10)
    
    if 'error' in result:
        messages.error(request, f"Помилка при оновленні новин: {result['error']}")
    else:
        messages.success(request, result['success'])
    
    return redirect('publications')
