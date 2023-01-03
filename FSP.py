import csv
a = []
with open("./data.csv","r") as cfile:
    for r in csv.reader(cfile):
        a.append(r)
    num_attr = len(a[0])-1
    h = ['0'] * num_attr
    for i in range(0,len(a)):
        if a[i][-1] == "yes":
            for j in range(0,num_attr):
                if h[j] == '0' or h[j] == a[i][j]:
                    h[j] = a[i][j]
                else:
                    h[j] = '?'
    print(h)