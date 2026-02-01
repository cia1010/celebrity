from CelebrityAnalyzer.core.scraper.wiki_scraper import WikiScraper
from CelebrityAnalyzer.core.scraper.imdb_scraper import IMDBScraper
from CelebrityAnalyzer.core.processor.cleaner import DataCleaner
from CelebrityAnalyzer.core.database.db_handler import DBHandler

def start_project():
    # 1. 爬取数据
    wiki = WikiScraper("https://en.wikipedia.org/wiki/List_of_people_by_net_worth")
    imdb = IMDBScraper("https://www.imdb.com/list/ls052283250/")
    raw_data = wiki.run() + imdb.run()
    # 2. 清洗数据
    for d in raw_data:
        d["net_worth"] = DataCleaner.clean_net_worth(d.get("net_worth"))
    # 3. 存入数据库
    db = DBHandler()
    db.save_celebrity(raw_data)
    print("项目阶段 1：爬取与存储完成")

if __name__ == "__main__":
    start_project()
