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

#Ferramentas

inspect(corpus[1:100])
as.character(corpus[[2]])

# Retorna uma lista de palavras sem valor sem�ntico

stopwords("portuguese")

# Quero remover os stopwords.

corpus = tm_map(corpus,removeWords,stopwords("english")) #remove palavras sem valor
corpus = tm_map(corpus,stripWhitespace) #remove excesso de espa�o em branco
corpus = tm_map(corpus,removePunctuation) # Removendo pontua��o
corpus = tm_map(corpus,removeNumber) # Remover n�meros se nao preciso deles

# Quero Criar uma n�vem de palavras e ver quais palavras s�o mais frequentes

#Nuvem de Palavras

install.packages("wordcloud")

library(wordcloud)

#Gerando Nuvem de Palavras com par�metro minha variavel corpus
#Palavras maiores tem uma frequ�ncia maior.


#random.order=T forma aleat�ria 
# colors=rainbow(8) cores diferentes
#rot.per=0.5 divide quantos em p� e deitados
#use.r.layout = T faz uma varia��o do layout

wordcloud(corpus,max.words = 100,random.order=T,colors=rainbow(8),rot.per=0.5,use.r.layout = T)