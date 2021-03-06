#Aprendizado baseado em inst�ncia
#Utiliza dados Hist�ricos para Classificar uma proximidade

#
#
install.packages("class",dependencies=T)
library(class)

head(iris)
summary(iris)

#Gerando amostra Treino e Dados a classificar

amostra = sample(2,150, replace=T, prob=c(0.7,0.3))
iristreino = iris[amostra==1,]
classificar = iris[amostra==2,]

dim(iristreino)
dim(classificar)


#knn - nearest neighbor
#k - n�mero de vizinhos + pr�ximos a serem considerados
#todaas colunas sem a classe
#knn(par�metros p/ localizar vizinho, dados a classificar,aonde est�o classes)

previsao = knn(iristreino[,1:4],classificar[,1:4],iristreino[,5],k=3)

#Matriz de Confus�o

table(classificar[,5],previsao)

previsao
