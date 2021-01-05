# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 15:12:32 2020

@author: rodri
"""

import matplotlib.pyplot as plt
import nltk # Linguagem natual 
#nltk.download() # primeira vez que for utilizar nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from matplotlib.colors import ListedColormap
from wordcloud import WordCloud # deve ser exatamente com os caracteres ao lado WordCloud
import string

# .* todas as extensões de arquivo
corpus = PlaintextCorpusReader('dados','.*')


# Variável com palavras sem valor semântico que quero tirar 
stops = stopwords.words('english')


# Todas palavras do corpus

palavras = corpus.words()
len(palavras)


###################### Pré Processamento - Limpeza de dados

# Vou criar palavras só que sem a stopwords

palavras_semstop = [ p for p in palavras if p not in stops]

len(palavras_semstop)

# Quero eleminar caracteres:

string.punctuation

palavras_sem_pont = [p  for p in palavras_semstop if p not in string.punctuation ]

len(palavras_sem_pont)



######################## Gerar termos frequentes

freq = nltk.FreqDist(palavras_sem_pont)

# Ranking com 100 palavras mais comuns

mais_comuns = freq.most_common(100)