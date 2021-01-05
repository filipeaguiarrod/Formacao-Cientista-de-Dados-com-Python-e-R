install.packages("cluster", dependencies = T)

library(cluster)


# chamando método pam, k=3 grupos que quero

cluster = pam(iris[,1:4],k=3)

plot(cluster)

#tabela de contigência ????? 

table(iris$Species,cluster$clustering)