import pandas as pd
import plotly.express as px

def visualize_net_worth(df):
    fig = px.bar(df, x="name", y="net_worth", color="country", title="全球名人净资产分布")
    fig.show()

if __name__ == "__main__":
    # 示例数据
    data = [
        {"name": "A", "net_worth": 1000000, "country": "US"},
        {"name": "B", "net_worth": 500000, "country": "UK"}
    ]
    df = pd.DataFrame(data)
    visualize_net_worth(df)
