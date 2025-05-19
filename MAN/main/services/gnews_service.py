import os
import requests
from datetime import datetime
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from ..models import News, GNewsAPILog

class GNewsService:
    BASE_URL = "https://gnews.io/api/v4/search"
    
    def __init__(self):
        self.api_key = os.getenv('GNEWS_API_KEY')
        if not self.api_key:
            raise ValueError("GNEWS_API_KEY environment variable is not set")
        
        self.system_user, _ = User.objects.get_or_create(
            username='system_gnews',
            defaults={'is_staff': True}
        )

    def _get_or_create_log(self):
        today = timezone.now().date()
        log, _ = GNewsAPILog.objects.get_or_create(date=today)
        return log

    def can_make_request(self):
        log = self._get_or_create_log()
        if log.requests_count >= 80: 
            return False
        return True #log.can_fetch_now()  

    def fetch_news(self, query="Ukraine", max_articles=10):
        if not self.can_make_request():
            return {"error": "Cannot fetch now. Either daily limit reached or too soon since last fetch."}

        try:
            params = {
                "q": query,
                "lang": "uk",  
                "country": "ua",  
                "max": max_articles,
                "expand": "content",  
                "apikey": self.api_key
            }
            
            response = requests.get(self.BASE_URL, params=params)
            
            log = self._get_or_create_log()
            log.requests_count += 1
            log.last_fetch_time = timezone.now()
            log.save()
            
            if response.status_code == 200:
                data = response.json()
                self._save_articles(data.get('articles', []))
                return {"success": f"Fetched {len(data.get('articles', []))} articles"}
            else:
                return {"error": f"API request failed with status code {response.status_code}"}

        except Exception as e:
            return {"error": str(e)}

    def _save_articles(self, articles):
        for article in articles:
            if News.objects.filter(source_url=article.get('url')).exists():
                continue

            
            content = article.get('content', '')
            if not content:
                content = article.get('description', '')

            if content:
                content = content.split(' [', 1)[0]
            content += ' більше дивитися на сайті публікатора:'
           
            source_link = f'\n\n<a class="dzer" target="_blank" href="{article.get("url", "")}">Джерело інформації</a>'
            content = content + source_link

            News.objects.create(
                author=self.system_user,
                name=article.get('title', ''),
                content=content,
                icon_url=article.get('image', ''),  
                source_url=article.get('url', ''),
                source_name=article.get('source', {}).get('name', ''),
                is_from_gnews=True
            )