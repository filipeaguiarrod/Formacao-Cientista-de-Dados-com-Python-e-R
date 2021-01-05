# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 11:19:37 2020

@author: rodri
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


###################### Histograma


base=pd.read_csv('trees.csv')


# bins = número de intervalos 
h = np.histogram(base.iloc[:,1], bins='auto')

#plotando o gráfico, posso alterar o bins

plt.hist(base.iloc[:,1],bins=6)
plt.title("Árvores")
plt.ylabel("Frequência")
plt.xlabel("Altura")


###################### Densidade

import seaborn as sns

base=pd.read_csv('trees.csv')


plt.hist(base.iloc[:,1],bins=10)


#hist = true desenha o hist, bins,kde
#sns gera ou histograma(hist) ou densidade(kde) 
sns.distplot(base.iloc[:,1],hist = True, kde=True,bins=6,color="blue",hist_kws={"edgecolor":"black"})

sns.distplot(base.Volume, bins= 10, axlabel = "Volume").set_title("Árvore")



base=pd.read_csv('chicken.csv')

# Precisamos agrupar as categorias dos feed
# adiciono váriavel que vou somar : weight
#[coluna que vou agrupar].função 

agrupado = base.groupby(['feed'])['weight'].sum()


# loc localiza - 
teste = base.loc[base['feed']=='horsebean']

plt.figure() # Defini a página, tudo que eu quiser depois disso estará na mesma página
plt.subplot(3,2,1)
sns.distplot(base.loc[base['feed']=='horsebean'].weight).set_title("Horsebean")


plt.subplot(3,2,2)
sns.distplot(base.loc[base['feed']=='casein'].weight).set_title("casein")


plt.subplot(3,2,3)
sns.distplot(base.loc[base['feed']=='linseed'].weight).set_title("linseed")

plt.tight_layout()# melhora a distribuição



###################### Dispersão




# Avalia se a relação entre variáveis continuas

base=pd.read_csv('trees.csv')

plt.scatter(base.Girth, base.Volume,color="blue",facecolors='none',marker='^')
plt.title("Relação Circunferência e Volume")
plt.ylabel("Volume")
plt.xlabel("Circunferência")

#Visualizar uma linha entre os pontos

plt.plot(base.Girth, base.Volume)

# Quero remover pontos muito próximos com jitter (x ou y ou ambos)
# Ele não remove ou muda valores apenas a visualização
# fit_reg=linha da regressão std é normal

sns.regplot(base.Girth, base.Volume,data=base,x_jitter=0.5,fit_reg=False)



############ Dispersão+Legendas




base=pd.read_csv('CO2.csv')

x = base.conc
y = base.uptake

# set pela conjunto de dados sem repetição de valores

unicos = list(set(base.Treatment))

#Agrupando valores dependendo da categoria:

for i in range (len(unicos)): # executa for duas vezes pelo len
    indice = base.Treatment == unicos[i]
    plt.scatter(x[indice],y[indice],label=unicos[i])
plt.legend(loc = "lower right")


# hue = escolho quem classifica de acordo com que lugar
sns.scatterplot(base.conc, base.uptake,hue=base.Type)

#### Gráfico Condicional

q = base.loc[base["Type"]=="Quebec"]
    
m = base.loc[base["Type"]=="Mississippi"]

plt.figure()
plt.subplot(2,2,1)
sns.scatterplot(q.conc,q.uptake).set_title("Quebec")
plt.subplot(2,2,2)
sns.scatterplot(m.conc,m.uptake).set_title("Mississippi")

plt.tight_layout()# melhora a distribuição    


##################

base = pd.read_csv("esoph.csv")

sns.catplot(x="alcgp",y="ncontrols",data=base,jitter=False)

sns.catplot(x="alcgp",y="ncontrols",data=base,col="tobgp")



###################### Dividindo a Tela

base=pd.read_csv('trees.csv')

plt.figure(1) # 1 determina a "página das figuras abaixo 

# Girth com Volume 

plt.subplot(2,2,1) # (nºLinhas, n°colunas,ID do gráfico)
plt.scatter(base.Girth, base.Volume)

# Girth com Height
plt.subplot(2,2,2) # (nºLinhas, n°colunas,ID do gráfico)
plt.scatter(base.Girth, base.Height)

# Height com Volume 
plt.subplot(2,2,3) # (nºLinhas, n°colunas,ID do gráfico)
plt.scatter(base.Height, base.Volume)

# Histograma com Volume 
plt.subplot(2,2,4) # (nºLinhas, n°colunas,ID do gráfico)
plt.hist(base.Volume)


###################### Boxplot

base=pd.read_csv('trees.csv')

plt.boxplot(base.Volume, vert = False, showfliers = False, notch = True,
            patch_artist = True)
plt.title('Árvores')
plt.xlabel('Volume')

# colorir
# https://matplotlib.org/gallery/statistics/boxplot_demo.html

plt.boxplot(base)

plt.boxplot(base.Volume, vert = False)
plt.boxplot(base.Girth, vert = False)
plt.boxplot(base.Height, vert = False)

###### Boxplot com seaborn


import seaborn as sns

sns.boxplot(base.Volume).set_title("Árvores")


# faz todos boxplots juntos

sns.boxplot(data=base)



###################### Gráficos de Setores

# Só utilizamos o pandas!


# Úteis para visualizar variáveis categóricas

base=pd.read_csv('insect.csv')

# Precisamos agrupar as categorias dos sprays
# adiciono váriavel que vou usar para agrupar : spray
#[coluna que vou agrupar].função 

agrupado = base.groupby(['spray'])['count'].sum()

agrupado.plot.bar(color="gray")

##### Gráfico de Pizza

agrupado.plot.pie(legend=True)


###################### Gráficos 3D


from mpl_toolkits.mplot3d import axes3d

base = pd.read_csv("orchard.csv")

figura = plt.figure()
eixo = figura.add_subplot(1,1,1,projection="3d") # projection para plotar 3d
eixo.scatter(base.decrease, base.rowpos, base.colpos)
eixo.set_xlabel("decrease")
eixo.set_ylabel("rowpos")
eixo.set_zlabel("colpos")

# cores
# https://pythonspot.com/3d-scatterplot/

























