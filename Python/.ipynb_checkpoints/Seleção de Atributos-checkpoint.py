# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:14:46 2020

@author: rodri
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
from sklearn.ensemble import ExtraTreesClassifier
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

################################Gerando Modelo Seleção de Atributos


svm = SVC()
svm.fit(X_treinamento, y_treinamento)
previsoes = svm.predict(X_teste)

################################ Matriz de Confusão
matriz_confusão = confusion_matrix(y_teste,previsoes)

taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1- taxa_acerto


################################ Escolhendo Melhores Atributos

forest = ExtraTreesClassifier()
forest.fit(X_treinamento, y_treinamento)

importancias = forest.feature_importances_ 
# Verificar quais são os atributos de maior relevância.

#Utilizaremos apenas os 4 primeiros atributos

X_treinamento2=X_treinamento[:,[0,1,2,3]]
X_teste2=X_teste[:,[0,1,2,3]]

svm2 = SVC()
svm2.fit(X_treinamento2, y_treinamento)
previsoes2 = svm2.predict(X_teste2)

matriz_confusão2 = confusion_matrix(y_teste,previsoes2)

taxa_acerto2 = accuracy_score(y_teste, previsoes2)
taxa_erro2 = 1- taxa_acerto


