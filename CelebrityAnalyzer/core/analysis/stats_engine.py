import pandas as pd

class AnalysisEngine:
    def __init__(self, dataframe):
        self.df = dataframe

    def get_wealth_distribution(self):
        return self.df.groupby('country')['net_worth'].mean()

    def get_top_industries(self, n=10):
        return self.df['profession'].value_counts().head(n)
