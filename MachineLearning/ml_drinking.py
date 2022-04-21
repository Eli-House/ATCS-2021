import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

''' Visualize Data  '''
data = pd.read_csv("data/drinking.csv")

x = data[["Urban_population_percentage", "Wine_consumption_per_capita", "Liquor_consumption_per_capita"]].values
y = data["Cirrhosis_death_rate"].values

x_train, x_test, y_train, y_test, = train_test_split(x, y, test_size=0.2)
model = LinearRegression().fit(x_train, y_train)
r_squared = model.score(x_train, y_train)

# print out the model information
print("Model Information:")
print("Urban Population Percentage coef:", model.coef_[0])
print("Wine Consumption per Capita coef:", model.coef_[1])
print("Liquor Consumption per Capita coef:", model.coef_[2])
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
    x_urban = x_test[index][0]
    x_wine = x_test[index][1]
    x_liquor = x_test[index][2]
    print("x Urban:", x_urban, "x Wine:", x_wine, "x Liquor:", x_liquor, " Predicted y value:", y_pred, " Actual y value:", actual)