# importing libraries
import pandas as pd
import sqlite3
import os

# get the database address
os.getcwd()

# creating database connection
DB_PATH = r"E:\Data Analyst project\Vendor Performance\inventory.db"
conn = sqlite3.connect(DB_PATH)

# creating engine
from sqlalchemy import create_engine
engine = create_engine(f"sqlite:///{DB_PATH}")

# checking tables present in the database
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'",conn)
tables
