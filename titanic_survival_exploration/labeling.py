import numpy as np
import pandas as pd

os.getcwd()
os.chdir('D:/Dropbox/learning/udacity_ML/titanic_survival_exploration')

# Load the dataset
X = pd.read_csv('titanic_data.csv')
# Limit to categorical data
X = X.select_dtypes(include=[object])

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# TODO: create a LabelEncoder object and fit it to each feature in X.
# The label encoder only takes a single feature at a time!

le = LabelEncoder()
X2 = le.fit_transform(X.Embarked)
XX = X.apply(le.fit_transform)

# TODO: create a OneHotEncoder object, and fit it to all of X.

enc = OneHotEncoder()
XXX = enc.fit_transform(XX)

XXX.shape



#TODO: transform the categorical titanic data, and store the transformed labels in the variable `onehotlabels`
onehotlabels = XXX

XXX_array = pd.DataFrame(XXX.toarray())