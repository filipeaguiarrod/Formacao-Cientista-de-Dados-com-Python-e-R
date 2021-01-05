# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:19:01 2020

@author: rodri
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # gerar os gráficos 
from sklearn.linear_model import LinearRegression # modelo de regressão linear
import statsmodels.formula.api as sm


base=pd.read_csv('mt_cars.csv')
base = base.drop (['Unnamed: 0'], axis = 1) #Removendo colunas utilizando o argumento axis=1, s/ axis remove linha

#Correlacionar o mpg(consumo galão) e disp(cilindradas)

X=base.iloc[:,2].values # variável independente disp
y=base.iloc[:,0].values# variável mpg dependente quero a previsão

correlação = np.corrcoef(X,y)
X = X.reshape(-1,1) # -1 mantenho linhas, 1 adiciono coluna (formato matriz)

modelo = LinearRegression() #aprendizagem 
modelo.fit(X,y) # fazendo o treinamento ???

modelo.intercept_
modelo.coef_

modelo.score(X,y) #R2

#para ler R2 ajustado preciso de nova biblioteca
#statsmodels.formula.api usando python parecido com r

previsões = modelo.predict(X) #gerando valores de y através do modelo aprendido
modelo_ajustado = sm.ols(formula = 'mpg ~ disp', data = base)
modelo_treinado = modelo_ajustado.fit()
modelo_treinado.summary()

plt.scatter(X,y) # cria gráfico de dispersão 
plt.plot(X,previsões, color='red') # cria gráfico estimado (regressão) e vermelho

#prevendo veiculo com disp = 200 
modelo.predict([[200]])

#Nas últimas versões do sklearn precisamos passar uma matriz como base de dados, e não um vetor. 
#Quando temos o valor [22] 
#é somente um vetor e [[22]] é uma matriz com uma linha e uma coluna


#regressão multpla
X1=base.iloc[:,1:4].values # criando previsão de mpg por cil/disp/hp/drat
Y1=base.iloc[:,0].values

modelo2 = LinearRegression()
modelo2.fit(X1,Y1)

modelo2.score(X1,Y1)
modelo_ajustado2 = sm.ols(formula = 'mpg ~ cyl + disp + hp', data = base)
modelo_treinado2 = modelo_ajustado2.fit()
modelo_treinado2.summary()

novo=np.array([4,200,100])
novo = novo.reshape(1,-1) # transpõe os dados
modelo2.predict(novo)