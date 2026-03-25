import pandas as pd

data = pd.read_csv("../Month 1/Day 11/sales_data.csv")

print("Full Data:")
print(data)

data.columns = data.columns.str.strip()
# Groupby category
grouped = data.groupby("category")["amount"].sum()

print("\nSales by Category:")
print(grouped)

print("\nTotal Sales:")
print(data["amount"].sum())