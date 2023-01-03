import math
low_lim=[0,10,20,30,40,50]   # lower limit
up_lim=[10,20,30,40,50,60]   # upper limit
freq=[27,10,7,5,4,2]         # m_ean=stat.mean(lower_values)
n=len(low_lim)               # length of the data
freq_sum=0
for i in range(0,n):
    freq_sum=freq_sum+freq[i] 
xifi = 0
xifi2 = 0
for i in range(0,len(low_lim)):
    xi = (up_lim[i] + low_lim[i])/2
    xifi += (freq[i] * xi)
    xifi2 += (freq[i] * xi * xi)
xmean = xifi / freq_sum
ss = xifi2 - ((xifi ** 2)/freq_sum)
var = ss/(freq_sum-1)
sd = math.sqrt(var)
print("Variance of above data is:- ",var)
print("Standard Deviation of above data is:- ",sd)