# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:17:40 2020

@author: rodri
"""

import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt # gerar os gráficos
from statsmodels.stats.multicomp import MultiComparison 

tratamento = pd.read_csv('anova.csv',sep=';') # abrir csv com separados ";"


tratamento.boxplot(by = 'Remedio', grid=False) # criar box plot dos dados em função de Remedio e grid tira linhas

plt.scatter(tratamento.Remedio,tratamento.Horas)

modelo1=ols("Horas ~ Remedio", data=tratamento).fit() # cria modelo através de data / fit faz o treinamento (regressão)
resultados1 = sm.stats.anova_lm(modelo1) # teste do anova

modelo2=ols("Horas ~ Remedio*Sexo", data=tratamento).fit() # cria modelo através de data + de 1 coluna/ fit faz o treinamento (regressão)
resultados2 = sm.stats.anova_lm(modelo2) # teste do anova

#Existe variação significativa ? Método Turkey

ac = MultiComparison (tratamento['Horas'], tratamento['Remedio'])
resultado_teste=ac.tukeyhsd()
print(resultado_teste)
resultado_teste.plot_simultaneous()

