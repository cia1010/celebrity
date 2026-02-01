# 可扩展为MongoDB或PostgreSQL
import pandas as pd
import os

class DBHandler:
    def __init__(self, path='CelebrityAnalyzer/data/processed/celebrities.csv'):
        self.path = path

    def save_celebrity(self, data):
        df = pd.DataFrame(data)
        if os.path.exists(self.path):
            try:
                old = pd.read_csv(self.path)
                # 若旧文件为空则直接覆盖
                if old.empty or len(old.columns) == 0:
                    df.to_csv(self.path, index=False)
                    return
                df = pd.concat([old, df], ignore_index=True).drop_duplicates(subset=['name'])
            except pd.errors.EmptyDataError:
                df.to_csv(self.path, index=False)
                return
        df.to_csv(self.path, index=False)

    def get_all_data(self):
        if os.path.exists(self.path):
            return pd.read_csv(self.path)
        return pd.DataFrame([])
