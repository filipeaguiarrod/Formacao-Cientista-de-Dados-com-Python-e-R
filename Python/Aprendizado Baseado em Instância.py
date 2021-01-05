# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:27:13 2020

@author: rodri
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from scipy import stats

iris = datasets.load_iris()

stats.describe(iris.data)

previsores = iris.data
classe = iris.target

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,classe,test_size = 0.3,random_state=0)

knn = KNeighborsClassifier(n_neighbors = 3 )
knn.fit(X_treinamento, y_treinamento)

# não cria um modelo, armazena e cria um registro quando
# quero prever ele calcula distância e gera uma previsão

previsões = knn.predict(X_teste)

matriz_confusão = confusion_matrix(y_teste,previsões)

taxa_acerto = accuracy_score(y_teste, previsões)
taxa_erro = 1- taxa_acerto
