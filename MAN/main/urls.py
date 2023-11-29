from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('articles', views.articles, name='articles'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='articles-detail'),
]
