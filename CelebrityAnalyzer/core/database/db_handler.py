# 可扩展为MongoDB或PostgreSQL
import pandas as pd
import os

class DBHandler:
    def __init__(self, path='CelebrityAnalyzer/data/processed/celebrities.csv'):
        self.path = path

    def save_celebrity(self, data):
        df = pd.DataFrame(data)
        if os.path.exists(self.path):
            old = pd.read_csv(self.path)
            df = pd.concat([old, df], ignore_index=True).drop_duplicates(subset=['name'])
        df.to_csv(self.path, index=False)

    def get_all_data(self):
        if os.path.exists(self.path):
            return pd.read_csv(self.path)
        return pd.DataFrame([])
