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

#Ferramentas

inspect(corpus[1:100])
as.character(corpus[[2]])

# Retorna uma lista de palavras sem valor semântico

stopwords("portuguese")

# Quero remover os stopwords.

corpus = tm_map(corpus,removeWords,stopwords("english")) #remove palavras sem valor
corpus = tm_map(corpus,stripWhitespace) #remove excesso de espaço em branco
corpus = tm_map(corpus,removePunctuation) # Removendo pontuação
corpus = tm_map(corpus,removeNumber) # Remover números se nao preciso deles

# Quero Criar uma núvem de palavras e ver quais palavras são mais frequentes

#Nuvem de Palavras

install.packages("wordcloud")

library(wordcloud)

#Gerando Nuvem de Palavras com parâmetro minha variavel corpus
#Palavras maiores tem uma frequência maior.


#random.order=T forma aleatória 
# colors=rainbow(8) cores diferentes
#rot.per=0.5 divide quantos em pé e deitados
#use.r.layout = T faz uma variação do layout

wordcloud(corpus,max.words = 100,random.order=T,colors=rainbow(8),rot.per=0.5,use.r.layout = T)