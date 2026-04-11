import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT", "5432")
)

query = "SELECT * FROM tour;"

df = pd.read_sql(query, conn)

df.to_csv("tour.csv", index=False)

conn.close()

print("Table exported to tour.csv")