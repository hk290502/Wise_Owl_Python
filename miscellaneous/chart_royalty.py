import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

connect = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT", "5432")
)

cur = connect.cursor()

query = query = """
SELECT
    track_name,
    single_release_date,
    us_billboard_hot_100_peak
FROM track
WHERE us_billboard_hot_100_peak IS NOT NULL
ORDER BY us_billboard_hot_100_peak ASC
LIMIT 10;
"""


cur.execute(query)
tracks = cur.fetchall()

medals = {
    1: "🥇",
    2: "🥈",
    3: "🥉"
}

print("\n🔥 CHART ROYALTY 🔥")
print("Top 10 Billboard Singles of All Time\n")

for rank, (name, date, peak) in enumerate(tracks, start=1):
    medal = medals.get(rank, "🎶")
    year = date.year if date else "Unknown year"

    print(f"{rank:>2}. {medal} {name} ({year}) — Peak #{peak}")

# Clean up
cur.close()
connect.close()
