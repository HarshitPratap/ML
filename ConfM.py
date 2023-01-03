actual = [1,1,0,0,0,1,0,0,1,1,0,1]
predicted = [1,1,0,1,0,1,0,1,0,1,0,0]
TP=TN=FP=FN=0
for i in  range(0,len(actual)):
    if actual[i] == 1 and predicted[i] == 1:
        TP+=1
    elif actual[i] == 0 and predicted[i] == 0:
        TN+=1
    elif actual[i] == 0 and predicted[i] == 1: 
        FP+=1
    elif actual[i] == 1 and predicted[i] == 0:  
        FN+=1
precision = TP/(TP + FP)
recall = TP / (TP+FN)
f1 = 2* ((precision*recall)/(precision + recall))
accu = (TP + FN)/(TP + TN + FP + FN)

print("Tp:- ",TP) 
print("Tn:- ",TN)
print("Fp:- ",FP) 
print("Fn:- ",FN)
print("Precision:- ",precision) 
print("Recall:- ",recall)
print("F1 Score:- ",f1) 
print("Accuracy:- ",accu)