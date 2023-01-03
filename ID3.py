import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
data = pd.read_csv("./dataset.csv")
print("The first 5 value of data is\n",data.head())

x =data.iloc[:,:-1]
print("The first 5 value of train data is\n",x.head())
y=data.iloc[:,-1]
print("The first 5 value of train output is\n",y.head())
le_outlook = LabelEncoder()
x.outlook = le_outlook.fit_transform(x.outlook)
le_temp = LabelEncoder()
x.temp = le_temp.fit_transform(x.temp)
le_humidity = LabelEncoder()
x.humidity = le_humidity.fit_transform(x.humidity)
le_windy = LabelEncoder()
x.windy = le_windy.fit_transform(x.windy)
print("Now the train date is\n",x.head())
le_playtenis = LabelEncoder()
y = le_playtenis.fit_transform(y)
print("Now the train data (target vaiable) is\n",y)

X_train,X_test,ytrain,ytest = train_test_split(x,y,test_size=0.2,shuffle=False)
print("Features in training set is \n",X_train)
print("Test set is \n",X_test)
classifier = DecisionTreeClassifier(criterion='entropy')
classifier.fit(X_train,ytrain)
pred1 = classifier.predict(X_test)
print("For input \n {0},\n we obtain {1}".format((X_test),le_playtenis.inverse_transform(pred1)))
print("Accuracy score is:- ",metrics.accuracy_score(ytest,pred1))

