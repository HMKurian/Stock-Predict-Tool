import pandas as pd
import os

def load_data(filename):
    return pd.read_csv(filename)

def create_features(df):
    # Example feature engineering: Calculate moving averages
    df['ma_5'] = df.groupby('symbol')['close'].transform(lambda x: x.rolling(window=5).mean())
    df['ma_10'] = df.groupby('symbol')['close'].transform(lambda x: x.rolling(window=10).mean())
    df['ma_20'] = df.groupby('symbol')['close'].transform(lambda x: x.rolling(window=20).mean())

    return df

def save_data(df, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Features engineered and saved to {filename}")

if __name__ == '__main__':
    processed_data_path = '../data/processed_historical_stock_data.csv'
    features_data_path = '../data/features_historical_stock_data.csv'

    # Load and create features
    data = load_data(processed_data_path)
    data_with_features = create_features(data)

    # Save data with features
    save_data(data_with_features, features_data_path)
