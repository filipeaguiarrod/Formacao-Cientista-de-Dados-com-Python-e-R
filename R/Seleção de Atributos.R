library(e1071)

#Utilizando Máquina de Vetor svm
#svm(variavel dependente, conjunto de dados)
#
#

modelo = svm(class~. , creditotreino)
modelo

# Fazer predição para análise do modelo criado.

predicao = predict(modelo, creditoteste)
predicao

#Criando Matriz de Confusão

confusao = table(creditoteste$class,predicao)
confusao

taxaacerto = (confusao[1]+confusao[4]) / sum(confusao)
#0.7627737
taxaerro = (confusao[2]+confusao[3]) / sum(confusao)
#0.2445255

#Quais colunas são mais relevantes na classificação.
#Utilizar pacote feature selector

install.packages("FSelector",dependencies = T)

library(FSelector)

random.forest.importance(class~.,credito)

# Me entrega em lista quais atributos são mais importantes para classificar
# 4 primeiros eu utilizarei para fazer o esquema no Atributos 2

