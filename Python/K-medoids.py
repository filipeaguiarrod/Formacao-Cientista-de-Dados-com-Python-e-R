# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:28:02 2020

@author: rodri
"""

from sklearn import datasets 
import numpy as np
from sklearn.metrics import confusion_matrix
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer

iris = datasets.load_iris()

# apenas classificaremos agrupamento de dois atributos pois cluster_visualizer
# não suporta + 

cluster = kmedoids(iris.data[:,0:2], [3,12,20]) # dois pois o upper bound ele nao pega

cluster.get_medoids()

#fazer agrupamento

cluster.process()
previsoes = cluster.get_clusters()

# algoritimo escolhe melhor conjunto de clusters 

medoids = cluster.get_medoids()

# visualizador dos medoides

v=cluster_visualizer()
v.append_clusters(previsoes, iris.data[:,0:2])
v.append_cluster(medoids,data=iris.data[:,0:2], marker="*", markersize=15)
v.show()

# para visualizar matriz de confusão tenho que adequar dados de previsoes

lista_previsoes = []
lista_real = [] # o que vem de iris dataset
for i in range(len(previsoes)):
    print("----")
    print(i)
    print("----")
    for j in range(len(previsoes[i])):
        #print(j)
        print(previsoes[i][j])
        lista_previsoes.append(i)
        lista_real.append(iris.target[previsoes[i][j]])
        
# processo parta transformar em numpy array para usar matriz de confusão
lista_previsoes = np.asarray(lista_previsoes)     
lista_real = np.asarray(lista_real)

matrizconfusao = confusion_matrix(lista_previsoes,lista_real)