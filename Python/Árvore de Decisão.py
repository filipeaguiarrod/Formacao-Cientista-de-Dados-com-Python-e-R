# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:40:41 2020

@author: rodri
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
import graphviz
from sklearn.tree import export_graphviz

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
## sobre test split ver exemplos : https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html?highlight=train_test_split#sklearn.model_selection.train_test_split

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,classe,test_size = 0.3,random_state=0)

################################Gerando Modelo Árvore de Decisão

arvore= DecisionTreeClassifier()
arvore.fit(X_treinamento,y_treinamento) #Aqui ele aprende!

# Para que seja possível visualizar a árvore

export_graphviz(arvore, out_file="tree.dot")

#Gera na pasta de trabalho o tree.dot - copio os dados e vou para
#www.webgraphviz.com

previsoes = arvore.predict(X_teste) # prevendo para o teste 
# para o predict ele pegou cada registro submeteu a árvore e
# decidiu resultado de acordo com a arvore


################################ Matriz de Confusão
matriz_confusão = confusion_matrix(y_teste,previsoes)

taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1- taxa_acerto


