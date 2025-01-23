from django.apps import AppConfig
from django.conf import settings


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        # Prevent running scheduler twice in development
        import sys
        if not settings.DEBUG or (len(sys.argv) > 1 and sys.argv[1] == 'runserver'):
            # Import here to avoid circular import
            from .scheduler import NewsScheduler
            scheduler = NewsScheduler()
            scheduler.start()
