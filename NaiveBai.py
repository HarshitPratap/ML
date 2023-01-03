import pandas as pd 
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

data= pd.read_csv('./dataset.csv')

print("The first 5 values of data is :\n",data.head())
X = data.iloc[:,:-1]

print("\nThe First 5 values of train data is\n",X.head()) 
y = data.iloc[:,-1]

print("\nThe first 5 values of Train output is\n",y.head())

le_outlook = LabelEncoder()
X.outlook = le_outlook.fit_transform(X.outlook) 

le_temp = LabelEncoder()
X.temp = le_temp.fit_transform(X.temp)

le_humidity = LabelEncoder()
X.humidity = le_humidity.fit_transform(X.humidity)
                  
le_windy = LabelEncoder()
X.windy = le_windy.fit_transform(X.windy)
print("\nNow the Train data is :\n",X.head())

le_PlayTennis = LabelEncoder()
y= le_PlayTennis.fit_transform(y)
print("\nNow the Train output is\n",y)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20) 
classifier=GaussianNB()
classifier.fit(X_train,y_train)
from sklearn.metrics import accuracy_score
print("Accuracy is:- ",accuracy_score(classifier.predict(X_test),y_test))
