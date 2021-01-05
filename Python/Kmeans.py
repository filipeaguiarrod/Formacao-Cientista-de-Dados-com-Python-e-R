# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:25:19 2020

@author: rodri
"""

from sklearn import datasets 
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

iris= datasets.load_iris()

# Quantos elementos tenho de cada classe ?

unicos, quantidade = np.unique(iris.target,return_counts=True)

# unicos, quantidades ->(data que vou ler, quero tmb quantidade ?)

# Fazer treinamento do Kmeans:

cluster = KMeans(n_clusters=3) # quantos clusters ? 3 
cluster.fit(iris.data) #treino o cluster

centroides = cluster.cluster_centers_
# ele mostra matriz de grupo por valores estimados de centroides
# de cada atributo

previsoes = cluster.labels_ # mostra qual foram as classificacoes dos dados


unicos2, quantidade2 = np.unique(previsoes,return_counts=True)
# unicos, quantidades ->(data que vou ler, quero tmb quantidade ?)


# Validando meu classificador, aproveito que existem classes 
matriz_confusão = confusion_matrix(iris.target, previsoes)
# nao posso analisar pela diagonal principal


# plotando valores, criando filtro apenas dos valores que fazem parte
# do grupo zero
# Passamos coluna 0 e 1 gráficos indicam apenas os dois primeiros atributos para cada classe
#Previsões = grupo 1
plt.scatter(iris.data[previsoes==0,0],iris.data[previsoes==0,1],c='green',label='Setosa')

#Previsões = grupo 2 

plt.scatter(iris.data[previsoes==1,0],iris.data[previsoes==1,1],c='red',label='Versicolor')

#Previsões = grupo 3 

plt.scatter(iris.data[previsoes==2,0],iris.data[previsoes==2,1],c='blue',label='Virginica')

plt.legend()