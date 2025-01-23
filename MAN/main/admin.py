from django.contrib import admin
from .models import Articles, News, GNewsAPILog

# Register your models here.
admin.site.register(Articles)
admin.site.register(News)
admin.site.register(GNewsAPILog)