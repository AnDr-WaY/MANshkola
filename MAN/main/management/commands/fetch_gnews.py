from django.core.management.base import BaseCommand
from main.services.gnews_service import GNewsService

class Command(BaseCommand):
    help = 'Fetches news from GNews API'

    def add_arguments(self, parser):
        parser.add_argument(
            '--query',
            type=str,
            default='Ukraine',
            help='Search query for news'
        )
        parser.add_argument(
            '--max',
            type=int,
            default=10,
            help='Maximum number of articles to fetch'
        )

    def handle(self, *args, **options):
        service = GNewsService()
        result = service.fetch_news(
            query=options['query'],
            max_articles=options['max']
        )
        
        if 'error' in result:
            self.stderr.write(self.style.ERROR(result['error']))
        else:
            self.stdout.write(self.style.SUCCESS(result['success'])) 