grafo2 = graph(edges=c(1,2,3,3,3,4,4,1))
class(grafo2)
plot(grafo2)

# D - direcionado e U Não direcionado
# Por Padrão o Graph cria direcionado / não direcionado -> (directed = F)
# Elementos isolados

grafo3 = graph(edges=c(1,2,3,3,3,4,4,1),directed = F)
plot(grafo3)

#n= número de vertices
grafo4 = graph(edges=c(1,2,3,3,3,4,4,1),directed = F,n=10)
plot(grafo4)

grafo5 = graph(edges=c('A','B','B','C','C','D','D','E','E','A','A','C','C','B'),isolates = c("F","G"))
plot(grafo5)