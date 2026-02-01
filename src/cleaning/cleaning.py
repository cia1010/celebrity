import pandas as pd

def clean_celebrities(raw_list):
    df = pd.DataFrame(raw_list)
    # 去重
    df = df.drop_duplicates(subset=["name", "country"])
    # 处理缺失值
    df = df.fillna({
        "net_worth": "未知",
        "country": "未知",
        "profession": "未知"
    })
    # 类型转换示例（净资产转为数字，去除美元符号等）
    if "net_worth" in df.columns:
        df["net_worth"] = df["net_worth"].str.replace("$", "").str.replace(",", "").astype(str)
    return df

if __name__ == "__main__":
    # 示例数据
    raw = [
        {"name": "A", "net_worth": "$1,000,000", "country": "US", "profession": "Actor"},
        {"name": "A", "net_worth": "$1,000,000", "country": "US", "profession": "Actor"},
        {"name": "B", "net_worth": None, "country": None, "profession": None}
    ]
    df = clean_celebrities(raw)
    print(df)
