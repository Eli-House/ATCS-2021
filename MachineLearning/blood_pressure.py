"""
@author: Eli Housenbold
@version: 03/1/2022
@source: CodeHS
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
''' Load Data '''
data = pd.read_csv("data/blood_pressure.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

''' TODO: Create Linear Regression '''
#seperate the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

# Get the values from x and y

# Use reshape to turn the x values into 2D arrays:
x_train = x_train.reshape(-1,1)
# Create the model
model = LinearRegression().fit(x_train, y_train)
r_squared = model.score(x_train, y_train)
# Find the slope and intercept
# Each should be a float and rounded to two decimal places.
slope = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)

x_test = x_test.reshape(-1,1)

# Print out the linear equation
print("Model Equation: y =", slope, "x +", intercept)
print("R squared", r_squared)

# Predict the the blood pressure of someone who is 43 years old.
#x_predict = 43
#prediction = model.predict([[x_predict]])
predict = model.predict(x_test)

#compare the actual and predicted values
print("Testing Linear Model with testing Data: ")
for index in range(len(x_test)):
    actual = y_test[index]
    y_pred = round(predict[index], 2)
    x_val = float(x_test[index])
    print("x value:", x_val, " Predicted y value:", y_pred, " Actual y value:", actual)

# Print out the prediction
#print("prediction when x is", x_predict, prediction)
''' Visualize Data '''
# set the size of the graph
plt.figure(figsize=(5, 4))

# label axes and create a scatterplot
plt.xlabel("Age")
plt.ylabel("Systolic Blood Pressure")
plt.title("Systolic Blood Pressure by Age")
plt.scatter(x_train, y_train, c="purple", label="Training Data")
plt.scatter(x_test, y_test,  c="blue", label="Testing Data")
plt.scatter(x_test, predict, c="orange", label="Predictions")
plt.plot(x_train, slope * x_train + intercept, c="red", label="Line of Best Fit")
plt.legend()
plt.show()

print("Pearson's Correlation: r = :", x.corr(y))
