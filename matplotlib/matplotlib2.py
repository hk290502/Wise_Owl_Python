
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def get_building_data() -> tuple:

  # read Excel worksheet into dataframe (defaults to sheet 1)
  buildings_table = pd.read_excel(r"C:\WiseOwl\matplotlib\Tallest Buildings.xlsx")

  # FIRST GET THE NUMBER OF BUILDINGS PER COUNTRY

  # group by country and count buildings
  country_counts = buildings_table["Country"].value_counts()

  # turn first (index) column into a normal column
  country_counts = country_counts.reset_index()

  # change the column names
  country_counts.columns = ["Country", "Number of buildings"]

  # NOW GET THE AVERAGE HEIGHT OF BUILDINGS BY YEAR

  # now get the average height of buildings by year
  average_heights = buildings_table.groupby("Opened")["Height m"].mean().reset_index()
  average_heights.columns = ["Year opened", "Average height in metres"]

  return (country_counts,average_heights)

# get and show the two dataframes
buildings_by_country, buildings_by_year = get_building_data()

print(buildings_by_country)
print(buildings_by_year)


# Use the two dataframes you already created
buildings_by_country, buildings_by_year = get_building_data()

# --- OPTIONAL: keep the pie readable (Top 10 + Other) ---
top_n = 10
country_plot = buildings_by_country.copy()

if len(country_plot) > top_n:
    top = country_plot.iloc[:top_n].copy()
    other_total = country_plot.iloc[top_n:]["Number of buildings"].sum()
    top.loc[len(top)] = ["Other", other_total]
    country_plot = top

# --- Create 2 side-by-side charts ---
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(12, 4),
    gridspec_kw={"width_ratios": [1, 1]}
)

# Background colours (to match your screenshot vibe)
fig.patch.set_facecolor("#f6b3c1")      # pink outer background
ax1.set_facecolor("#fde7ee")           # light pink panel
ax2.set_facecolor("#fde7ee")

# -------------------------
# LEFT: Average height by year (bar chart)
# -------------------------
x = buildings_by_year["Year opened"]
y = buildings_by_year["Average height in metres"]

ax1.bar(x, y, color="#1f77b4", width=0.8)
ax1.set_title("Average height by year", fontsize=10)
ax1.set_xlabel("Year")
ax1.set_ylabel("Average height")

# optional: make it a bit cleaner
ax1.tick_params(axis="x", labelrotation=0)

# -------------------------
# RIGHT: Breakdown by country (pie chart)
# -------------------------
labels = country_plot["Country"]
sizes = country_plot["Number of buildings"]

wedges, texts = ax2.pie(
    sizes,
    startangle=90,
    wedgeprops={"edgecolor": "white"}
)
ax2.set_title("Breakdown by country", fontsize=10)

# Legend under the pie (like your example)
ax2.legend(
    wedges, labels,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.15),
    ncol=3,
    fontsize=7,
    frameon=True
)

# Final layout tweaks
plt.tight_layout()
plt.show()
