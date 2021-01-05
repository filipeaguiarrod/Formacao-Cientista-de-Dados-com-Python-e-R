install.packages("mltools",dependencies=T)
install.packages("data.table",dependencies=T)

library(mltools)
library(data.table)

Titanic
class(Titanic)

tit = as.data.frame(Titanic)

#Visualizando Label Encoding;

labelenc = data.matrix(tit[,1:3]) # label encoding / função nativa


# Hot encoding
# espera data_table

tit = as.data.table(tit)

#BInarizou as classes;

hotenco = one_hot(tit[,1:3])