# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:39:01 2020

@author: rodri
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier 

credito = pd.read_csv('Credit.csv')
previsores = credito.iloc[:,0:20].values # intervalo de 0 até 19 / 20 não entra
classe = credito.iloc[:,20].values # Pegando coluna 20

# GaussianNB não trabalha com dados categóricos(qualitativos)
# Converteremos as classificações em valores c/ LabelEncoder
# Cada coluna separadamente eu aplito o fit. "Label"

labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])
previsores[:,5] = labelencoder.fit_transform(previsores[:,5])
previsores[:,6] = labelencoder.fit_transform(previsores[:,6])
previsores[:,8] = labelencoder.fit_transform(previsores[:,8])
previsores[:,9] = labelencoder.fit_transform(previsores[:,9])
previsores[:,11] = labelencoder.fit_transform(previsores[:,11])
previsores[:,13] = labelencoder.fit_transform(previsores[:,13])
previsores[:,14] = labelencoder.fit_transform(previsores[:,14])
previsores[:,16] = labelencoder.fit_transform(previsores[:,16])
previsores[:,18] = labelencoder.fit_transform(previsores[:,18])
previsores[:,19] = labelencoder.fit_transform(previsores[:,19])

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,classe,test_size = 0.3,random_state=0)

################################ Ensamble Learning

floresta = RandomForestClassifier(n_estimators=100)
# Ele fara 100 arvores de decisão diferentes
floresta.fit(X_treinamento, y_treinamento)

previsoes = floresta.predict(X_teste)

################################ Matriz de Confusão

matriz_confusão = confusion_matrix(previsoes,y_teste)

taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1- taxa_acerto

############################## Posso visualizar as árvores criadas


floresta.estimators_
# foram geradas 100 árvores 

#Caso eu queira visualizar árvores especifica:

floresta.estimators_[88]