###################### Histograma


# Utilizando para visualizar apenas uma v�riavel continua.

hist(trees$Height)

# Adicionando detalhes no gr�fico
hist(trees$Height, main="�rvores",ylab="Altura",xlab="Altura",col="blue")

# Posso Altera n�mero de quebras e densidade da cor;

hist(trees$Height, main="�rvores",ylab="Altura",xlab="Altura",col="blue",density=10, breaks=20)

############# Histograma com Lattice

library(lattice)

#aspect=2 - quanto maior mais compacto ( Apenas visualmente )
#type="count" - frequ�ncia relativa 
#nint=10 - n�mero de barras

histogram(trees$Volume,main="�rvores",xlab="Volume",aspect=1,type="count",nint=10)

chickwts #dados com galinhas e seus pesos cada uma com uma alimenta��o

aggregate(chickwts$weight,by=list(chickwts$feed),FUN=sum)

#Histograma condicional 

histogram(~weight | feed, data=chickwts) # Agrego pelo peso o tipo de alimenta��o


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

densityplot(~CO2$conc | CO2$Treatment, plot.points=F)#plot.points=F tiro pontos da dispers�o



###################### Dispers�o

plot(trees$Girth,trees$Volume,main="�rvores",ylab="Circunfer�ncia",xlab="Volume",col="blue")
# Mudar tipo do ponto
plot(trees$Girth,trees$Volume,main="�rvores",ylab="Circunfer�ncia",xlab="Volume",col="blue",pch=20)
#Type muda o tipo( pontos, linhas e etc)
plot(trees$Girth,trees$Volume,main="�rvores",ylab="Circunfer�ncia",xlab="Volume",col="blue",pch=20,type='l')
#jitter varia��o de dados para reduzir sobreposi��o
plot(jitter(trees$Girth),trees$Volume,main="�rvores",ylab="Circunfer�ncia",xlab="Volume",col="blue",pch=20)


##### Dispers�o c/ Legendas

CO2 # Base de dados
#Gerei cores diferentes para v�riaveis conforme classifica��o do Tretment
plot(CO2$conc,CO2$uptake,pch=20,col=CO2$Treatment)
# Colocando Legenda
legend("bottomright",legend=c("nonchilled","chilled"),cex=1,fill=c("black","red"))

############# Dispers�o com Lattice

library(lattice)

xyplot(CO2$conc~CO2$uptake)

#Adicionando Variavel categ�rica

xyplot(CO2$conc~CO2$uptake|CO2$Type) # Divide em classifica��es
xyplot(CO2$conc~CO2$uptake|CO2$Treatment) 


esoph # Dados

dotplot(esoph$alcgp~esoph$ncontrols,data=esoph )

dotplot(esoph$alcgp~esoph$ncontrols|esoph$tobgp,data=esoph )


###################### Visualiza��o de V�rios Gr�ficos

plot(trees) # Vari�veis continuas ele me mostra todas op��es

plot(CO2)

# Se eu quiser divir a tela para organizar gr�ficos;

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

boxplot(trees$Volume, main="�rvores",xlab="Volume")

boxplot(trees$Volume, main="�rvores",xlab="Volume",col="blue",horizontal=T)

# Se eu quiser remover outlier:

boxplot(trees$Volume, main="�rvores",xlab="Volume",col="blue",horizontal=T,outline=F)

# Ver os par�metros do boxplot:

boxplot.stats(trees$Volume)

boxplot(trees)


############# Boxplot com Lattice

library(lattice)

bwplot(trees$Volume,main="�rvores",xlab="Volume")



###################### Gr�fico de Barra / Setor

InsectSprays

#Agregando dados em soma
spray=aggregate(.~spray,data=InsectSprays, sum)

#Gr�fico de Barras
barplot(spray$count,col=gray.colors(6),xlab="Spray",ylab="total",names.arg=spray$spray)

#Gr�fico de Pizza
pie(spray$count,main="Spray",labels=spray$spray)
pie(spray$count,main="Spray",labels=NA,col=c(1:6))
legend("bottomright",legend=spray$spray,fill = c(1:6))


###################### Gr�fico 3D
# 3 Vari�veis no mesmo gr�fico

cloud(decrease~rowpos*colpos,data=OrchardSprays )

cloud(decrease~rowpos*colpos,groups=treatment,data=OrchardSprays ) #Groups cor por classfica��o do treatment