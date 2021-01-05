# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:47:58 2020

@author: rodri
"""


#pip install mongo

from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017/')


# Recuperar banco de dados
db = cliente.dbmidias

# Recuperar coleção 

conexao = db.posts

print(conexao.find_one())

print(conexao.find_one({"nome":"José"}))

# find all preciso percorrer um cursor

for conexao in conexao.find():
    print(conexao)
