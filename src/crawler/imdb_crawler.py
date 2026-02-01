import requests
from bs4 import BeautifulSoup
from src.utils.antibot import get_headers, random_delay

IMDB_URL = "https://www.imdb.com/list/ls052283250/"

def fetch_imdb_celebrities():
    html = requests.get(IMDB_URL, headers=get_headers()).text
    random_delay()
    soup = BeautifulSoup(html, "lxml")
    celebrities = []
    for item in soup.select(".lister-item.mode-detail"):
        name = item.select_one(".lister-item-header a").get_text(strip=True)
        # IMDB页面可能没有净资产、国籍等，需后续补充
        celebrities.append({
            "name": name,
            "net_worth": None,
            "country": None,
            "profession": None
        })
    return celebrities

if __name__ == "__main__":
    data = fetch_imdb_celebrities()
    print(data)
