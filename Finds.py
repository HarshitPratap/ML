import csv
a =[]
with open("./data.csv","r") as csvfile:
    for row in csv.reader(csvfile):
        a.append(row)
    ##print("\n",a)
    print("\nTraning instances:- ",len(a)-1)
    num_attr = len(a[0])-1
    print("\nTotal attributes:-",num_attr)
    print("\nIntial Hypothesis:- ")
    hypothesis = ['0'] * num_attr
    print(hypothesis)
    for i in range(0, len(a)):
        if a[i][num_attr] == 'yes':
            for j in range(0, num_attr):
                if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                    hypothesis[j] = a[i][j]
                else:
                    hypothesis[j] = "?"
                    print(hypothesis)
    print("\nThe hypothesis of the training instance {} is: \n".format(i),hypothesis)
    print("\nThe specifi hypothesis for the training instance is: ")
    print(hypothesis)
