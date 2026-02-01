import sys
import os
import importlib
import pandas as pd
import logging
from datetime import datetime
from src.cleaning.cleaning import clean_celebrities
from src.crawler.social_crawler import fetch_twitter_followers

# 各爬虫模块路径
CRAWLER_MODULES = [
    'src.crawler.forbes_crawler',
    'src.crawler.wikipedia_crawler',
    'src.crawler.imdb_crawler',
]

ALL_DATA = []

def run_all_crawlers():
    for module_name in CRAWLER_MODULES:
        try:
            module = importlib.import_module(module_name.replace('/', '.'))
            if hasattr(module, 'fetch_forbes_celebrities'):
                data = module.fetch_forbes_celebrities()
            elif hasattr(module, 'fetch_wikipedia_celebrities'):
                data = module.fetch_wikipedia_celebrities()
            elif hasattr(module, 'fetch_imdb_celebrities'):
                data = module.fetch_imdb_celebrities()
            else:
                data = []
            ALL_DATA.extend(data)
            logging.info(f"{module_name} 爬取成功，获取{len(data)}条数据")
        except Exception as e:
            logging.error(f"{module_name} 爬取失败: {e}")
    return ALL_DATA


def enrich_with_social_data(df):
    # 假设有twitter用户名列
    if 'twitter' in df.columns:
        def safe_fetch(x):
            try:
                return fetch_twitter_followers(x) if pd.notnull(x) else None
            except Exception as e:
                logging.warning(f"获取 {x} 粉丝数失败: {e}")
                return None
        df['followers'] = df['twitter'].apply(safe_fetch)
    return df

def main():
    log_file = f"logs/pipeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    os.makedirs('logs', exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )
    try:
        raw_data = run_all_crawlers()
        df = clean_celebrities(raw_data)
        df = enrich_with_social_data(df)
        df.to_csv('data/celebrities_cleaned.csv', index=False)
        logging.info('数据采集、清洗、社交数据补全完成，已保存至 data/celebrities_cleaned.csv')
        print('数据采集、清洗、社交数据补全完成，已保存至 data/celebrities_cleaned.csv')
    except Exception as e:
        logging.critical(f"主流程异常: {e}")
        print(f"主流程异常: {e}")

if __name__ == "__main__":
    # 支持命令行参数 --cron 用于定时任务场景
    if '--cron' in sys.argv:
        print(f"[CRON] {datetime.now()} 自动调度启动...")
    main()
