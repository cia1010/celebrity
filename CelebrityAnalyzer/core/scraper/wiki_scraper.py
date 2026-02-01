from .base_scraper import BaseScraper
from bs4 import BeautifulSoup

class WikiScraper(BaseScraper):
    def __init__(self, base_url):
        super().__init__(base_url)

    def parse(self, html):
        soup = BeautifulSoup(html, 'lxml')
        celebrities = []
        # 1. 找到所有子页面链接（如List of richest people等）
        content_div = soup.find('div', {'class': 'mw-parser-output'})
        links = []
        if content_div:
            for li in content_div.find_all('li'):
                a = li.find('a', href=True)
                if a and 'List_of_' in a['href'] and 'people' in a['href']:
                    full_url = 'https://en.wikipedia.org' + a['href']
                    links.append(full_url)
        # 2. 递归抓取每个子页面的wikitable
        for url in links:
            sub_html = self.get_page(url)
            if not sub_html:
                continue
            sub_soup = BeautifulSoup(sub_html, 'lxml')
            tables = sub_soup.find_all("table", {"class": "wikitable"})
            for table in tables:
                headers = [th.get_text(strip=True).lower() for th in table.find_all('th')]
                for row in table.find_all("tr")[1:]:
                    cols = row.find_all("td")
                    if len(cols) >= 2:
                        # 尝试智能匹配字段
                        name = cols[0].get_text(strip=True)
                        net_worth = None
                        country = None
                        profession = None
                        for i, h in enumerate(headers[1:], 1):
                            val = cols[i].get_text(strip=True) if i < len(cols) else None
                            if 'net worth' in h:
                                net_worth = val
                            elif 'country' in h or 'nationality' in h:
                                country = val
                            elif 'occupation' in h or 'profession' in h or 'industry' in h:
                                profession = val
                        celebrities.append({
                            "name": name,
                            "net_worth": net_worth,
                            "country": country,
                            "profession": profession
                        })
        return celebrities
