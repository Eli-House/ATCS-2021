"""
Multiple Linear Regressions
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

''' Visualize Data  '''
data = pd.read_csv("data/antelope.csv")
x_1 = data["Annual Precipitation"]
x_2 = data["Winter Severity"]
y = data["Fawn"]

fig, graph = plt.subplots(2)
graph[0].scatter(x_1, y)
graph[0].set_xlabel("Annual Precipitation")
graph[0].set_ylabel("Fawn")

graph[1].scatter(x_2, y)
graph[1].set_xlabel("Winter Severity")
graph[1].set_ylabel("Fawn")

print("Corr between Annual Precipitation and Fawn Population", x_1.corr(y))
print("Corr between Winter Severity and Fawn Population", x_2.corr(y))

plt.tight_layout()
plt.show()

''' Create Multipe Linear Regression Model'''
#Organize our data into the correct fromat
x = data[["Annual Precipitation", "Winter Severity"]].values
y = data["Fawn"].values

# Split our training and testing data
x_train, x_test, y_train, y_test, = train_test_split(x, y, test_size=0.2)
model = LinearRegression().fit(x_train, y_train)

# print out the model information
print("Model Information:")
print("Annual Precipitation coef:", model.coef_[0])
print("Winter Severity coef:", model.coef_[1])
print("Intercept:", model.intercept_)
print("R squared", r_squared)
print()

''' Compare Data'''

predict = model.predict(x_test)
print("Testing Linear Model with testing Data: ")
for index in range(len(x_test)):
    # actual y value
    actual = y_test[index]
    # predicted y value
    y_pred = round(predict[index], 2)
    # Test x value
    x_precip = x_test[index][0]
    x_winter = x_test[index][1]
    print("x Precip:", x_precip, "x Winter:", x_winter, " Predicted y value:", y_pred, " Actual y value:", actual)