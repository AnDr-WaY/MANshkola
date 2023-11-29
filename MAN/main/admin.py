from django.contrib import admin
from .models import Articles, News

# Register your models here.
admin.site.register(Articles)
admin.site.register(News)