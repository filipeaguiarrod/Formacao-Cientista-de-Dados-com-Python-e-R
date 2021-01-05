# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:05:14 2020

@author: rodri
"""

# Fuzzy Means mostra a probabilidade de cada um pertencer a cada grupo.

from sklearn import datasets 
import numpy as np
from sklearn.metrics import confusion_matrix
import skfuzzy

iris = datasets.load_iris()


# variavel r ira abrigar resultados.
# devo instalar skfuzzy no terminal
# data tem que ser transposta (data.T), std variaveis  c=3, m=2, 
# error = 0.005, maxiter = 1000, init = None vem da documentação

r = skfuzzy.cmeans(data=iris.data.T, c=3, m=2, error = 0.005, maxiter = 1000, 
                   init = None)

previsoes = r[1]

previsoes[0][0]

# valor maior de probabilidade será do grupo ....

previsoesgrupo = previsoes.argmax(axis = 0 )

# ele no argmax pega maior valor e mostra qual indice que este corresponde.

matrizconfusao = confusion_matrix(iris.target,previsoesgrupo)