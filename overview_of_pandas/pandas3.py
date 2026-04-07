import pandas as pd

series = pd.read_excel(r"C:\WiseOwl\overview_of_pandas\Most popular series.xlsx")

change = series.rename(columns={
    "Title": "Series name",
    "Hours (millions)": "Million hours"
})

# Sort alphabetically by series name, then season/part descending
sorted_series = change.sort_values(
    by=["Series name", "Season/part"],
    ascending=[True, False]
)

# Print only the first 2 columns
print(sorted_series.iloc[:, :2])

print("\nHorror titles:")
for idx, row in change.iterrows():
    if "horror" in str(row["Genre"]).lower():
        print(f'{row["Series name"]} - series/part number {row["Season/part"]}')

print("\ncontaining u:")
for idx, row in change.iterrows():
    if "u" in str(row["Genre"]).lower():
        print(f'{row["Series name"]} - series/part number {row["Season/part"]}')