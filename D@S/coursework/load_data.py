import sqlite3
import pandas as pd

# Create SQLite DB
conn = sqlite3.connect("datas74.db")

# URLs for the tables (same data as Databricks)
base = "https://docs.google.com/uc?export=download&id="

files = {
    "customers": "1jz9XGdYlZ5nQ4V4W8Z0m5cQnYw7n1G5R",
    "products": "1x1xkY0Y9LkqP6VbK0mH5rZ1XQ3PZpE7J",
    "stores": "1ZJQk3ZJp7Bqz1Kp8H2pHjM2WZ5kZ7ZxP",
    "receipts": "1nJ7Yw0JqPZ7M3m0b1Nw8C1Y9GJ0bX1P8",
    "receipt_lines": "1P7kQmY8YJ2K9W9P1X7Y8kM9X2k0PZ8nY",
}

for table, file_id in files.items():
    df = pd.read_csv(base + file_id)
    df.to_sql(table, conn, index=False, if_exists="replace")
    print(f"Loaded {table}")

conn.close()
print("datas74.db created successfully")
