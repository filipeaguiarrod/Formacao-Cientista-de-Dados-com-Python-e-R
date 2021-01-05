#install.packages("neuralnet")
library(neuralnet)

#binearizar? os dados

myiris = iris

#criando uma nova coluna nos dados iris
#cbind adiciona uma coluna e == é um operador lógico

myiris = cbind(myiris,myiris$Species=='setosa')
myiris = cbind(myiris,myiris$Species=='versicolor')
myiris = cbind(myiris,myiris$Species=='virginica')

summary(myiris)

# iremos mudar os nomes das colunas 

names(myiris) [6] = 'setosa'
names(myiris) [7] = 'versicolor'
names(myiris) [8] = 'virginica'

#criaremos amostras para 70% treino e 30% teste

amostra = sample(2,150,replace=T, prob=c(0.7,0.3))

myiristreino = myiris[amostra==1,]
myiristeste = myiris[amostra==2,]

dim(myiristreino)
dim(myiristeste)

# criando o modelo
#hidden = são quantas camadas internas(ocultas) uma c/ 5 e 4

modelo=neuralnet(setosa+versicolor+virginica ~ Sepal.Length + Sepal.Width + Petal.Length + Petal.Width, myiristreino, hidden=c(5,4))
print(modelo)
plot(modelo)

#faremos o teste do modelo
#compute fazendo a previsão

teste = compute(modelo,myiristeste[,1:4])
teste$net.result # matriz criada através do modelo (previsto)

#preciso através dos resultados do teste atribuir os classificadores para 
#resultados maiores

resultado = as.data.frame(teste$net.result)
names(resultado) [1] = 'setosa'
names(resultado) [2] = 'versicolor'
names(resultado) [3] = 'virginica'

#para que eu consiga comparar quem acertou e quem errou preciso de uma coluna
#com o resultado da classe prevista

resultado$class = colnames(resultado[,1:3])[max.col(resultado[,1:3],ties.method ='first')]
head(resultado)

# Matriz de confusão

confusao = table(resultado$class,myiristeste$Species)

acerto = (sum(diag(confusao))/sum(confusao))*100