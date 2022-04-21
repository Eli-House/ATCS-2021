"""
A Machine Learning algorithm to predict car prices

@author: Eli Housenbold
@version: 03/03/2022
@source: CodeHS
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

''' Load Data '''
data = pd.read_csv("data/car.csv")
x_1 = data["miles"]
x_2 = data["age"]
y = data["Price"]

''' Visualize Data '''
fig, graph = plt.subplots(2)
graph[0].scatter(x_1, y)
graph[0].set_xlabel("Total Miles")
graph[0].set_ylabel("Price")

graph[1].scatter(x_2, y)
graph[1].set_xlabel("Car Age")
graph[1].set_ylabel("Price")

print("Correlation between Total Miles and Car Price:", x_1.corr(y))
print("Correlation between Age and Car Price:", x_2.corr(y))

plt.tight_layout()
plt.show()

''' TODO: Create Linear Regression '''
# Reload and/or reformat the data to get the values from x and y
x = data[["miles", "age"]].values
y = data["Price"].values

# Separate data into training and test sets
x_train, x_test, y_train, y_test, = train_test_split(x, y, test_size=0.2)
model = LinearRegression().fit(x_train, y_train)

# Create multivariable linear regression model
# Find and print the coefficients, intercept, and r squared values.
# Each rounded to two decimal places.
print("Model Information:")
print("Annual Precipitation coef:", model.coef_[0])
print("Winter Severity coef:", model.coef_[1])
print("Intercept:", model.intercept_)
r_squared = model.score(x_train, y_train)
print("R squared", r_squared)
print()

# Test the model

# Print out the actual vs the predicted values
#print("prediction when x is", x_predict, prediction)
#prediction = model.predict([[x_predict]])
pone_age = 10
pone_miles = 89000
ptwo_age = 20
ptwo_miles = 150000
pone = model.predict([[pone_age, pone_miles]])
ptwo = model.predict([[ptwo_age, ptwo_miles]])

print("Prediction when car age in 10 years old and has 89000 miles:", pone)
print("prediction when car age in 20 years old and has 150000 miles:", ptwo)
print()
predict = model.predict(x_test)
print("Testing Linear Model with testing Data: ")
for index in range(len(x_test)):
    # actual y value
    actual = y_test[index]
    # predicted y value
    y_pred = round(predict[index], 2)
    # Test x value
    x_mile = x_test[index][0]
    x_age = x_test[index][1]
    print("x Miles:", x_mile, "x Age:", x_age, " Predicted y value:", y_pred, " Actual y value:", actual)