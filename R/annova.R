tratamento = read.csv(file.choose(),sep=";",header = T)

boxplot(Horas~Remedio,data=tratamento)

an = aov(Horas~Remedio,data=tratamento)

summary(an)

#P-value  comparar com alpha escolhido 
# P-value < 0,05 ? Não 

old.par<-par(mai=c(1.5,2,1,1))


# Aonde está variação ?

tukey=TukeyHSD(an)

tukey

plot(tukey,las=1,col='blue')

InsectSprays

library(lattice)

histogram(~weight | feed, data=chickwts) # Agrego pelo peso o tipo de alimentação