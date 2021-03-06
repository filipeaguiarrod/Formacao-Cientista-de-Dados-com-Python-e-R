library(e1071) # Biblioteca utilizada pro naivebayes

credito = read.csv(file.choose(),sep=",",header=T)

#criar modelo para ver se algu�m � bom ou mal pagador

# para ser gen�rico: 70% Uso modelo treino / 30% teste

Amostra = sample(2,1000,replace=TRUE,prob=c(0.7,0.3)) # 2 n�meros sorteado 1,2, 1000sorteios, c/ reposi��o e prob 0.7 -1 e 0.3 -1

creditotreino = credito[Amostra==1,] #crio dados com a mesma linha da amostra ==1
creditoteste = credito [Amostra==2,]

# As amostras s�o independentes e n�o v�o estar exatamente 70% e 30 %
dim(creditoteste)
dim(creditotreino)

#Criando modelo naiveBayes classe(variavel dependente)~ todas (.)
#Variavel treino para o modelo

modelo = naiveBayes(class ~ . , creditotreino )

#visualizar modelo
modelo

# pode ser utilizado como objeto posso usa-lo em diferentes locais
class(modelo)

# O modelo � satisfat�rio ? Devo prever com teste

predicao = predict(modelo, creditoteste)

#gera um vetor com resultados
predicao

#Devemos comparar dados teste estimado x dados reais do teste 
#Tabela COnfus�o

confusao = table(creditoteste$class, predicao)
confusao

# Medindo indice de acertos

taxaacerto = (confusao[1]+confusao[4]) / sum(confusao)

taxaerro = (confusao[2]+confusao[3]) / sum(confusao)

#Posso colocar ele em produ��o ? Analisar se resultados s�o satisfat�rios para voc�
