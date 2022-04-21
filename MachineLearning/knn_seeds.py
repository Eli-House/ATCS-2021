import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score

data = pd.read_csv("data/seeds.csv")

feature_area = data["area"].values
feature_perimeter = data["perimeter"].values
feature_compactness = data["compactness"].values
feature_kernel_length = data["kernel_length"].values
feature_kernel_width = data["kernel_width"].values
feature_asymmetry_coef = data["asymmetry_coef"].values
feature_groove_length = data["groove_length"].values
classes = data["seed"].values
kVal = []
ac = []

features = np.array([feature_area, feature_perimeter, feature_compactness, feature_kernel_length, feature_kernel_width,feature_asymmetry_coef, feature_groove_length]).transpose()


scaler = StandardScaler().fit(features)
features = scaler.transform(features)
class_labels = np.unique(data["seed"])
features_train, features_test, classes_train, classes_test = train_test_split(features, classes, test_size=0.2)

for i in range (2, 42):
    model = KNeighborsClassifier(n_neighbors=i).fit(features_train, classes_train)
    classes_pred = model.predict(features_test)
    accuracy = accuracy_score(classes_test, classes_pred)
    print("Accuracy:", accuracy )
    ac.append(accuracy)
    kVal.append(i)

#cm = confusion_matrix(classes_test, classes_pred, labels=class_labels)
#cmd = ConfusionMatrixDisplay(cm, display_labels=class_labels)
#cmd.plot()
plt.scatter(kVal,ac)
plt.show()