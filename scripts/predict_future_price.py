import pandas as pd
import numpy as np
import pickle
import os

def load_data(filename):
    return pd.read_csv(filename)

def load_model(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def make_prediction(model, df):
    # Define features used in training the model
    features = ['ma_5', 'ma_10', 'ma_20']

    # Drop rows with NaN values
    df = df.dropna(subset=features)

    # Make a copy of df to avoid SettingWithCopyWarning
    df = df.copy()

    # Extract features for prediction
    X = df[features]

    # Make predictions
    predictions = model.predict(X)

    # Assign predictions to 'predicted_close' using .loc
    df.loc[:, 'predicted_close'] = predictions

    return df


def save_predictions(df, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Predictions saved to {filename}")

if __name__ == '__main__':
    features_data_path = '../data/features_historical_stock_data.csv'
    model_path = '../models/stock_price_model.pkl'
    predictions_path = '../data/predicted_stock_prices.csv'

    # Load data and model
    data = load_data(features_data_path)
    model = load_model(model_path)

    # Make predictions
    data_with_predictions = make_prediction(model, data)

    # Save predictions
    save_predictions(data_with_predictions, predictions_path)
