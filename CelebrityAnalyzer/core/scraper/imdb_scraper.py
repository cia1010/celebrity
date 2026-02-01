from .base_scraper import BaseScraper
from bs4 import BeautifulSoup

class IMDBScraper(BaseScraper):
    def __init__(self, base_url):
        super().__init__(base_url)

    def parse(self, html):
        soup = BeautifulSoup(html, 'lxml')
        celebrities = []
        for item in soup.select(".lister-item.mode-detail"):
            name = item.select_one(".lister-item-header a").get_text(strip=True)
            celebrities.append({
                "name": name,
                "net_worth": None,
                "country": None,
                "profession": None
            })
        return celebrities
