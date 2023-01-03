import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([7,14,15,18,19])
n = np.size(x)

xm = np.mean(x)
ym = np.mean(y)

Sxy = np.sum(x*y) - n * xm * ym
Sxx = np.sum(x*x) - n * xm * xm

b1 = Sxy/Sxx
b0 = ym - b1 * xm
print("Slope:- ",b1)
print("InterCept:- ",b0)
yp = b0 + b1 * x

plt.scatter(x,y,color="red")
plt.plot(x,yp,color="yellow")
plt.xlabel("X")
plt.ylabel("Y")

err = y - yp

se = np.sum(err ** 2)
print("Se:- ",se)

mse = se/n
print("mse:- ",mse)

rmse = np.sqrt(mse)
print("rmse:- ",rmse)

sst = np.sum((y-ym) ** 2)
r2 = 1 - (se/sst)
print("r2:- ",r2)
plt.show()

