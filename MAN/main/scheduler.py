import threading
import time
from datetime import datetime, timedelta
from .services.gnews_service import GNewsService
from django.utils import timezone

class NewsScheduler:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(NewsScheduler, cls).__new__(cls)
                cls._instance.is_running = False
                cls._instance.thread = None
            return cls._instance

    def fetch_news_task(self):
        while self.is_running:
            try:
                service = GNewsService()
                result = service.fetch_news(query="Ukraine", max_articles=10)
                if 'error' in result:
                    print(f"Error fetching news: {result['error']}")
                else:
                    print(f"Success: {result['success']}")
            except Exception as e:
                print(f"Error in news fetch task: {e}")
            

            for _ in range(15):  
                if not self.is_running:
                    break
                time.sleep(60)  

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.thread = threading.Thread(target=self.fetch_news_task, daemon=True)
            self.thread.start()
            print("News scheduler started")

    def stop(self):
        if self.is_running:
            self.is_running = False
            if self.thread:
                self.thread.join(timeout=1)
            print("News scheduler stopped") 