install.packages("igraph",dependencies =T)

library("igraph")


#Criando Grafo manualmente 1-2  2-3 3-4 4-1
#Edge = aresta

grafo1 = graph(edges=c(1,2,2,3,3,4,4,1))
plot(grafo1)
grafo

# Grafo com duas direções
grafo1 = graph(edges=c(1,2,2,3,3,4,4,1,1,4,4,3,3,2,2,1))
plot(grafo1)

# Grafo com auto relacionamento
grafo3 = graph(edges=c(1,2,2,3,3,4,4,1,1,1)) 
plot(grafo3)

# + aresta segue na direção do vértice, -+ direção pra direita 
grafo3 = graph_from_literal(1-+2,2-+3,3++4,4-+1) 
plot(grafo3)


#GRafo Literal nao direcionado.

grafo2 = graph_from_literal(1-2,2-3,3-4,4-1) 
plot(grafo2)

#GRafo Literal nao direcionado com isolado

grafo2 = graph_from_literal(1-2,2-3,3-4,4-1,5) 
plot(grafo2)