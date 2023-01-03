import matplotlib.pyplot as plt
import math

def mean(data):
    sum = 0
    for X in data:
        sum += X
    return (sum/len(data))

x = [1,2,3,4,5]
y = [7,14,15,18,19]
n = len(x)
x_mean = mean(x)
y_mean = mean(y)

SxySum = 0
SxxSum = 0
for i in range(0, len(x)):
    SxySum += x[i] * y[i]
    SxxSum += x[i] * x[i]
Sxy = SxySum - n * x_mean * y_mean
Sxx = SxxSum - n * x_mean * x_mean
#print("\nxmean ",Sxy)
#print("\nxmean ",Sxx)
b1 = Sxy / Sxx
b0 = y_mean - b1 * x_mean
print("\nSlope b1 is:- ",b1)
print("\nIntercept b0 is:- ",b0)

plt.scatter(x,y)
plt.xlabel("Independent variable X")
plt.ylabel("Dependent variable Y")

y_pred = [] 
for i in range(0, len(x)):
    y_pred.append(b1 * x[i] + b0)
plt.scatter(x,y,color="red")
plt.plot(x,y_pred,color = "green")
plt.xlabel("X")
plt.ylabel("Y")

error = []
for i in range(0, len(y)):
    error.append(y[i] - y_pred[i])
se = 0 
for i in range(0, len(error)):
    se += error[i] ** 2
print("\nSqaured Error is ",se)

mse = se/n
print("\nMean Sqaured Error is ",mse)

rmse = math.sqrt(mse)
print("\nRoot mean Sqaured Error is ",rmse)

sst = 0
for i in range(0, len(y)):
    sst += (y[i] - y_mean) ** 2
r2 = 1 - (se/sst)
print("\nR square",r2)
plt.show()



