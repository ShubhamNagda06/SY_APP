import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Age': [25, 35, np.nan, 45, 30, 50, 28, np.nan, 40, 32],
    'MonthlyCharges': [500, 700, 600, np.nan, 800, 900, 550, 650, 750, 600],
    'Tenure': [2, 12, 6, 24, 3, 36, 5, 8, 18, 4],
    'Churn': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes']
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(df['MonthlyCharges'].mean())

df = df.drop_duplicates()

print("\nCleaned Dataset:")
print(df)

print("\nSummary Statistics:")
print(df.describe())

print("\nChurn Count:")
print(df['Churn'].value_counts())

print("\nAverage Monthly Charges by Churn:")
print(df.groupby('Churn')['MonthlyCharges'].mean())

print("\nAverage Tenure by Churn:")
print(df.groupby('Churn')['Tenure'].mean())

churn_rate = np.mean(df['Churn'] == 'Yes') * 100
print("\nCustomer Churn Rate:", churn_rate, "%")

plt.figure(figsize=(6, 4))
df['Churn'].value_counts().plot(kind='bar')
plt.title("Customer Churn Count")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
df.boxplot(column='MonthlyCharges', by='Churn')
plt.title("Monthly Charges by Churn Status")
plt.suptitle("")
plt.xlabel("Churn Status")
plt.ylabel("Monthly Charges")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
df.groupby('Churn')['Tenure'].mean().plot(kind='bar')
plt.title("Average Tenure by Churn Status")
plt.xlabel("Churn Status")
plt.ylabel("Average Tenure (Months)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()