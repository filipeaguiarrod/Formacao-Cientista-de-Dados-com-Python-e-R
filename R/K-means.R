head(iris)
summary(iris)

#crio uma vari�vel cluster (grupo)

cluster = kmeans(iris[1:4],center=3)

# Quanto realmente o agrupamento tem semelhan�a com esp�cie de iris.
# crio matriz atrav�s dos dois que se relacionam


table(iris$Species,cluster$cluster)

# Gr�fico de dispers�o para an�lise de classifica��o

plot(iris[,1:4],col=cluster$cluster)
