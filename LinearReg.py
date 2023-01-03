import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([7,14,15,18,19])
n = np.size(x)
x_mean = np.mean(x)
y_mean = np.mean(y)

Sxy = np.sum(x*y) - n*x_mean*y_mean
Sxx = np.sum(x*x) - n*x_mean*x_mean

b1 = Sxy/Sxx
b0 = y_mean - b1 * x_mean
print("\nSlope b1 is:- ",b1)
print("\nIntercept b0 is:- ",b0)

plt.scatter(x,y)
plt.xlabel("Independent variable X")
plt.ylabel("Dependent variable Y")

y_pred = b1 * x +b0
plt.scatter(x,y,color="red")
plt.plot(x,y_pred,color = "green")
plt.xlabel("X")
plt.ylabel("Y")

error = y - y_pred
se = np.sum(error ** 2)
print("\nSqaured Error is ",se)

mse = se/n
print("\nMean Sqaured Error is ",mse)

rmse = np.sqrt(mse)
print("\nRoot mean Sqaured Error is ",rmse)

sst = np.sum((y-y_mean) ** 2)
r2 = 1 - (se/sst)
print("\nR square",r2)
plt.show()
