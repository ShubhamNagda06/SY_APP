import pandas as pd
import numpy as np

data = {
    'Name': ['Amit', 'Priya', None, 'Rahul', 'Sneha'],
    'Age': [25, 30, np.nan, 45, 35],
    'Weight': [65, np.nan, 70, 80, 55],
    'Blood Pressure': [120, 130, np.nan, 140, 110]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Weight'] = df['Weight'].fillna(df['Weight'].mean())
df['Blood Pressure'] = df['Blood Pressure'].fillna(df['Blood Pressure'].mean())

print("\nDataFrame After Filling Missing Values:")
print(df)

df = df.dropna(subset=['Name'])

print("\nDataFrame After Dropping Rows with Missing Names:")
print(df)