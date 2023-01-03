import matplotlib.pyplot as plt
import math
def mean(data):
    sum = 0
    for X in data:
        sum += X
    return sum/len(data)

x = [1,2,3,4,5]
y = [7,14,15,18,19]
n = len(x)
xm = mean(x)
ym = mean(y)

Sxy = 0
Sxx = 0
for i in range(len(x)):
    Sxy += (x[i] * y[i])
    Sxx +=(x[i] * x[i])
Sxy = Sxy - n * xm * ym
Sxx = Sxx - n * xm * xm

b1 = Sxy / Sxx
b0 = ym - b1 * xm
print("\nSlope b1 is:- ",b1)
print("\nIntercept b0 is:- ",b0)

yp = []
for i in range(len(x)):
    yp.append(b0 + (b1 * x[i]))
plt.scatter(x,y,color="black")
plt.plot(x,yp,color="green")
plt.xlabel("X")
plt.ylabel("Y")

err = []
for i in range(len(y)):
    err.append(y[i] - yp[i])
se = 0
for i in range(len(err)):
    se += (err[i] ** 2)
print("\nSqaured Error is ",se)
mse = se/n
print("\nMean Sqaured Error is ",mse)
rmse= math.sqrt(mse)
print("\nRoot mean Sqaured Error is ",rmse)
sst = 0
for i in range(len(y)):
    sst += (y[i] - ym) ** 2
r2 = 1 - (se/sst)
print("\nR square",r2)
plt.show()
