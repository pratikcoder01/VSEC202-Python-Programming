"""
Simple bar chart example with car data.
"""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "car": ["Car A", "Car B", "Car C"],
    "mileage": [15, 18, 20],
}

df = pd.DataFrame(data)
print(df)

plt.bar(df["car"], df["mileage"])
plt.title("Car Mileage Comparison")
plt.xlabel("Car")
plt.ylabel("Mileage (km/l)")
plt.tight_layout()
plt.show()
