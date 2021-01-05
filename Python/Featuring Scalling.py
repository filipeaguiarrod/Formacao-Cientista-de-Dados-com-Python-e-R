# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:44:07 2020

@author: rodri
"""

import pandas as pd

credito = pd.read_csv("Credit.csv")

# Pego as colunas separadas
dt=credito.iloc[:,[1,4,7]].values


from sklearn.preprocessing import StandardScaler, MinMaxScaler


# Faremos a padronização através do Z-score

sc = StandardScaler()
x_pad = sc.fit_transform(dt)

# Normalização pelo Min Max Scaler - divido pelo máx

mms = MinMaxScaler()
x_norm = mms.fit_transform(dt)