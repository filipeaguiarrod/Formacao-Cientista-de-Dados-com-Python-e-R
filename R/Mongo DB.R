install.packages("mongolite")

library(mongolite)


# Parametros que quero conectar

conex�o = mongo(collection="posts", db="dbmidias",url = "mongodb://localhost")

dados = conex�o$find() # crio v�riavel data.frame

# Posso procurar igual no mongo / igual s� Jos�

dados = conex�o$find('{"nome":"Jos�"}')