from django.db import models

# Create your models here.
class Articles(models.Model):
    
    name = models.CharField('Назва', max_length=50)
    content = models.TextField('Зміст')
    icon = models.ImageField('Картинка', upload_to = 'main/static/main/ArticleImgs/')
    date = models.DateTimeField("Дата публікації", auto_now=True)
    views = models.IntegerField("Перегляди", default=0)
    
    def __str__(self) -> str:
        return f"Стаття {self.name}"
       
    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'