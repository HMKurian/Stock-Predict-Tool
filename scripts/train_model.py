import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

def load_data(filename):
    return pd.read_csv(filename)

def train_model(df):
    # Define features and target
    features = ['ma_5', 'ma_10', 'ma_20']
    target = 'close'

    # Drop rows with NaN values
    df = df.dropna(subset=features)

    # Split data into features and target
    X = df[features]
    y = df[target]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate model
    score = model.score(X_test, y_test)
    print(f"Model R^2 score: {score}")

    return model

def save_model(model, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {filename}")

if __name__ == '__main__':
    features_data_path = '../data/features_historical_stock_data.csv'
    model_path = '../models/stock_price_model.pkl'

    # Load data and train model
    data = load_data(features_data_path)
    model = train_model(data)

    # Save trained model
    save_model(model, model_path)
