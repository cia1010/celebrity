import requests
from src.utils.antibot import get_headers, random_delay

def fetch_twitter_followers(username):
    # 这里只做接口结构示例，实际需用API或第三方库
    url = f"https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names={username}"
    resp = requests.get(url, headers=get_headers())
    random_delay()
    if resp.status_code == 200:
        data = resp.json()
        if data:
            return data[0].get("followers_count", 0)
    return None

if __name__ == "__main__":
    print(fetch_twitter_followers("elonmusk"))
