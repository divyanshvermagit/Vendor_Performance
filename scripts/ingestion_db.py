# ==============================
# INSTALL DEPENDENCIES (Jupyter only)
# ==============================
# Remove these if running from terminal
!pip install pandas sqlalchemy


# ==============================
# IMPORTS
# ==============================
import pandas as pd
import os
import logging
import time
from sqlalchemy import create_engine


# ==============================
# LOGGING SETUP (professional logging)
# ==============================
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/ingestion_db.log"),
        logging.StreamHandler()
    ]
)


# ==============================
# DATABASE CONNECTION
# ==============================
engine = create_engine("sqlite:///inventory.db")


# ==============================
# INGEST FUNCTION
# ==============================
def ingest_db(df, table_name):
    """Ingest dataframe into SQLite table"""

    logging.info(f"Ingesting → {table_name}")

    df.to_sql(
        table_name,
        con=engine,
        if_exists="replace",   # replace table if exists
        index=False,
        chunksize=500          # avoids SQLite variable error + faster
    )

    logging.info(f"Completed → {table_name} | rows={len(df)}")


# ==============================
# LOAD ALL CSV FILES
# ==============================
def load_raw_data():

    start_time = time.time()

    data_folder = "data"

    for file in os.listdir(data_folder):

        if file.endswith(".csv"):
            file_path = os.path.join(data_folder, file)
            table_name = file.replace(".csv", "")

            try:
                logging.info(f"Reading → {file}")

                df = pd.read_csv(
                    file_path,
                    dtype=str,       # prevents datatype conflicts
                    low_memory=False
                )

                logging.info(f"Loaded → {file} | rows={len(df)} cols={len(df.columns)}")

                ingest_db(df, table_name)

            except Exception as e:
                logging.error(f"Failed → {file} | {e}")

    total_time = (time.time() - start_time) / 60
    logging.info(f"INGESTION COMPLETE | Total time: {total_time:.2f} minutes")


# ==============================
# RUN SCRIPT
# ==============================
if __name__ == "__main__":
    load_raw_data()
