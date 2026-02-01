from .base_scraper import BaseScraper
from bs4 import BeautifulSoup

class WikiScraper(BaseScraper):
    def __init__(self, base_url):
        super().__init__(base_url)

    def parse(self, html):
        soup = BeautifulSoup(html, 'lxml')
        celebrities = []
        tables = soup.find_all("table", {"class": "wikitable"})
        for table in tables:
            for row in table.find_all("tr")[1:]:
                cols = row.find_all("td")
                if len(cols) >= 4:
                    name = cols[0].get_text(strip=True)
                    net_worth = cols[1].get_text(strip=True)
                    country = cols[2].get_text(strip=True)
                    profession = cols[3].get_text(strip=True)
                    celebrities.append({
                        "name": name,
                        "net_worth": net_worth,
                        "country": country,
                        "profession": profession
                    })
        return celebrities
