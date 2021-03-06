library(arules)

transacoes = read.transactions(file.choose(),format = "basket", sep=",")

#Forma de visualiza��es
transacoes
inspect(transacoes)
image(transacoes)


# supp m�n e malen numero m�ximo de itens
regras = eclat(transacoes, parameter = list(supp=0.1, maxlen=15))

inspect(regras)

library(arulesViz)

plot(regras)

plot(regras, method="graph", control=list(type="items"))