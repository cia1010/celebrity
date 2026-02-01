import streamlit as st
import pandas as pd
from CelebrityAnalyzer.core.analysis.stats_engine import AnalysisEngine
from CelebrityAnalyzer.core.database.db_handler import DBHandler

def main():
    st.title("全球名人数据洞察系统")
    db = DBHandler()
    df = db.get_all_data()
    if df.empty:
        st.warning("暂无数据，请先运行主流程采集数据。")
        return
    engine = AnalysisEngine(df)
    st.subheader("财富分布（按国家均值）")
    st.bar_chart(engine.get_wealth_distribution())
    st.subheader("热门行业Top10")
    st.bar_chart(engine.get_top_industries())
    st.dataframe(df)

if __name__ == "__main__":
    main()
