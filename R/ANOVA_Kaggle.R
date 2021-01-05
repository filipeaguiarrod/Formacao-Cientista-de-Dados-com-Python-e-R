# Analise Anova para os grupos de estudo

performance = read.csv(file.choose(),sep=",",header = T)

# Seguem distribuição normal?


library(lattice)

histogram(~math.score | race.ethnicity, data=performance) # Agrego pelo peso o tipo de alimentação

boxplot(math.score~race.ethnicity,data=performance )



#ANNOVA

anova = aov(math.score~race.ethnicity,data=performance)

summary(anova)


# Onde estão as difertenças ?
tukey=TukeyHSD(annova)

tukey

plot(tukey)

group D-group A