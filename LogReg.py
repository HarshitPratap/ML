import numpy as np
from sklearn import linear_model

x = np.array([3.78,2.44,2.09,0.14,1.72,1.67,4.92,4.37,4.96,4.52,3.69,5.88,2.98,3.33]).reshape(-1,1)
y = np.array([0,0,0,0,0,0,1,1,1,1,1,1,0,0])
logr = linear_model.LogisticRegression()
logr.fit(x,y)
predicted = logr.predict(np.array([3.46]).reshape(-1,1))

print(predicted)

def logit2prob(logr,x):
    log_odds = logr.coef_*x+logr.intercept_
    odds = np.exp(log_odds)
    probability = odds/(1+odds)
    return probability

print(logit2prob(logr,x))