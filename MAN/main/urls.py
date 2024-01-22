from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('articles', views.articles, name='articles'),
    path('news', views.news, name='news'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='articles-detail'),
    path('news/<int:pk>', views.NewDetailView.as_view(), name='news-detail'),
    
    path('articles/search', views.SearchAcricles, name="search-articles"),
    path('news/search', views.SearchNews, name="search-news"),
    
    path('articles/<int:pk>/update', views.ArticleUpdateView.as_view(), name='articles-update'),
    path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    
    path('articles/<int:pk>/delete', views.ArticleDeleteView.as_view(), name='articles-delete'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    
    
    
    path('mypublications', views.publications, name='publications'),
    path('create/article', views.create_article, name='create_article'),
    path('create/news', views.create_news, name='create_news'),
    
    
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
]
