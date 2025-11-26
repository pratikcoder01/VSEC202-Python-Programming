"""
Example visualization using a small Iris-like dataset.
"""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "sepal_length": [5.1, 4.9, 6.3, 5.8],
    "sepal_width": [3.5, 3.0, 3.3, 2.7],
    "species": ["setosa", "setosa", "virginica", "versicolor"],
}

df = pd.DataFrame(data)
print(df)

plt.scatter(df["sepal_length"], df["sepal_width"])
plt.title("Iris Sepal Length vs Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.tight_layout()
plt.show()
