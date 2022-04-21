import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

''' Visualize Data  '''
data = pd.read_csv("data/houses.csv")

x = data[["bathrooms", "lot_size_1000_sqft", "living_space_1000_sqft", "garages", "bedrooms", "age", "num_fire_places"]].values
y = data["selling_price"].values

x_train, x_test, y_train, y_test, = train_test_split(x, y, test_size=0.2)
model = LinearRegression().fit(x_train, y_train)
r_squared = model.score(x_train, y_train)

# print out the model information
print("Model Information:")
print("bathrooms coef:", model.coef_[0])
print("lot_size_1000_sqft coef:", model.coef_[1])
print("living_space_1000_sqft coef:", model.coef_[2])
print("garages coef:", model.coef_[3])
print("bedrooms coef:", model.coef_[4])
print("age coef:", model.coef_[5])
print("num_fire_places coef:", model.coef_[6])
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
    x_bathrooms = x_test[index][0]
    x_lot_size = x_test[index][1]
    x_living_space = x_test[index][2]
    x_garages = x_test[index][3]
    x_bedrooms = x_test[index][4]
    x_age = x_test[index][5]
    x_fire = x_test[index][6]
    print("x bathrooms:", x_bathrooms, "x lot size:", x_lot_size, "x living space:", x_living_space, "x garages:", x_garages, "x bedrooms:", x_bedrooms, "x age:", x_age, "x fire:", x_fire, " Predicted y value:", y_pred, " Actual y value:", actual)