# Pacote Necess�rio para utilizar

install.packages("tm")

library(tm)

getSources() # Poss�veis tipos de dados que posso utilizar

getReaders() # Formas que posso ler o texto;

# Come�ando com a cria��o do Corpus
#Cria-se uma v�riavel para armazenar tudo;


# Criarei uma v�riavel Vol�til / 
# Ele lera todos arquivos o mesmo diret�rio.
#Cria Metadado com todos textos
corpus = VCorpus(DirSource("C:/dados", encoding="UTF-8"),readerControl=list(reader=readPlain,language="eng"))



# TermDocumentMatrix # DocumentTermMatrix

freq = TermDocumentMatrix(corpus)
matriz = as.matrix(freq)
matriz = sort(rowSums(matriz), decreasing = T)
matriz = data.frame(word=names(matriz), freq=matriz)

#Lendo linhas 
head(matriz,n=100)