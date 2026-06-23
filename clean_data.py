import pandas as pd

# Read Excel file
df = pd.read_excel("sales.xlsx")

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned file
df.to_excel("clean_sales_data.xlsx", index=False)

print("Task completed")