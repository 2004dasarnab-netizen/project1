import pandas as pd
import numpy as np
from numpy.polynomial import Polynomial
from sklearn.metrics import r2_score

# Load your Excel file
file_path = "C:\\Users\\Arpan_PC\\Downloads\\east_kolkata_cleaned.xlsx"
xls = pd.ExcelFile(file_path)
df = xls.parse('Sheet1')

# Extract independent and dependent variables
X = df['Total_Sq.ft'].values
y = df['Flat_Price'].values

# Dictionary to store R² scores for each degree
r2_scores = {}

# Check polynomial fits from degree 1 to 10
for degree in range(1, 11):
    p = Polynomial.fit(X, y, degree)
    y_pred = p(X)
    r2 = r2_score(y, y_pred)
    r2_scores[degree] = r2

# Print R² values
print("R² scores for polynomial degrees 1 to 10:")
for degree, r2 in r2_scores.items():
    print(f"Degree {degree}: R² = {r2:.4f}")

# Suggest the smallest degree with R² ≥ 0.8
best_degrees = [deg for deg, score in r2_scores.items() if score >= 0.8]
if best_degrees:
    print(f"\n✅ Degree {best_degrees[0]} is the lowest degree with R² ≥ 0.8")
else:
    print("\n❌ No polynomial degree between 1 and 10 achieved R² ≥ 0.8")
