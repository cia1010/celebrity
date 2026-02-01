import random
import time
from fake_useragent import UserAgent

def get_headers():
    ua = UserAgent()
    return {'User-Agent': ua.random}

def random_delay():
    time.sleep(random.uniform(1, 3))

# 代理池示例（可扩展为动态获取代理）
def get_proxy():
    proxies = [
        # "http://proxy1:port",
        # "http://proxy2:port",
    ]
    if proxies:
        return {"http": random.choice(proxies)}
    return None
