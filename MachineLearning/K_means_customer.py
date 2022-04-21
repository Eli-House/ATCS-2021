'''

'''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

''' Load Data '''
data = pd.read_csv("data/customer.csv")
x = data[["Annual Income", "Spending Score"]]

# Standardize the data
scaler = StandardScaler().fit(x)
x = scaler.transform(x)

''' Determine the value for X '''
# Calculate the inertia k = 1 to 10
inertias = []
for k in range(1,11):
    # Build and fit the model
    kmeanModel = KMeans(n_clusters=k).fit(x)
    # Store the inertias
    inertias.append(kmeanModel.inertia_)

# Plot the inertias to fid the Elbow
#plt.plot(range(1,11), inertias, "bx-")
##plt.xlabel("Values of K")
#plt.ylabel("Inertias")
#plt.title("The Elbow Methid using Inertia")
#plt.show()

''' Create the Model'''
# From the elbow method
k = 5
km = KMeans(n_clusters=k).fit(x)

# Get the centroid and label values
centroids = km.cluster_centers_
labels = km.labels_
print(centroids)
print(labels)

''' Visualize the clusters '''
# set the size of the graph
plt.figure(figsize=(5,4))

# Plot the Data points for each of the k Clusters
for i in range(k):
    # Get all Points x[n]
    cluster = x[labels == i]
    # Get the income and spending values for each point in the cluster
    cluster_income = cluster[:, 0]
    cluster_spending = cluster[:, 1]
    plt.scatter(cluster_income, cluster_spending)

#3 plot the centroids

centroid_income = centroids[:,0]
centroids_spending = centroids[:, 1]
plt.scatter(centroid_income, centroids_spending, marker="X", c="r")

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()
