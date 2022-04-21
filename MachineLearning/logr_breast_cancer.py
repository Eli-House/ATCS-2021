''' Creates a logistic regression model to determine if someone will survive cancer '''
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

# read the data
data = pd.read_csv("data/breast_cancer.csv")

x = data[["Age","Nodes"]].values
y = data["Survived_5_Years"].values

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

# Split into train and test data
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)
model = LogisticRegression().fit(x_train, y_train)

# get weights for logistic regression equation
coef = model.coef_[0]
print("Weights for model:", coef)
print()
''' Test Model '''
y_pred = model.predict(x_test)

#Get confusion matrix
print("Confusion Matrix")
print(confusion_matrix(y_test, y_pred))

accuracy = model.score(x_test, y_test)
print("Accuracy:", accuracy)

''' make a new prediction '''

age = int(input("How old is the patient?\n"))
node = int(input("How many nodes?\n"))

#3Scale the inputs
x_pred = [[age, node]]
x_pred = scaler.transform(x_pred)

# Make and print the prediction
if model.predict(x_pred)[0] == 1:
    print("This patient will likely survive 5 years")
else:
    print("This patient will likely not survive 5 years")