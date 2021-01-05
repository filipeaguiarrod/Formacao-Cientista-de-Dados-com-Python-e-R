# Dimensionamento de Caracter�sticas/

boxplot(iris[,1:4])

# Realizando padroniza��o nos atributos;
# PAdroniza��o por Z-score - normal

iris_padr = scale(iris[,1:4])
boxplot(iris_padr)

#  Normaliza��o por Min-max:

normaliza = function(x)
  {
  return ((x-min(x))/(max(x)-min(x)))
  }


iris_norm = normaliza(x=iris[,1:4])
boxplot(iris_norm)
