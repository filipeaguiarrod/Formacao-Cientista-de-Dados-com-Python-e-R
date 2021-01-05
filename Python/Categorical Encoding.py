# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:29:43 2020

@author: rodri
"""

import pandas as pd

credito = pd.read_csv("Credit.csv")

X=credito.iloc[:,8:10].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer

labelencoder = LabelEncoder()
X[:,0] = labelencoder.fit_transform(X[:,0])

# pega a coluna que precisa de label" classe " e gera binarização e onehotencoder
# para evitar dummy_trap devemos excluir coluna
onehotencoder = make_column_transformer((OneHotEncoder(categories="auto",sparse = "false"), [1]),remainder="passthrough")
X = onehotencoder.fit_transform(X)

# para evitar dummy_trap devemos excluir coluna
X = X[:,1:4] 