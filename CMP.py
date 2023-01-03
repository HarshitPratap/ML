# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import classification_report

# actual = [1,1,0,0,0,1,0,0,1,1,0,1]
# predicted = [1,1,0,1,0,1,0,1,0,1,0,0]

# matrix = confusion_matrix(actual,predicted,labels=[1,0])
# print(matrix)

# tp,fn,fp,tn = confusion_matrix(actual,predicted,labels=[1,0]).reshape(-1)
# print("Outcome:- ",tp,fn,fp,tn)

# matrix = classification_report(actual,predicted,labels=[1,0])
# print(matrix)


a = [1,1,0,0,0,1,0,0,1,1,0,1]
p = [1,1,0,1,0,1,0,1,0,1,0,0]

tp=tn=fp=fn=0

for i in range(0,len(a)):
    if a[i] == 1 and p[i] == 1:
        tp+=1
    elif a[i] == 0 and p[i] == 0:
        tn+=1
    elif a[i] == 0 and p[i] == 1:
        fp+=1
    elif a[i] == 1 and p[i] == 0:
        fn+=1
pre = tp/(tp+fp)
rec = tp/(tp+fn)
f1 = 2 * ((pre*rec)/(pre+rec))
acc = (tp+fn)/(tp+tn+fp+fn)
print("Outcome:- ",tp,fn,fp,tn)
print("Report:- ",pre,rec,f1,acc)