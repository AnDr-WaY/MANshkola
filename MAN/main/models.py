from django.db import models
from django.contrib.auth.models import User


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
    icon = models.ImageField('Картинка', upload_to = 'main/static/main/ArticleImgs/')
    date = models.DateTimeField("Дата публікації", auto_now_add=True)

    
    def __str__(self) -> str:
        return f"Новина: {self.name}"
    
    def get_absolute_url(self):
        return f'/news/{self.id}'   
    
    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
    