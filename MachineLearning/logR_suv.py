''' Creates a logistic regression model to determine if someone will buy and SUV'''
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

''' Load Data '''
data = pd.read_csv("data/suv.csv")

# replace qualitative data with binary(quantitative)
data["Gender"].replace(["Male", "Female"], [0,1 ], inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values
#stndardize

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

# Split into train and test data
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

model = LogisticRegression().fit(x_train, y_train)

# get weights for logistic regression equation
coef = model.coef_[0]
print("Weights for model:")
print(coef)
print()

''' Test Model '''
y_pred = model.predict(x_test)

#Get confusion matrix
print("Confusion Matrix")
print(confusion_matrix(y_test, y_pred))

accuracy = model.score(x_test, y_test)
print("Accuracy:", accuracy)

''' make a new prediction '''

age = int(input("How old is the customer?\n"))
gender = int(input("is the customer Male (0) or Female (1)\n"))
salary = int(input("How uch does the customer make in a year?\n"))

#3Scale the inputs
x_pred = [[age, salary, gender]]
x_pred = scaler.transform(x_pred)

# Make and print the prediction
if model.predict(x_pred)[0] == 1:
    print("This customer will likely buy and SUV")
else:
    print("This customer will likely not buy and SUV")