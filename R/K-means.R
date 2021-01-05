head(iris)
summary(iris)

#crio uma variável cluster (grupo)

cluster = kmeans(iris[1:4],center=3)

# Quanto realmente o agrupamento tem semelhança com espécie de iris.
# crio matriz através dos dois que se relacionam


table(iris$Species,cluster$cluster)

# Gráfico de dispersão para análise de classificação

plot(iris[,1:4],col=cluster$cluster)
