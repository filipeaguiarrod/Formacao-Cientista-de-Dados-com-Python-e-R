library(rpart)

credito = read.csv(file.choose(), sep=",",header = T)

#gerando amostras com dados de treino 70% e 30 % teste

amostra = sample(2,1000,replace=T,prob=c(0.7,0.3))

creditotreino=credito[amostra==1,]
creditoteste=credito[amostra==2,]

# Regras de associação Árvore de Dados

arvore = rpart(class~.,,data=creditotreino, method="class")
print(arvore)

#visualizar arvore 

plot(arvore)
text(arvore,use.n=T,all=T,cex=.8)

# verificando árvore criada

teste = predict(arvore,newdata=creditoteste)
teste

# Predict cria uma probabilidade de ser ou não mal pagador
# Gerar resposta good ou bad de acordo com probabilidade
#

#adicionando colunas teste no credito teste
cred=cbind(creditoteste,teste)
fix(cred)

#coluna nova gerando resultado bad ou good
cred["Result"] = ifelse(cred$bad >=0.5,"bad","good" )
fix(cred)

# MAtriz de confusão

confusao = table(cred$class,cred$Result)

confusao

# Medindo indice de acertos

taxaacerto = (confusao[1]+confusao[4]) / sum(confusao)

taxaerro = (confusao[2]+confusao[3]) / sum(confusao)
