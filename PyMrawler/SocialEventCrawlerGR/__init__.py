'''
Created on 7 Dec 2011

@author: mpetyx
'''

from Days import Date
from GeneralDescription import Description,Category
from Pics import Photographs
from Places import Place
from Tickets import Ticket
from Title import Title
from Links import Link

class artAndLife:
    
    def __init__(self, text=None):
        """
            
        """
        self.text = text
        if self.text != None:
            self.f = open(self.text,"r")
            
    def fileInit(self, text):
        self.text = text
        if self.text != None:
            self.f = open(self.text,"r")
            
    def Day(self):
        return Date(self.f).day
    
    def Title(self):
        return Title(self.f).title
    
    def Place(self):
        return Place(self.f).place
    
    def Description(self):
        return Description(self.f).description
    
    def Category(self):
        return Description(self.f).category
    
    def Ticket(self):
        return Ticket(self.f).ticket
    
    def Photographs(self):
        return Photographs(self.f).photographs
    
    def Links(self):
        return Links(self.f).links
    
    def youtube(self):
        return Links(self.f).youtube()