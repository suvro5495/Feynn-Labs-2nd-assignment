# -*- coding: utf-8 -*-
"""2nd assignment 2nd time .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iZk-2Re5BJk0SXmJrcsgd4uSRVyLLan2
"""

# Data Loading
from google.colab import drive
import pandas as pd
drive.mount('/content/drive')
file_path = '/content/drive/My Drive/mcdonalds.csv'
df = pd.read_csv(file_path)
print(df.head())

# Data exploration
X = df.iloc[:,1:12].replace({'Yes': 1, 'No': 0})

print(X.mean())

# Using dataframe X: Clean the dataset by finding and locating for all of the string entries

X['Like'] = X['Like'].str.replace('I hate it!', '-5').str.replace('-3', '3')

# Using dataframe X: Data exploration with PCA by dropping out the string entries

import numpy as np
from sklearn.decomposition import PCA

# Create a PCA object
pca = PCA()

# Drop the string entries from the dataframe
X = X.drop(['Like'], axis=1)

# Fit the PCA object to the data
pca.fit(X)

# Print the principal components
print(pca.components_)

# Using dataframe X: Plot the previously computed principal components

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(X)
X_pca = pca.transform(X)
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.show()

# Using dataframe X: K-means clustering on this dataset

from sklearn.cluster import KMeans
km = KMeans(n_clusters=3)
km.fit(X)

# Using dataframe X: Plot the previously computed clusters

X.plot.scatter(x='spicy', y='greasy')

# Applying logistic regression and decision tree on this dataset , evaluate the model and show their visualisations.

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_pca, km.labels_, test_size=0.25, random_state=42)

# Create a logistic regression model
lr = LogisticRegression()

# Fit the model to the training data
lr.fit(X_train, y_train)

# Make predictions on the test data
y_pred = lr.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print('Logistic regression accuracy:', accuracy)

# Create a decision tree model
dt = DecisionTreeClassifier()

# Fit the model to the training data
dt.fit(X_train, y_train)

# Make predictions on the test data
y_pred = dt.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print('Decision tree accuracy:', accuracy)

# Visualize the decision tree
import pydotplus
from sklearn.tree import export_graphviz
dot_data = export_graphviz(dt, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png('decision_tree.png')

# Plot the previously done decision tree model evaluation and logistic regression model evaluation

plt.plot([0.25, 0.5, 0.75, 1], [accuracy, accuracy, accuracy, accuracy])
plt.xlabel('Test set size')
plt.ylabel('Accuracy')
plt.title('Model evaluation')
plt.show()

# Using dataframe X: Assess the previously performed K-means clustering stability using bootstrapping on this dataset
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.model_selection import KFold
from sklearn.cluster import KMeans

# Split the data into training and test sets
X_train, X_test = train_test_split(X, test_size=0.25)

# Perform K-means clustering on the training set
kmeans = KMeans(n_clusters=5)
kmeans.fit(X_train)

# Calculate the cluster assignments for the test set
y_pred = kmeans.predict(X_test)

# Calculate the accuracy of the clustering
accuracy = np.mean

# Split the data into training and test sets
X_train, X_test = train_test_split(X, test_size=0.25)

# Perform K-means clustering on the training set
kmeans = KMeans(n_clusters=5)
kmeans.fit(X_train)

# Calculate the cluster assignments for the test set
y_pred = kmeans.predict(X_test)

# Calculate the accuracy of the clustering
accuracy = np.mean(y_pred == kmeans.labels_[kmeans.predict(X_test)])

print(f"Accuracy: {accuracy}")

# Using dataframe X: Clean and transform the response data to numeric values . Also Extract feature variables related to food qualities

X.replace('yes', 1, inplace=True)
X.replace('no', 0, inplace=True)
X.drop('tasty', axis=1, inplace=True)

# Using dataframe X: Gaussian mixture model applying on this dataset

from sklearn.mixture import GaussianMixture
gmm = GaussianMixture(n_components=2).fit(X)

# Using dataframe X: Plot the gaussian mixture model previous computed results

from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

# Load the data
data = X

# Reduce the dimensionality of the data using PCA
pca = PCA(n_components=2)
data = pca.fit_transform(data)

# Create a Gaussian mixture model
gmm = GaussianMixture(n_components=3)

# Fit the model to the data
gmm.fit(data)

# Plot the results
plt.scatter(data[:, 0], data[:, 1], c=gmm.predict(data))

# Using dataframe X: Compare the solutions between K-means and Gaussian mixture model from the above results on this dataset

from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import pandas as pd

# Create a KMeans model with 3 clusters
kmeans = KMeans(n_clusters=3)

# Fit the model to the data
kmeans.fit(X)

# Create a Gaussian Mixture Model with 3 clusters
gmm = GaussianMixture(n_components=3)

# Fit the model to the data
gmm.fit(X)

# Get the cluster labels for each data point
kmeans_labels = kmeans.labels_
gmm_labels = gmm.predict

print(X.shape)

print(len(kmeans_labels))

from sklearn.mixture import GaussianMixture

print(gmm)

print("gmm_labels" in dir(gmm))

print(len(gmm.predict(X)))

import matplotlib.pyplot as plt

print(type(gmm_labels))

from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

# Assign the labels to gmm_labels variable
gmm_labels = GaussianMixture(n_components=4).fit(X)

# Plot the data points with the corresponding labels
plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels[:4].reshape(-1))
plt.scatter(X[:, 0], X[:, 1], c=gmm_labels.predict(X)[:4].reshape(-1))
plt.show()