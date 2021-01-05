library(arules)

transacoes = read.transactions(file.choose(),format = "basket", sep=",")


#Forma de visualizações
transacoes
inspect(transacoes)
image(transacoes)


# Suporte e confiança mínimos 

regras = apriori(transacoes, parameter = list(supp=0.5,conf=0.5))



# Visualizar regras com mais detalhes

inspect(regras)

# 3 primeiros são ele com ele

# install.packages("arulesViz") ajuda nas visualizações

library(arulesViz)

plot(regras)

plot(regras, method="graph", control=list(type="items"))

