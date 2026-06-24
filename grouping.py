import pandas as pd

df = pd.read_excel("sales.xlsx")

result = df.groupby("Item")["Qty"].sum()

print("Total Quantity Sold Per Item:")
print(result)