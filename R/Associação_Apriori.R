library(arules)

transacoes = read.transactions(file.choose(),format = "basket", sep=",")


#Forma de visualiza��es
transacoes
inspect(transacoes)
image(transacoes)


# Suporte e confian�a m�nimos 

regras = apriori(transacoes, parameter = list(supp=0.5,conf=0.5))



# Visualizar regras com mais detalhes

inspect(regras)

# 3 primeiros s�o ele com ele

# install.packages("arulesViz") ajuda nas visualiza��es

library(arulesViz)

plot(regras)

plot(regras, method="graph", control=list(type="items"))

