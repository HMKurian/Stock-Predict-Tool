import requests
import json
import os

def fetch_stock_data(symbol, interval='1day', outputsize='500'):
    url = "https://twelve-data1.p.rapidapi.com/time_series"
    querystring = {"symbol": symbol, "interval": interval, "outputsize": outputsize, "format": "json"}
    headers = {
        "x-rapidapi-key": "703e75cec2msh678d6c73540a186p1fb32ejsn50e85eb2608f",
        "x-rapidapi-host": "twelve-data1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {symbol}: {response.status_code}")
        return None

def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f"Data saved to {filename}")

if __name__ == '__main__':
    symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]  # List of stock symbols
    all_data = {}

    for symbol in symbols:
        stock_data = fetch_stock_data(symbol)
        if stock_data:
            all_data[symbol] = stock_data
    
    os.makedirs('../data', exist_ok=True)
    save_data(all_data, '../data/historical_stock_data.json')
