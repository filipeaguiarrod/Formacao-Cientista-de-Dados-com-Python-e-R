library(e1071)
#Utilizando Máquina de Vetor svm
#svm(variavel dependente, conjunto de dados)
#
#

modelo=svm(class~ checking_status + duration + credit_history + credit_amount,creditotreino)
predicao = predict(modelo, creditoteste)

confusao = table(creditoteste$class,predicao)
confusao

taxaacerto = (confusao[1]+confusao[4]) / sum(confusao)
#0.7627737
taxaerro = (confusao[2]+confusao[3]) / sum(confusao)
#0.2445255


taxaacerto
taxaerro 