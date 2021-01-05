# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:13:53 2020

@author: rodri
"""

import matplotlib.pyplot as plt
import nltk # Linguagem natual 
#nltk.download() # primeira vez que for utilizar nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from matplotlib.colors import ListedColormap
from wordcloud import WordCloud # deve ser exatamente com os caracteres ao lado WordCloud

# .* todas as extensões de arquivo
corpus = PlaintextCorpusReader('dados','.*')

# Nuvem de palavras para observar quais aparecem mais.
todo_texto = corpus.raw()


# Variável com palavras sem valor semântico que quero tirar 
stops = stopwords.words('english')
# Variável com as cores que quero preencher na nuvem de palavras
mapa_cores = ListedColormap(['orange','green','red','magenta'])


# Criando a nuvem

nuvem = WordCloud(background_color='white',colormap = mapa_cores,stopwords=stops, max_words = 100)


# Gerar nuvem com dados que quero, ele já ira retirar o stopwords

nuvem.generate(todo_texto)

#Plotar imagem 
plt.imshow(nuvem)