import time
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
import joblib

#Loading the saved model with joblib
pipe = joblib.load('model.pkl')
start_time = time.time()
n = len(pipe.coef_[0])
exponents = np.array([*range(0, n, 1)])

x = 60
list_x = np.array([x]*n)
# apply the whole pipeline to data
print(pipe.predict([np.array(np.power(list_x,exponents))])[0][0])
print("--- %s seconds ---" % (time.time() - start_time))

