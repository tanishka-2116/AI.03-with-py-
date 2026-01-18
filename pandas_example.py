
import pandas as pd

# create a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# access a column
print("\nNames column:")
print(df["Name"])

# basic info
print("\nAverage Marks:")
print(df["Marks"].mean())
