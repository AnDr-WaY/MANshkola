# Generated by Django 4.2.7 on 2023-12-06 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_articles_author_alter_news_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='views',
        ),
    ]