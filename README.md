# CelebrityAnalyzer | 全球名人数据分析系统

[English](#english) | [中文](#中文)

---

## English

### 🌟 Project Overview
**CelebrityAnalyzer** is a full-stack data engineering project designed to crawl, process, and analyze data of global celebrities from multiple sources (Wikipedia, IMDb, Forbes, etc.). It provides insights into wealth distribution, career trends, and social influence through an interactive dashboard.

### 🚀 Key Features
- **Multi-source Scraper**: Modular crawlers for different platforms with anti-bot measures.
- **ETL Pipeline**: Automated data cleaning, currency normalization, and date formatting.
- **Statistical Analysis**: Deep dive into celebrity demographics, net worth, and industry patterns.
- **Interactive Dashboard**: Real-time data visualization built with Streamlit.

### 📂 Project Structure
```text
CelebrityAnalyzer/
├── app/                # Dashboard UI (Streamlit)
├── config/             # Configuration (API keys, site rules)
├── core/               # Core Logic (The "Brain" of the project)
│   ├── scraper/        # Scraper implementations (Wiki, IMDb)
│   ├── processor/      # Data cleaning logic
│   ├── database/       # DB handlers (SQL/NoSQL)
│   └── analysis/       # Stats and analytics engine
├── data/               # Data storage (Raw & Processed)
├── logs/               # Operational logs
├── main.py             # Project entry point
└── requirements.txt    # Python dependencies
```

### 🛠️ Tech Stack
- **Language**: Python 3.9+
- **Scraping**: `httpx`, `BeautifulSoup4`, `Playwright`
- **Data**: `Pandas`, `NumPy`, `SQLAlchemy`
- **Visualization**: `Streamlit`, `Plotly`

### 📦 Quick Start
1. **Clone**: `git clone https://github.com/username/CelebrityAnalyzer.git`
2. **Install**: `pip install -r requirements.txt`
3. **Run Pipeline**: `python main.py`
4. **Launch App**: `streamlit run app/dashboard.py`

---

## 中文

### 🌟 项目简介
**CelebrityAnalyzer** 是一个全栈数据工程项目，旨在从多个渠道（如维基百科、IMDb、福布斯等）抓取全球名人的信息。项目涵盖了从自动化爬虫、数据清洗（ETL）到深度数据分析及交互式可视化展示的完整流程。

### 🚀 核心功能
- **多源爬虫系统**：针对不同平台设计的模块化爬虫，集成反爬虫策略。
- **自动化 ETL 流水线**：自动清洗数据，统一货币单位，标准化日期格式。
- **深度数据挖掘**：分析名人财富分布、行业趋势及地域产出比。
- **交互式仪表盘**：基于 Streamlit 构建，支持动态筛选与图表展示。

### 📂 目录结构
```text
CelebrityAnalyzer/
├── app/                # 可视化前端 (Streamlit)
├── config/             # 项目配置 (API 密钥、站点规则)
├── core/               # 核心逻辑 (项目的“大脑”)
│   ├── scraper/        # 爬虫具体实现
│   ├── processor/      # 数据清洗与处理
│   ├── database/       # 数据库交互
│   └── analysis/       # 统计分析引擎
├── data/               # 数据存放 (原始数据与清洗后数据)
├── logs/               # 运行日志
├── main.py             # 项目启动入口
└── requirements.txt    # 依赖库清单
```

### 🛠️ 技术栈
- **编程语言**: Python 3.9+
- **爬虫技术**: `httpx`, `BeautifulSoup4`, `Playwright`
- **数据处理**: `Pandas`, `NumPy`, `SQLAlchemy`
- **可视化**: `Streamlit`, `Plotly`

### 📦 快速开始
1. **克隆项目**: `git clone https://github.com/username/CelebrityAnalyzer.git`
2. **安装依赖**: `pip install -r requirements.txt`
3. **执行流程**: `python main.py`
4. **启动看板**: `streamlit run app/dashboard.py`

---

### ⚠️ Disclaimer / 免责声明
This project is for educational purposes only. Please adhere to the **robots.txt** of target websites and local data privacy laws (e.g., GDPR).
本项目仅供学习研究使用。请务必遵守目标网站的 **robots.txt** 协议及当地法律法规。
