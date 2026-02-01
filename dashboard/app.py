import streamlit as st
import pandas as pd
import plotly.express as px

st.title("全球名人数据洞察系统")

# 假设已加载清洗后的数据
@st.cache_data
def load_data():
    # 实际应从data/目录加载
    return pd.DataFrame([
        {"name": "A", "net_worth": 1000000, "country": "US", "profession": "Actor", "followers": 10000000},
        {"name": "B", "net_worth": 500000, "country": "UK", "profession": "Singer", "followers": 2000000},
    ])

df = load_data()

st.subheader("名人净资产分布")
fig = px.bar(df, x="name", y="net_worth", color="country")
st.plotly_chart(fig)

st.subheader("社交媒体粉丝数")
fig2 = px.bar(df, x="name", y="followers", color="profession")
st.plotly_chart(fig2)

st.dataframe(df)
