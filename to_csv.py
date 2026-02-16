!pip install pandas 

import sqlite3
import pandas as pd

conn = sqlite3.connect("inventory.db")

df = pd.read_sql_query("SELECT * FROM vendor_sales_summary", conn)
df.to_csv("output.csv", index=False)

conn.close()