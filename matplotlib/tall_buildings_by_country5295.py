import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tall = pd.read_excel(r'C:\WiseOwl\matplotlib\Tallest Buildings.xlsx')

country_counts = tall["Country"].value_counts()
country_counts = country_counts.reset_index()
country_counts.columns = ["Country", "Number of buildings"]

country_data = country_counts.to_numpy()

fig, ax = plt.subplots()
ax.barh(country_data[:, 0], country_data[:, 1])

plt.tight_layout()
plt.show()