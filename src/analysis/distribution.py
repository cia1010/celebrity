import pandas as pd
import plotly.express as px

def visualize_profession_distribution(df):
    fig = px.pie(df, names="profession", title="职业分布")
    fig.show()

def visualize_country_distribution(df):
    fig = px.bar(df, x="country", y="name", title="国籍分布", color="country",
                 labels={"name": "名人数", "country": "国家"},
                 category_orders={"country": df["country"].value_counts().index.tolist()})
    fig.show()

if __name__ == "__main__":
    data = [
        {"name": "A", "net_worth": 1000000, "country": "US", "profession": "Actor"},
        {"name": "B", "net_worth": 500000, "country": "UK", "profession": "Singer"},
        {"name": "C", "net_worth": 800000, "country": "US", "profession": "Singer"}
    ]
    df = pd.DataFrame(data)
    visualize_profession_distribution(df)
    visualize_country_distribution(df)
