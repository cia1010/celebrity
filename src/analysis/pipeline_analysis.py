import pandas as pd
from src.analysis.visualization import visualize_net_worth
from src.analysis.distribution import visualize_profession_distribution, visualize_country_distribution

def main():
    df = pd.read_csv('data/celebrities_cleaned.csv')
    visualize_net_worth(df)
    visualize_profession_distribution(df)
    visualize_country_distribution(df)

if __name__ == "__main__":
    main()
