import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

''' Visualize Data  '''
data = pd.read_csv("data/homicides.csv")

x = data[["Inhabitants", "Percent_with_income_below_5000", "Percent_unemployed"]].values
y = data["Murders_per_year_per_million"].values

x_train, x_test, y_train, y_test, = train_test_split(x, y, test_size=0.2)
model = LinearRegression().fit(x_train, y_train)
r_squared = model.score(x_train, y_train)

# print out the model information
print("Model Information:")
print("Inhabitants coef:", model.coef_[0])
print("Percent with income below 5000 coef:", model.coef_[1])
print("Percent unemployed coef:", model.coef_[2])
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
    x_inhabitants = x_test[index][0]
    x_income = x_test[index][1]
    x_unemployed = x_test[index][2]
    print("x inhabitants:", x_inhabitants, "x Percent with income below 5000:", x_income, "x percent unemployed:", x_unemployed, " Predicted y value:", y_pred, " Actual y value:", actual)