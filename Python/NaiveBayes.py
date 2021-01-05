# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 20:55:07 2020

@author: rodri
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score

################################Tratamento da Base de Dados

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


#train_test_split vai me ajudar a dividir dados treino e teste
## ???? entender o train_test_split

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,classe,test_size = 0.3,random_state=0)


#  X_treinamento - 70% variaveis  para o treinamento
#  X_teste - 30 % variais para testar o modelo
#  y_treinamento - resposta do X_treinamento classes
#  y_teste - resposta X_teste classes

################################ Gerando Modelo

naive_bayes = GaussianNB()
# fit ira efetivamente encaixar "treinar"
naive_bayes.fit(X_treinamento, y_treinamento)

### A Partir de agora todas previsões são utilizadas sem a base
# de dados

previsoes = naive_bayes.predict(X_teste)

# Ele vai pegar cada registro do X_teste (300,20) submete ao model
#treinado, faz estimativa e decide qual classe


################################ Matriz de Confusão

matriz_confusão = confusion_matrix(y_teste,previsoes)

taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1- taxa_acerto

# para que eu consiga visualizar a matriz de confusão ao invés de
# 0 e 1 good or Bad utilizar yellowbrick

from yellowbrick.classifier import ConfusionMatrix

v = ConfusionMatrix(GaussianNB())
v.fit(X_treinamento, y_treinamento)
v.score(X_teste, y_teste)
v.poof()

################################ Prevendo Novo Credito

#Devo manter todos os dados anteriores do treinamento para 
#manter modelo treinado

novocredito = pd.read_csv('NovoCredit.csv')
# Deixando novo credito no formato do numpy array dataframe - object
novocredito = novocredito.iloc[:,0:20].values

# Reescrevendo formatos do label encoder para novos dados

labelencoder = LabelEncoder()
novocredito[:,0] = labelencoder.fit_transform(novocredito[:,0])
novocredito[:,2] = labelencoder.fit_transform(novocredito[:,2])
novocredito[:,3] = labelencoder.fit_transform(novocredito[:,3])
novocredito[:,5] = labelencoder.fit_transform(novocredito[:,5])
novocredito[:,6] = labelencoder.fit_transform(novocredito[:,6])
novocredito[:,8] = labelencoder.fit_transform(novocredito[:,8])
novocredito[:,9] = labelencoder.fit_transform(novocredito[:,9])
novocredito[:,11] = labelencoder.fit_transform(novocredito[:,11])
novocredito[:,13] = labelencoder.fit_transform(novocredito[:,13])
novocredito[:,14] = labelencoder.fit_transform(novocredito[:,14])
novocredito[:,16] = labelencoder.fit_transform(novocredito[:,16])
novocredito[:,18] = labelencoder.fit_transform(novocredito[:,18])
novocredito[:,19] = labelencoder.fit_transform(novocredito[:,19])

naive_bayes.predict(novocredito)

