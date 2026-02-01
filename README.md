
# CelebrityAnalyzer

全球名人数据洞察系统

## 项目简介
CelebrityAnalyzer 是一个全栈数据项目，自动化爬取、清洗、分析全球名人信息，并通过可视化仪表盘展示洞察。支持多数据源、模块化扩展、自动化调度。

## 功能特性
- 多网站爬虫（如 Wikipedia、IMDB、Forbes 等）
- 数据清洗与标准化（净资产、国籍、职业等）
- 数据存储（CSV，支持扩展 MongoDB/PostgreSQL）
- 数据分析（财富分布、热门行业等）
- Streamlit 可视化仪表盘
- 自动化调度（支持 GitHub Actions 定时运行）

## 目录结构
```
CelebrityAnalyzer/
├── config/           # 配置文件
├── core/             # 核心模块（爬虫/清洗/数据库/分析）
├── data/             # 数据存储（raw/processed）
├── app/              # 可视化仪表盘
├── logs/             # 日志
├── main.py           # 主入口
└── requirements.txt  # 依赖
```

## 快速开始
1. 安装依赖
	```bash
	pip install -r CelebrityAnalyzer/requirements.txt
	```
2. 运行主流程（采集+清洗+存储）
	```bash
	python CelebrityAnalyzer/main.py
	```
3. 启动可视化仪表盘
	```bash
	streamlit run CelebrityAnalyzer/app/dashboard.py
	```

## 自动化与CI
已集成 GitHub Actions，支持 push/定时/手动自动运行主流程，产出数据自动上传 artifact。

## 扩展与定制
- 新增数据源：在 core/scraper/ 下添加新爬虫子类，并注册到 main.py
- 切换数据库：实现 core/database/db_handler.py 的 MongoDB/PostgreSQL 版本
- 增加分析维度：在 core/analysis/stats_engine.py 中扩展分析方法

## 贡献与反馈
欢迎提交 issue 或 PR 共同完善项目。
