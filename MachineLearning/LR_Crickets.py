import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

''' Load Data '''
data = pd.read_csv("data/chirping.csv")
# Independent
x = data["Temp"].values
# Dependent
y = data["Chirps"].values

#seperate the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

# Turn x into a 2D array
x_train = x_train.reshape(-1, 1)
print(x)

''' Creat the Model '''
model = LinearRegression().fit(x_train, y_train)
slope = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x_train, y_train)

''' Test the Model '''
#x_predict = 77
#prediction = model.predict([[x_predict]])
x_test = x_test.reshape(-1,1)

#get the predicted y values for x_test values
predict = model.predict(x_test)

#compare the actual and predicted values
print("Testing Linear Model with testing Data: ")
for index in range(len(x_test)):
    actual = y_test[index]
    y_pred = round(predict[index], 2)
    x_val = float(x_test[index])
    print("x value:", x_val, " Predicted y value:", y_pred, " Actual y value:", actual)



''' Print Results '''
print("Model Equation: y =", slope, "x +", intercept)
print("R squared", r_squared)
#print("prediction when x is", x_predict, prediction)

''' Visualization '''
# Set the size of the graph
plt.figure(figsize = (5,4))

#create the scatterplot
plt.scatter(x_train, y_train, c="purple", label="Training Data")
plt.scatter(x_test, y_test,  c="blue", label="Testing Data")
plt.scatter(x_test, predict, c="orange", label="Predictions")

plt.xlabel("Temperature")
plt.ylabel("Chirps per Minute")
plt.title("Cricket Chirps by Temperature")
plt.plot(x_train, slope * x_train + intercept, c="red", label="Line of Best Fit")
plt.show()
