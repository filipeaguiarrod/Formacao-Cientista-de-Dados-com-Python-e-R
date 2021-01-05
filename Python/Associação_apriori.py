# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:23:34 2020

@author: rodri
"""

#Regras de associação

import pandas as pd
from apyori import apriori

dados = pd.read_csv('transacoes.txt', header = None) # reader para ignorar 
#primeira linha


# Preciso transformar dados de dataframe para list
transacoes=[]
for i in range(0,6):
    transacoes.append([str(dados.values[i,j]) for j in range(0,3)])
    
regras = apriori(transacoes, min_support=0.5, min_confidence=0.5)
resultados = list(regras)

# Preciso visualizar de forma melhor

resultados2= [list(x) for x in resultados]

resultados3=[]
for j in range (0,7):
    resultados3.append([list(x) for x in resultados2[j][2]])