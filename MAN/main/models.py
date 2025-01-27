from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField('Назва', max_length=150)
    content = models.TextField('Зміст')
    icon = models.ImageField('Картинка', upload_to = 'main/static/main/ArticleImgs/')
    date = models.DateTimeField("Дата публікації", auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Стаття: {self.name}"
       
    def get_absolute_url(self):
        return f'/articles/{self.id}'
       
    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
        

class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField('Назва', max_length=150)
    content = models.TextField('Зміст')
    icon = models.ImageField('Картинка', upload_to='main/static/main/ArticleImgs/', null=True, blank=True)
    icon_url = models.URLField('URL картинки', max_length=500, null=True, blank=True)
    date = models.DateTimeField("Дата публікації", auto_now_add=True)
    source_url = models.URLField('Source URL', max_length=500, null=True, blank=True)
    source_name = models.CharField('Source Name', max_length=200, null=True, blank=True)
    is_from_gnews = models.BooleanField('From GNews', default=False)
    
    def __str__(self) -> str:
        return f"Новина: {self.name}"
    
    def get_absolute_url(self):
        return f'/news/{self.id}'   
    
    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'


class GNewsAPILog(models.Model):
    date = models.DateField('Request Date', default=timezone.now)
    requests_count = models.IntegerField('Requests Count', default=0)
    last_fetch_time = models.DateTimeField('Last Fetch Time', null=True, blank=True)

    class Meta:
        verbose_name = 'GNews API Log'
        verbose_name_plural = 'GNews API Logs'

    def __str__(self):
        return f"API Requests on {self.date}: {self.requests_count}"

    def can_fetch_now(self):
        if not self.last_fetch_time:
            return True
            
        # 24 hours * 3600 seconds / 80 requests = 1080 seconds between requests
        min_interval = timezone.timedelta(seconds=1080)  # ~18 minutes
        time_since_last_fetch = timezone.now() - self.last_fetch_time
        
        return time_since_last_fetch >= min_interval

