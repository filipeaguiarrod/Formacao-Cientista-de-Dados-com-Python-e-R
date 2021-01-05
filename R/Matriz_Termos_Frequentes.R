# Pacote Necessário para utilizar

install.packages("tm")

library(tm)

getSources() # Possíveis tipos de dados que posso utilizar

getReaders() # Formas que posso ler o texto;

# Começando com a criação do Corpus
#Cria-se uma váriavel para armazenar tudo;


# Criarei uma váriavel Volátil / 
# Ele lera todos arquivos o mesmo diretório.
#Cria Metadado com todos textos
corpus = VCorpus(DirSource("C:/dados", encoding="UTF-8"),readerControl=list(reader=readPlain,language="eng"))



# TermDocumentMatrix # DocumentTermMatrix

freq = TermDocumentMatrix(corpus)
matriz = as.matrix(freq)
matriz = sort(rowSums(matriz), decreasing = T)
matriz = data.frame(word=names(matriz), freq=matriz)

#Lendo linhas 
head(matriz,n=100)