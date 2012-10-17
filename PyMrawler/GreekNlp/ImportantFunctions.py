'''
Created on 11 Dec 2011

@author: mpetyx
'''

import nltk

class Function:
    
    def lexical_diversity(self, my_text):
        
        word_count= len(my_text)
        print "exeis "+str(word_count)+" lekseis"
        vocab_size= len(set(my_text))
        print "exeis "+str(vocab_size)+" megethos leksikou"
        return word_count/vocab_size
    
    def unusual_words(self, text):
        text_vocab=set(w.lower() for w in text if w.isalpha())
        english_vocab=set(w.lower() for w in nltk.corpus.words.words())
        unusual=text_vocab.difference(english_vocab)
        return sorted(unusual)
    
    def distribution(self, text):
        from nltk import FreqDist
        fdist = FreqDist(text)
        return fdist.keys()
    
    def collocations(self, text):
        return text.collocations()
    
    def text(self):
        f = open('test')
        raw = f.read()
        tokens = nltk.word_tokenize(raw)
        print tokens
        return tokens
    
    def greek_tokenize(self, text):
        tokenizer = nltk.data.load('tokenizers/punkt/greek.pickle')
        tokens = tokenizer.tokenize(text)#unicode(text,'utf-8').encode('utf-8'))
        #print nltk.pos_tag(tokens)
        print len(tokens)
        return tokens