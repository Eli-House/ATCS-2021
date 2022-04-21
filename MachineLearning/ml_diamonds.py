import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

# read the data
data = pd.read_csv("data/diamonds.csv")

x = data[["carat","depth","table"]].values

# replace qualitative data with binary(quantitative)
data["cut"].replace(["Fair", "Premium"], [0,1], inplace=True)

y = data["cut"].values



scaler = StandardScaler().fit(x)
x = scaler.transform(x)

# Split into train and test data
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)
model = LogisticRegression().fit(x_train, y_train)

# get weights for logistic regression equation
coef = model.coef_[0]
print("Weights for model:", coef)

''' Test Model '''
y_pred = model.predict(x_test)

#Get confusion matrix
print("Confusion Matrix")
print(confusion_matrix(y_test, y_pred))

accuracy = model.score(x_test, y_test)
print("Accuracy:", accuracy)

''' make a new prediction '''
carat = float(input("How big is the size of the carat?\n"))
depth = float(input("How deep is your diamond?\n"))
table = float(input("How large is your table?\n"))

#Scale the inputs
x_pred = [[carat,depth,table]]
x_pred = scaler.transform(x_pred)

# Make and print the prediction
if model.predict(x_pred)[0] == 1:
    print("This diamond is a premium cut")
else:
    print("This diamond is a fair cut")

