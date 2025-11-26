"""
Simple example of using pandas and matplotlib with COVID-like data.
Uses a small in-memory dataset.
"""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "cases": [10, 20, 35, 30, 25],
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

plt.plot(df["day"], df["cases"], marker="o")
plt.title("COVID Cases over Days")
plt.xlabel("Day")
plt.ylabel("Number of Cases")
plt.tight_layout()
plt.show()
