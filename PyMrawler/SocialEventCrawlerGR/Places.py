#!/usr/local/bin/python
# -*- coding: utf-8 -*-

'''
Created on 7 Dec 2011

@author: mpetyx
'''

class Place:
    
    def __init__(self, text):
        """
            The main idea is to search the database and find places already there into the text
            That could be slow, so i need a copy of the places in one accessible database like gae
        
            The similar result is mostly at the same sentence.
            Some times is either at the top or bottom line!
        """
        
        self.text = text
        
    def load(self):
        
        self.places = [] # Here we load the places from the database
        
        
    def place(self):
        return 1