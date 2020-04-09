
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

import operator

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
import joblib

# load training-data file
training_data = pd.read_csv('training-data.csv')

# retrieve x data from training data; this is converted from Pandas.DataFrame
#to numpy
n_rows, n_columns = training_data.shape

X_train = pd.DataFrame.to_numpy(training_data.iloc[:,0:n_columns-1])

# retrieve y data from training data; this is converted from Pandas.DataFrame
# to numpy

Y_train = pd.DataFrame.to_numpy(training_data.iloc[:,-1]).reshape(n_rows, 1)

def create_polynomial_regression_model(degree):
    "Creates a polynomial regression model for the given degree"

    poly_features = PolynomialFeatures(degree=degree)

    # transforms the existing features to higher degree features.
    X_train_poly = poly_features.fit_transform(X_train)

    # fit the transformed features to Linear Regression
    poly_model = LinearRegression()
    poly_model.fit(X_train_poly, Y_train)

    # predicting on training data-set
    y_train_predicted = poly_model.predict(X_train_poly)

    # evaluating the model on training dataset
    rmse_train = np.sqrt(mean_squared_error(Y_train, y_train_predicted))
    r2_train = r2_score(Y_train, y_train_predicted)
    print("The model performance for the training set")
    print("-------------------------------------------")
    print("RMSE of training set is {}".format(rmse_train))
    print("R2 score of training set is {}".format(r2_train))
    print("\n")

    joblib.dump(poly_model, 'model.pkl')

    plt.scatter(X_train, Y_train, s=10)
    plt.plot(X_train, y_train_predicted, color='g')
    plt.grid()
    plt.show()


create_polynomial_regression_model(7)

