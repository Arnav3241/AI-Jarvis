from nltk.stem.porter import PorterStemmer
import numpy as np
import nltk

Stemmer = PorterStemmer()

def Tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return Stemmer.stem(word.lower())

def bagOfWords(TokenizedSentence, words):
    sentence_words = [stem(word) for word in TokenizedSentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag