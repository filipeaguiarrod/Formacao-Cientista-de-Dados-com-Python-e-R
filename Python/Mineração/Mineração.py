# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:55:10 2020

@author: rodri
"""

import matplotlib.pyplot as plt
import nltk # Linguagem natual 

#nltk.download() # primeira vez que for utilizar nltk

from nltk.corpus import PlaintextCorpusReader


# .* todas as extensões de arquivo
corpus = PlaintextCorpusReader('dados','.*')

# Visualizar se todos arquivos estão armazenados em corpus

arquivos = corpus.fileids()

# Caso queira acessar texto de um arquivo específico

texto=corpus.raw('1.txt')

# Todos textos em todos arquivos

todo_texto=corpus.raw()

# palavras 

palavras = corpus.words()

palavras