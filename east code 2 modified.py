import pandas as pd
import numpy as np
from numpy.polynomial import Polynomial
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Load the Excel file
file_path ="C:\\Users\\Arpan_PC\\Desktop\\Excel all project\\east_kolkata_modified.xlsx"
xls = pd.ExcelFile(file_path)
df = xls.parse('Sheet1')

# Extract independent (X) and dependent (y) variables
X = df['Total_Sq.ft(x)'].values
y = df['sqrt y'].values

# Fit a 2nd-degree polynomial
p = Polynomial.fit(X, y, 2)

# Get the model coefficients in standard polynomial form (in increasing order of power)
model_coefficients = p.convert().coef

# Predict using the model
y_pred = p(X)

# Calculate correlation ratio (R²)
r2 = r2_score(y, y_pred)

# Print model
print(f"Model: Flat Price = {model_coefficients[0]:.4f} + {model_coefficients[1]:.4f}*Sq.ft + {model_coefficients[2]:.8f}*Sq.ft^2")
print(f"Correlation ratio (R²): {r2:.4f}")

# Plot the data and the polynomial fit
plt.scatter(X, y, label='Data Points')
plt.plot(*p.linspace(), label='2nd Degree Fit', color='red')
plt.xlabel('Total Sq.ft')
plt.ylabel('Flat Price (Lakh)')
plt.title('2nd Degree Polynomial Fit')
plt.legend()
plt.grid(True)
plt.show()
