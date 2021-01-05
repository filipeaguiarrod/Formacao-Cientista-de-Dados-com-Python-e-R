# Analise Anova para os grupos de estudo

performance = read.csv(file.choose(),sep=",",header = T)

# Seguem distribui��o normal?


library(lattice)

histogram(~math.score | race.ethnicity, data=performance) # Agrego pelo peso o tipo de alimenta��o

boxplot(math.score~race.ethnicity,data=performance )



#ANNOVA

anova = aov(math.score~race.ethnicity,data=performance)

summary(anova)


# Onde est�o as diferten�as ?
tukey=TukeyHSD(annova)

tukey

plot(tukey)

group D-group A