import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the dataset
df = pd.read_excel("C:\\Users\\Arpan_PC\\Downloads\\east kolkata modified.xlsx")

# Prepare the data
X = df[['Total_Sq.ft']].values  # Independent variable
y = df['sqrt y'].values     # Dependent variable

# Fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Get model parameters
slope = model.coef_[0]
intercept = model.intercept_

# Calculate R²
r_squared = model.score(X, y)

# Print the results
print(f"Linear Regression Equation: Flat Price = {slope:.4f} * Total Sq.ft + {intercept:.2f}")
print(f"R² (coefficient of determination): {r_squared:.4f}")
