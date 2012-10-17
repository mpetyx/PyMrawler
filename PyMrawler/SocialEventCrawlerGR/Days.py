#!/usr/local/bin/python
# -*- coding: utf-8 -*-

'''
Created on 7 Dec 2011

@author: mpetyx
'''

class Date:
    
    def __init__(self, text=None):
        
        from TextHandling import TextFunctions
        
        """
            Here we look for the day of the event
            
            The similar result is mostly at the same sentence.
            Some times is either at the top or bottom line!
        """
        
        self.text = TextFunctions(text)
        self.lines = self.text.lines
        
    def week_days(self):
        
        days = ['δευτέρα','δευτερα','τρίτη','τριτη','τετάρτη','τεταρτη','πέμπτη','πεμπτη','παρασκευή','παρασκευη','σάββατο','σαββατο','κυριακή','κυριακη']
        
        return days
        
    def months(self):
        
        monthNames = ['ιανουάριο','ιανουάριο','φεβρουάριο','φεβρουαριο','μάρτιο','μαρτιο','απρίλιο','απριλιο','μαιο','μάιο','ιουνιο','ιούνιο','ιούλιο','ιουλιο','αύγουστο','αυγουστο','σεπτέμβριο','σεπτεμβριο','οκτώβριο','οκτωβριο','νοέμβριο','νοεμβριο','δεκέμβριο','δεκεμβριο']
        
        return monthNames
    
    def month_number(self, month):
        
        m_number = 0
        months = self.months()
        while m_number<len(months):
            if months[m_number] in month:
                break
            m_number = m_number + 1
            
        m_number = m_number + 1
        if m_number%2==0:
            final = m_number/2
        else:
            final  =m_number/2 + 1
        
        return final
    
    def current_year(self):
        
        return 1
    
    def date_format(self, text):
        import re
        
        temp = re.findall(u'^(0[1-9]|[12][0-9]|3[01])[- /.]([1-9]|1[012])[- /.](19|20)\d\d$',"19/4-2011")
        print temp
        
    def current_time(self):
        
        import datetime
        
        today = datetime.date.today()
        self.month = today.month
        self.day = today.day
        self.year = today.year
        
    def searching_DATE(self):
        
        month = ""
        day   = ""
        for d in self.months():
            for line in self.lines:
                if d in line.decode('utf-8').lower():
                    month= line
                    
                
        for d in self.week_days():
            for line in self.lines:
                if d in line.decode('utf-8').lower():
                    print line
                    day= line
                    
        print day
        print month
        
#example =  "Λεω να παω να δω την παρασκευή καμια συναυλια! Τι λες εσυ? Ναι ψήσου να πάμε τον απρίλιο"

#day = Date()
#day.month_number("ιανουάριο")