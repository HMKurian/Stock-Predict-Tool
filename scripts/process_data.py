import json
import pandas as pd
import os

def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def process_data(data):
    all_dfs = []
    for symbol, stock_data in data.items():
        df = pd.DataFrame(stock_data['values'])
        df['symbol'] = symbol
        all_dfs.append(df)

    # Concatenate all dataframes
    df = pd.concat(all_dfs, ignore_index=True)

    # Convert to appropriate data types
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['open'] = pd.to_numeric(df['open'])
    df['high'] = pd.to_numeric(df['high'])
    df['low'] = pd.to_numeric(df['low'])
    df['close'] = pd.to_numeric(df['close'])
    df['volume'] = pd.to_numeric(df['volume'])

    # Sort by date and symbol
    df.sort_values(by=['symbol', 'datetime'], inplace=True)

    return df

def save_data(df, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Data processed and saved to {filename}")

if __name__ == '__main__':
    raw_data_path = '../data/historical_stock_data.json'
    processed_data_path = '../data/processed_historical_stock_data.csv'

    # Load and process data
    raw_data = load_data(raw_data_path)
    processed_data = process_data(raw_data)

    # Save processed data
    save_data(processed_data, processed_data_path)
