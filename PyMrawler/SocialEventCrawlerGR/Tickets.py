#!/usr/local/bin/python
# -*- coding: utf-8 -*-

'''
Created on 7 Dec 2011

@author: mpetyx
'''

class Ticket:
    
    def __init__(self, text):
        """
        
        The similar result is mostly at the same sentence.
        Some times is either at the top or bottom line!
            
        """
        from TextHandling import TextFunctions
        
        self.text = TextFunctions(text)
        self.lines = self.text.lines
        self.words = []
        
        
    def propolisi(self):
        
        self.words = self.words+["ΠΡΟΠΩΛΗΣΗ","προπώληση","προπωληση"]
        
        
    def value(self):
        
        self.words = self.words+['€','euro','ευρώ',"ευρω","κόστο","κοστο",]
        
    def where_to_buy(self):
        
        self.words = self.words+["ΠΡΟΠΩΛΗΣΗ","προπώληση","προπωληση"]
        
    def searching_PRICES(self):
        
        self.value()
        self.propolisi()
        
        results = []
        
        for d in self.words:
            for line in self.lines:
                if d in line.decode('utf-8').lower():
                    results.append(line)
                    
        if results!=[]:
            result = results[0]
#            for res in results:
#                if result!=res:
#                    print "opa"
        return result