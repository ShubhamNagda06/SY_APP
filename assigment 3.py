import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Neha', 'Rohan', 'Karan', 'Anjali'],
    'Age': [22, 24, 25, 23, 26, 28, 24, 27],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR'],
    'Salary': [30000, 35000, 40000, 32000, 38000, 45000, 36000, 200000]
}

df = pd.DataFrame(data)

print("Employee DataFrame:")
print(df)

print("\nMean Salary:", df['Salary'].mean())
print("Median Salary:", df['Salary'].median())
print("Standard Deviation:", df['Salary'].std())

Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

df_clean = df[
    (df['Salary'] >= lower_limit) &
    (df['Salary'] <= upper_limit)
]

print("\nDataFrame After Removing Outliers:")
print(df_clean)

plt.figure(figsize=(6, 4))
plt.boxplot(df_clean['Salary'])
plt.title("Employee Salary Boxplot")
plt.ylabel("Salary")
plt.show()

plt.figure(figsize=(6, 4))
plt.hist(df_clean['Salary'], bins=5, edgecolor='black')
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()