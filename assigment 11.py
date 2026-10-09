import pandas as pd
import numpy as np

np.random.seed(42)
numbers = np.random.randint(1, 101, 10)
series = pd.Series(numbers)

print("Original Series:")
print(series)

print("Element at Index 3:", series.iloc[3])
print("Elements from Index 2 to 6:")
print(series.iloc[2:7])

print("Numbers Greater Than 50:")
print(series[series > 50])

print("Mean:", series.mean())
print("Median:", series.median())
print("Minimum:", series.min())
print("Maximum:", series.max())