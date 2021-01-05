# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:14:24 2020

@author: rodri
"""


from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt
 
dados = norm.rvs(size=100) # dados normalizados aleatórios (100 valores)
print(dados)
 
stats.probplot(dados, plot=plt) #curva normal e real.
