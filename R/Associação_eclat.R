library(arules)

transacoes = read.transactions(file.choose(),format = "basket", sep=",")

#Forma de visualizações
transacoes
inspect(transacoes)
image(transacoes)


# supp mín e malen numero máximo de itens
regras = eclat(transacoes, parameter = list(supp=0.1, maxlen=15))

inspect(regras)

library(arulesViz)

plot(regras)

plot(regras, method="graph", control=list(type="items"))