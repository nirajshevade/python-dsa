import pandas as pd

data = {
    "Name": ["Amit", "Rahul", "Neha"],
    "Age": [21, 22, 20]
}

df = pd.DataFrame(data)

print(df)
print()

print(df[df["Age"] > 20])
print()
print(df.duplicated())