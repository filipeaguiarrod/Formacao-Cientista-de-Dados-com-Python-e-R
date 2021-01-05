# Dimensionamento de Características/

boxplot(iris[,1:4])

# Realizando padronização nos atributos;
# PAdronização por Z-score - normal

iris_padr = scale(iris[,1:4])
boxplot(iris_padr)

#  Normalização por Min-max:

normaliza = function(x)
  {
  return ((x-min(x))/(max(x)-min(x)))
  }


iris_norm = normaliza(x=iris[,1:4])
boxplot(iris_norm)

