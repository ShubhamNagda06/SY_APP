import numpy as np

arr = np.arange(1, 11)

print("Original Array:", arr)
print("First Five Elements:", arr[:5])
print("Elements from Index 3 to 7:", arr[3:8])
print("Every Second Element:", arr[::2])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

arr = arr + 5
print("Array After Broadcasting (+5):", arr)