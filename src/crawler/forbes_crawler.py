import requests
from bs4 import BeautifulSoup
import random
import time
from src.utils.antibot import get_headers, random_delay

# Forbes 名人榜爬虫示例
FORBES_URL = "https://www.forbes.com/celebrities/"


def fetch_forbes_celebrities():
    html = requests.get(FORBES_URL, headers=get_headers()).text
    random_delay()
    soup = BeautifulSoup(html, "lxml")
    celebrities = []
    # 这里只做结构示例，具体解析需根据页面结构调整
    for item in soup.select(".profile-row"):
        name = item.select_one(".profile-name").get_text(strip=True)
        net_worth = item.select_one(".profile-net-worth").get_text(strip=True)
        country = item.select_one(".profile-country").get_text(strip=True)
        profession = item.select_one(".profile-profession").get_text(strip=True)
        celebrities.append({
            "name": name,
            "net_worth": net_worth,
            "country": country,
            "profession": profession
        })
    return celebrities

if __name__ == "__main__":
    data = fetch_forbes_celebrities()
    print(data)
