import math
def mean(data):
    n = len(data)
    sum = 0
    for X in data:
        sum+=X
    return sum/(n)

def deviation(data):
    dmean = mean(data)
    print("Mean is:- "+str(dmean))
    mdev = 0
    for x in data:
        print("Deviation of {} is {}".format(x,str(dmean - x)))
        print("Absolute Deviation of {} is {}".format(x,abs(dmean - x)))
        mdev += abs(dmean - x)
    print("Average deviation is:- "+str(mdev/len(data)))

def variation(data):
    dmean = mean(data)
    variation = 0
    for x in data:
        variation+=((dmean - x) ** 2)
    print("Variation is:- "+str(variation))

def variance(data):
    dmean = mean(data)
    n = len(data)
    var = 0
    for x in data:
        var += ((x - dmean) ** 2)
    print("Population variance of data:- "+str(var/n))
    print("Sample variance of data:- "+str(var/(n-1)))
    print("Standard deviation is:- "+str(math.sqrt((var/n))))
data = [2,9,8,4,3,12,45,3]
deviation(data)
variation(data)
variance(data)
