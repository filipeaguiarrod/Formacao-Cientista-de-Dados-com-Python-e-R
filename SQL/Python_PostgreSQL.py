# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

# pip install psycopg2

import psycopg2

#Gerando a conexão com o servidor de dados SQL

conexao = psycopg2.connect(host='localhost',database='DS',user="postgres",password="sadafi",port=5432)

#crio um cursos para que percorra os dados

cursor = conexao.cursor()

#crio uma consulta com a linguagem sql

consulta = "select * from clientes"
cursor.execute(consulta)
# retorna todos registros com fetchall e retornar em uma variável
registros = cursor.fetchall()

# quero imprimir apenas 5 registros.



#Percorrendo registros.

for row in registros:
    print("Nome = ",row[1],)
    print("Estado = ",row[2],)
    print("Status = ",row[4], "\n")
    
    
# Fechamos as conexões.
cursor.close()
conexao.close()


