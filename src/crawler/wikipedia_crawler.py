import requests
from bs4 import BeautifulSoup
from src.utils.antibot import get_headers, random_delay

WIKI_URL = "https://en.wikipedia.org/wiki/List_of_people_by_net_worth"

def fetch_wikipedia_celebrities():
    html = requests.get(WIKI_URL, headers=get_headers()).text
    random_delay()
    soup = BeautifulSoup(html, "lxml")
    celebrities = []
    # 以表格为例，需根据实际页面结构调整
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

if __name__ == "__main__":
    data = fetch_wikipedia_celebrities()
    print(data)
