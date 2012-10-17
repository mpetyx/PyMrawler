#!/usr/local/bin/python
# -*- coding: utf-8 -*-


'''
Created on 4 Jan 2012

@author: mpetyx
'''

class TextFunctions:
    
    def __init__(self, text=None):
        """
            Useful functions for handling greek text
        """
        
        if text!= None:
            self.text  = open(text,"r")
        
            self.lines = self.text.readlines()
        