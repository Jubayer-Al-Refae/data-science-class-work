#Assignment for data science
import pandas as pd

# Task 1

dt = pd.read_csv("dataset for data science project\IRIS.csv")

# Displaying First 5 rows
print("First 5 Rows: ")
print(dt.head())

# column names
print("\nColumns Names", end=" ")
print(dt.columns)

# Number of Rows and Columns
shp = dt.shape
print("Row      :", shp[0])
print("Columns  :", shp[1])

# Summary Statistics
print("\nSummary Statistics:")
print(dt.describe())


# Task 2

# New column "Average score"

dt["Average score"] = (
    dt.iloc[:, 0] + dt.iloc[:, 1] + dt.iloc[:, 2] + dt.iloc[:, 3]
) / 4

print()
print(dt.head())
print()
# Applying condition
dt["Average score condition"] = "Smaller than 2.5"

dt.loc[dt["Average score"] > 2.5, "Average score condition"] = "Bigger Than 2.5"
print()
print(dt.head())
print()

# Task 3

print(dt.sort_values("sepal_length"))