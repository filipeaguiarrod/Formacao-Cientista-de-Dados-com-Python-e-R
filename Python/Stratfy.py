import pandas as pd
from sklearn.model_selection import train_test_split


iris=pd.read_csv('iris.csv')
iris['class'].value_counts()

X,_,Y,_=train_test_split(iris.iloc[:,0:4],iris.iloc[:,4],train_size=0.5,stratify=iris.iloc[:,4])
Y,_['class'].value_counts()

X,_,Y,_=train_test_split(iris.iloc[:,0:4],iris.iloc[:,4],train_size=0.5,stratify=iris.iloc[:,4])


infert = pd.read_csv('infert.csv')
infert['education'].value_counts()

X1,_,y1,_=train_test_split(infert.iloc[:, 2:9],infert.iloc[:, 1],train_size=0.4,stratify=infert.iloc[:, 1]) 

y1.value_counts()