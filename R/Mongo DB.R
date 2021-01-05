install.packages("mongolite")

library(mongolite)


# Parametros que quero conectar

conexão = mongo(collection="posts", db="dbmidias",url = "mongodb://localhost")

dados = conexão$find() # crio váriavel data.frame

# Posso procurar igual no mongo / igual só José

dados = conexão$find('{"nome":"José"}')