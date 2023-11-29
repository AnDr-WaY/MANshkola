from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView

# Create your views here.
def main(request):
    return render(request, 'main/home.html',  {"articles": Articles.objects.all()})

def articles(request):
    return render(request, 'main/articles.html', {"articles": Articles.objects.all()})


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'main/article.html'
    context_object_name = 'article'