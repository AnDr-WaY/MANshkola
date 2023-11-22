from django.shortcuts import render
from .models import Articles

# Create your views here.
def main(request):
    return render(request, 'main/home.html')

def news(request):
    return render(request, 'main/news.html', {"articles": Articles.objects.all()})