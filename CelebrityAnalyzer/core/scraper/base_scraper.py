import httpx
import time
import random

class BaseScraper:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {"User-Agent": "Mozilla/5.0 (compatible; CelebrityBot/1.0)"}
        self.client = httpx.Client(headers=self.headers)

    def get_page(self, url):
        for _ in range(3):
            try:
                resp = self.client.get(url, timeout=10)
                if resp.status_code == 200:
                    time.sleep(random.uniform(1, 3))
                    return resp.text
            except Exception as e:
                print(f"请求失败: {e}")
                time.sleep(2)
        return None

    def parse(self, html):
        raise NotImplementedError

    def run(self):
        html = self.get_page(self.base_url)
        if html:
            return self.parse(html)
        return []
