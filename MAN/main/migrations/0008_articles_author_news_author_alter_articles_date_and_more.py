# Generated by Django 4.2.7 on 2023-12-04 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_news_remove_articles_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації'),
        ),
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Назва'),
        ),
    ]
