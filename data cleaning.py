pip install pandas
pip install numpy

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Create DataFrame
df = pd.DataFrame({
    'Date': ['2023-01-01', '02-01-2023', 'Invalid'],
    'Category': ['Apple', 'apple', 'Banana'],
    'Value': [10, 1500, 20],
    'Missing': [1, np.nan, 3]
})

print("Original Data:\n", df)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing values with mean
df['Missing'] = df['Missing'].fillna(df['Missing'].mean())

# Convert 'Date' column to datetime, coerce errors to NaT
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Forward fill missing dates
df['Date'] = df['Date'].ffill()

# Standardize 'Category' text to lowercase
df['Category'] = df['Category'].str.lower()

# Clip 'Value' column to a maximum of 100
df['Value'] = df['Value'].clip(upper=100)

# Normalize 'Value' column using MinMaxScaler
scaler = MinMaxScaler()
df['Value_norm'] = scaler.fit_transform(df[['Value']])

print("\nCleaned Data:\n", df)
