###################### Histograma


# Utilizando para visualizar apenas uma váriavel continua.

hist(trees$Height)

# Adicionando detalhes no gráfico
hist(trees$Height, main="Árvores",ylab="Altura",xlab="Altura",col="blue")

# Posso Altera número de quebras e densidade da cor;

hist(trees$Height, main="Árvores",ylab="Altura",xlab="Altura",col="blue",density=10, breaks=20)

############# Histograma com Lattice

library(lattice)

#aspect=2 - quanto maior mais compacto ( Apenas visualmente )
#type="count" - frequência relativa 
#nint=10 - número de barras

histogram(trees$Volume,main="Árvores",xlab="Volume",aspect=1,type="count",nint=10)

chickwts #dados com galinhas e seus pesos cada uma com uma alimentação

aggregate(chickwts$weight,by=list(chickwts$feed),FUN=sum)

#Histograma condicional 

histogram(~weight | feed, data=chickwts) # Agrego pelo peso o tipo de alimentação


###################### Densidade

densidade = density(trees$Height)

plot(densidade)

# Juntando Histograma e Densidade 

hist(trees$Height,main=NULL,xlab=NULL)
par(new=TRUE) # Usado para que eu consiga sobrepor 
plot(densidade)

############# Densidade com Lattice

library(lattice)


densityplot(CO2$conc)

densityplot(~CO2$conc | CO2$Treatment, plot.points=F)#plot.points=F tiro pontos da dispersão



###################### Dispersão

plot(trees$Girth,trees$Volume,main="Árvores",ylab="Circunferência",xlab="Volume",col="blue")
# Mudar tipo do ponto
plot(trees$Girth,trees$Volume,main="Árvores",ylab="Circunferência",xlab="Volume",col="blue",pch=20)
#Type muda o tipo( pontos, linhas e etc)
plot(trees$Girth,trees$Volume,main="Árvores",ylab="Circunferência",xlab="Volume",col="blue",pch=20,type='l')
#jitter variação de dados para reduzir sobreposição
plot(jitter(trees$Girth),trees$Volume,main="Árvores",ylab="Circunferência",xlab="Volume",col="blue",pch=20)


##### Dispersão c/ Legendas

CO2 # Base de dados
#Gerei cores diferentes para váriaveis conforme classificação do Tretment
plot(CO2$conc,CO2$uptake,pch=20,col=CO2$Treatment)
# Colocando Legenda
legend("bottomright",legend=c("nonchilled","chilled"),cex=1,fill=c("black","red"))

############# Dispersão com Lattice

library(lattice)

xyplot(CO2$conc~CO2$uptake)

#Adicionando Variavel categórica

xyplot(CO2$conc~CO2$uptake|CO2$Type) # Divide em classificações
xyplot(CO2$conc~CO2$uptake|CO2$Treatment) 


esoph # Dados

dotplot(esoph$alcgp~esoph$ncontrols,data=esoph )

dotplot(esoph$alcgp~esoph$ncontrols|esoph$tobgp,data=esoph )


###################### Visualização de Vários Gráficos

plot(trees) # Variáveis continuas ele me mostra todas opções

plot(CO2)

# Se eu quiser divir a tela para organizar gráficos;

split.screen(figs=c(2,2))
screen(1)
plot(trees$Girth,trees$Volume)
screen(4)
plot(trees$Girth,trees$Height)
screen(2)
hist(trees$Height)

# Quero desabilitar o recurso 

close.screen(all=TRUE)

###################### Boxplot

#Limite inferior e superior ( 50% aceitavel para cima e para baixo)
#Mediana

boxplot(trees$Volume, main="Árvores",xlab="Volume")

boxplot(trees$Volume, main="Árvores",xlab="Volume",col="blue",horizontal=T)

# Se eu quiser remover outlier:

boxplot(trees$Volume, main="Árvores",xlab="Volume",col="blue",horizontal=T,outline=F)

# Ver os parâmetros do boxplot:

boxplot.stats(trees$Volume)

boxplot(trees)


############# Boxplot com Lattice

library(lattice)

bwplot(trees$Volume,main="Árvores",xlab="Volume")



###################### Gráfico de Barra / Setor

InsectSprays

#Agregando dados em soma
spray=aggregate(.~spray,data=InsectSprays, sum)

#Gráfico de Barras
barplot(spray$count,col=gray.colors(6),xlab="Spray",ylab="total",names.arg=spray$spray)

#Gráfico de Pizza
pie(spray$count,main="Spray",labels=spray$spray)
pie(spray$count,main="Spray",labels=NA,col=c(1:6))
legend("bottomright",legend=spray$spray,fill = c(1:6))


###################### Gráfico 3D
# 3 Variáveis no mesmo gráfico

cloud(decrease~rowpos*colpos,data=OrchardSprays )

cloud(decrease~rowpos*colpos,groups=treatment,data=OrchardSprays ) #Groups cor por classficação do treatment