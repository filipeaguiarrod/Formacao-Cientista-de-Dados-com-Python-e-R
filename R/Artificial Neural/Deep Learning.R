digitos = read.csv(gzfile(file.choose()),header=F)
dim(digitos)
head(digitos)

# função que divide tela de plotagem em 4 para que eu possa
#ver 4 gráficos de uma vez

split.screen(figs=c(2,2))# crio divisao de 4 dos gráficos

####################### - 4 

dig = t(matrix(unlist(digitos[20,-785]),nrow=28,byrow=F))
dig = t(apply(dig,2,rev))
image(dig,col=grey.colors(255)) # ploto a imagem
screen(1)# qual das 4 telas vou plotar.

####################### - 3

dig = t(matrix(unlist(digitos[2,-785]),nrow=28,byrow=F))
dig = t(apply(dig,2,rev))
image(dig,col=grey.colors(255))
screen(2)

####################### - 0

dig = t(matrix(unlist(digitos[4,-785]),nrow=28,byrow=F))
dig = t(apply(dig,2,rev))
image(dig,col=grey.colors(255))
screen(3)

####################### - 2

dig = t(matrix(unlist(digitos[5,-785]),nrow=28,byrow=F))
dig = t(apply(dig,2,rev))
image(dig,col=grey.colors(255))
screen(4)

####################### Trabalhando efetivamente com redes neurais

install.packages("Rcurl",dependencies=T)
install.packages("h2o",dependencies=T)

library(h2o)

#Inicializando pacote.

h2o.unload()
