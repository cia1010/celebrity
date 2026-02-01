
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import streamlit as st
import pandas as pd
from CelebrityAnalyzer.core.analysis.stats_engine import AnalysisEngine
from CelebrityAnalyzer.core.database.db_handler import DBHandler
import plotly.express as px
import plotly.graph_objects as go

def main():
    st.set_page_config(page_title="全球名人数据洞察系统", layout="wide")
    st.markdown("""
    <style>
    .css-18e3th9 {background: #f5f7fa;}
    .css-1d391kg {background: #f5f7fa;}
    .logo-title {font-size:2.2em;font-weight:bold;color:#2b5876;letter-spacing:2px;}
    .footer {text-align:center;color:#888;font-size:0.9em;margin-top:2em;}
    </style>
    <div class="logo-title">🌏 全球名人数据洞察系统</div>
    """, unsafe_allow_html=True)

    db = DBHandler()
    df = db.get_all_data()
    if df.empty:
        st.warning("暂无数据，请先运行主流程采集数据。")
        return
    engine = AnalysisEngine(df)

    # 侧边栏多重筛选
    st.sidebar.header("筛选条件")
    country = st.sidebar.multiselect("选择国家", options=sorted(df['country'].dropna().unique()), default=None)
    profession = st.sidebar.multiselect("选择职业", options=sorted(df['profession'].dropna().unique()), default=None)
    min_worth, max_worth = float(df['net_worth'].min()), float(df['net_worth'].max())
    worth_range = st.sidebar.slider("净资产区间", min_value=min_worth, max_value=max_worth, value=(min_worth, max_worth), step=1000000.0, format="%.0f")
    df_filtered = df.copy()
    if country:
        df_filtered = df_filtered[df_filtered['country'].isin(country)]
    if profession:
        df_filtered = df_filtered[df_filtered['profession'].isin(profession)]
    df_filtered = df_filtered[(df_filtered['net_worth'] >= worth_range[0]) & (df_filtered['net_worth'] <= worth_range[1])]

    # 重要指标卡片
    total_celebs = len(df_filtered)
    total_wealth = df_filtered['net_worth'].sum()
    avg_wealth = df_filtered['net_worth'].mean()
    colA, colB, colC = st.columns(3)
    colA.metric("名人总数", f"{total_celebs}")
    colB.metric("总财富(USD)", f"{total_wealth:,.0f}")
    colC.metric("平均财富(USD)", f"{avg_wealth:,.0f}")

    # 年龄分布直方图
    if 'age' in df_filtered.columns:
        st.markdown("#### 🎂 年龄分布")
        fig_age = px.histogram(df_filtered, x='age', nbins=10, color='gender', title='名人年龄分布', labels={'age':'年龄'})
        st.plotly_chart(fig_age, use_container_width=True)

    # 性别比例
    if 'gender' in df_filtered.columns:
        st.markdown("#### 🚻 性别比例")
        gender_count = df_filtered['gender'].value_counts().reset_index()
        gender_count.columns = ['gender', 'count']
        fig_gender = px.pie(gender_count, names='gender', values='count', title='名人性别比例', hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_gender, use_container_width=True)

    # 粉丝数Top10
    if 'followers' in df_filtered.columns:
        st.markdown("#### 🌟 粉丝数Top10 名人")
        top_fans = df_filtered.sort_values('followers', ascending=False).head(10)
        fig_fans = px.bar(top_fans, x='name', y='followers', color='country', text='followers', title='粉丝数Top10', labels={'followers':'粉丝数'})
        st.plotly_chart(fig_fans, use_container_width=True)

    # 净资产分布直方图
    st.markdown("#### 💸 净资产分布直方图")
    fig_hist = px.histogram(df_filtered, x='net_worth', nbins=20, color='country', title='净资产分布', labels={'net_worth':'净资产(USD)'})
    st.plotly_chart(fig_hist, use_container_width=True)

    # 单一国家/职业Top榜
    st.markdown("#### 🏅 单一国家/职业净资产Top榜")
    colX, colY = st.columns(2)
    with colX:
        sel_country = st.selectbox("选择国家(Top5)", options=['全部']+sorted(df['country'].dropna().unique().tolist()))
        if sel_country != '全部':
            top_country = df[df['country']==sel_country].sort_values('net_worth', ascending=False).head(5)
        else:
            top_country = df.sort_values('net_worth', ascending=False).head(5)
        fig_c = px.bar(top_country, x='name', y='net_worth', color='profession', title=f'{sel_country}净资产Top5')
        st.plotly_chart(fig_c, use_container_width=True)
    with colY:
        sel_prof = st.selectbox("选择职业(Top5)", options=['全部']+sorted(df['profession'].dropna().unique().tolist()))
        if sel_prof != '全部':
            top_prof = df[df['profession']==sel_prof].sort_values('net_worth', ascending=False).head(5)
        else:
            top_prof = df.sort_values('net_worth', ascending=False).head(5)
        fig_p = px.bar(top_prof, x='name', y='net_worth', color='country', title=f'{sel_prof}净资产Top5')
        st.plotly_chart(fig_p, use_container_width=True)

    # 图表切换
    st.markdown("#### 📊 图表类型切换演示")
    chart_type = st.radio("选择图表类型", options=["柱状图", "折线图", "饼图"])
    if chart_type == "柱状图":
        st.plotly_chart(px.bar(df_filtered, x='name', y='net_worth', color='country', title='名人净资产柱状图'), use_container_width=True)
    elif chart_type == "折线图":
        st.plotly_chart(px.line(df_filtered, x='name', y='net_worth', color='country', title='名人净资产折线图'), use_container_width=True)
    else:
        st.plotly_chart(px.pie(df_filtered, names='name', values='net_worth', title='名人净资产饼图'), use_container_width=True)

    # 国家分布、职业分布
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🌍 国家分布")
        country_count = df_filtered['country'].value_counts().reset_index()
        country_count.columns = ['country', 'count']
        fig2 = px.pie(country_count, names='country', values='count', title='名人国别分布', hole=0.4)
        st.plotly_chart(fig2, use_container_width=True)
    with col2:
        st.markdown("#### 🏆 职业分布")
        prof_count = df_filtered['profession'].value_counts().reset_index()
        prof_count.columns = ['profession', 'count']
        fig3 = px.bar(prof_count, x='profession', y='count', color='profession', title='职业分布')
        st.plotly_chart(fig3, use_container_width=True)

    # 财富分布（按国家均值）
    st.markdown("#### 📈 财富分布（按国家均值）")
    wealth_dist = engine.get_wealth_distribution().reset_index()
    wealth_dist.columns = ['country', 'mean_net_worth']
    fig4 = px.bar(wealth_dist, x='country', y='mean_net_worth', color='country', title='各国名人平均净资产')
    st.plotly_chart(fig4, use_container_width=True)

    # 数据导出按钮
    st.markdown("#### ⬇️ 数据导出")
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button("导出筛选后数据为CSV", csv, "celebrities_filtered.csv", "text/csv")

    st.markdown("#### 全部数据明细")
    st.dataframe(df_filtered, use_container_width=True)

    st.markdown('<div class="footer">© 2026 CelebrityAnalyzer | Powered by Streamlit & Plotly</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import streamlit as st
import pandas as pd
from CelebrityAnalyzer.core.analysis.stats_engine import AnalysisEngine
from CelebrityAnalyzer.core.database.db_handler import DBHandler



import plotly.express as px
import plotly.graph_objects as go


    st.set_page_config(page_title="全球名人数据洞察系统", layout="wide")
    st.markdown("""
    <style>
    .css-18e3th9 {background: #f5f7fa;}
    .css-1d391kg {background: #f5f7fa;}
    .logo-title {font-size:2.2em;font-weight:bold;color:#2b5876;letter-spacing:2px;}
    .footer {text-align:center;color:#888;font-size:0.9em;margin-top:2em;}
    </style>
    <div class="logo-title">🌏 全球名人数据洞察系统</div>
    """, unsafe_allow_html=True)

    db = DBHandler()
    df = db.get_all_data()
    if df.empty:
        st.warning("暂无数据，请先运行主流程采集数据。")
        return
    engine = AnalysisEngine(df)

    # 侧边栏多重筛选
    st.sidebar.header("筛选条件")
    country = st.sidebar.multiselect("选择国家", options=sorted(df['country'].dropna().unique()), default=None)
    profession = st.sidebar.multiselect("选择职业", options=sorted(df['profession'].dropna().unique()), default=None)
    min_worth, max_worth = float(df['net_worth'].min()), float(df['net_worth'].max())
    worth_range = st.sidebar.slider("净资产区间", min_value=min_worth, max_value=max_worth, value=(min_worth, max_worth), step=1000000.0, format="%.0f")
    df_filtered = df.copy()
    if country:
        df_filtered = df_filtered[df_filtered['country'].isin(country)]
    if profession:
        df_filtered = df_filtered[df_filtered['profession'].isin(profession)]
    df_filtered = df_filtered[(df_filtered['net_worth'] >= worth_range[0]) & (df_filtered['net_worth'] <= worth_range[1])]

    # 重要指标卡片
    total_celebs = len(df_filtered)
    total_wealth = df_filtered['net_worth'].sum()
    avg_wealth = df_filtered['net_worth'].mean()
    colA, colB, colC = st.columns(3)
    colA.metric("名人总数", f"{total_celebs}")
    colB.metric("总财富(USD)", f"{total_wealth:,.0f}")
    colC.metric("平均财富(USD)", f"{avg_wealth:,.0f}")

    # 净资产分布直方图
    st.markdown("#### 💸 净资产分布直方图")
    fig_hist = px.histogram(df_filtered, x='net_worth', nbins=20, color='country', title='净资产分布', labels={'net_worth':'净资产(USD)'})
    st.plotly_chart(fig_hist, use_container_width=True)

    # 单一国家/职业Top榜
    st.markdown("#### 🏅 单一国家/职业净资产Top榜")
    colX, colY = st.columns(2)
    with colX:
        sel_country = st.selectbox("选择国家(Top5)", options=['全部']+sorted(df['country'].dropna().unique().tolist()))
        if sel_country != '全部':
            top_country = df[df['country']==sel_country].sort_values('net_worth', ascending=False).head(5)
        else:
            top_country = df.sort_values('net_worth', ascending=False).head(5)
        fig_c = px.bar(top_country, x='name', y='net_worth', color='profession', title=f'{sel_country}净资产Top5')
        st.plotly_chart(fig_c, use_container_width=True)
    with colY:
        sel_prof = st.selectbox("选择职业(Top5)", options=['全部']+sorted(df['profession'].dropna().unique().tolist()))
        if sel_prof != '全部':
            top_prof = df[df['profession']==sel_prof].sort_values('net_worth', ascending=False).head(5)
        else:
            top_prof = df.sort_values('net_worth', ascending=False).head(5)
        fig_p = px.bar(top_prof, x='name', y='net_worth', color='country', title=f'{sel_prof}净资产Top5')
        st.plotly_chart(fig_p, use_container_width=True)

    # 图表切换
    st.markdown("#### 📊 图表类型切换演示")
    chart_type = st.radio("选择图表类型", options=["柱状图", "折线图", "饼图"])
    if chart_type == "柱状图":
        st.plotly_chart(px.bar(df_filtered, x='name', y='net_worth', color='country', title='名人净资产柱状图'), use_container_width=True)
    elif chart_type == "折线图":
        st.plotly_chart(px.line(df_filtered, x='name', y='net_worth', color='country', title='名人净资产折线图'), use_container_width=True)
    else:
        st.plotly_chart(px.pie(df_filtered, names='name', values='net_worth', title='名人净资产饼图'), use_container_width=True)

    # 国家分布、职业分布
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🌍 国家分布")
        country_count = df_filtered['country'].value_counts().reset_index()
        country_count.columns = ['country', 'count']
        fig2 = px.pie(country_count, names='country', values='count', title='名人国别分布', hole=0.4)
        st.plotly_chart(fig2, use_container_width=True)
    with col2:
        st.markdown("#### 🏆 职业分布")
        prof_count = df_filtered['profession'].value_counts().reset_index()
        prof_count.columns = ['profession', 'count']
        fig3 = px.bar(prof_count, x='profession', y='count', color='profession', title='职业分布')
        st.plotly_chart(fig3, use_container_width=True)

    # 财富分布（按国家均值）
    st.markdown("#### 📈 财富分布（按国家均值）")
    wealth_dist = engine.get_wealth_distribution().reset_index()
    wealth_dist.columns = ['country', 'mean_net_worth']
    fig4 = px.bar(wealth_dist, x='country', y='mean_net_worth', color='country', title='各国名人平均净资产')
    st.plotly_chart(fig4, use_container_width=True)

    # 数据导出按钮
    st.markdown("#### ⬇️ 数据导出")
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button("导出筛选后数据为CSV", csv, "celebrities_filtered.csv", "text/csv")

    st.markdown("#### 全部数据明细")
    st.dataframe(df_filtered, use_container_width=True)

    st.markdown('<div class="footer">© 2026 CelebrityAnalyzer | Powered by Streamlit & Plotly</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
