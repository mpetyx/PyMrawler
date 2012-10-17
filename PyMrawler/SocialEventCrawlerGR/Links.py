'''
Created on 11 Dec 2011

@author: mpetyx
'''

class Link:
    
    def __init__(self,text):
        """
            Here we search all the links included in the description
        """
        
        self.links = None
        from TextHandling import TextFunctions
        
        self.text = TextFunctions(text)
        self.lines = self.text.lines
        self.words = []
        
        
    def links(self):
        import re
        # parsing addresses
        # http://stackoverflow.com/questions/6173/regular-expression-for-parsing-links-from-a-webpage
        self.links = re.findall(r'\b(https?|ftp|file)://[-A-Z0-9+&@#/%?=~_|!:,.;]*[-A-Z0-9+&@#/%=~_|]',self.text)
        
    def youtube(self):
        self.youtubeLinks = []
        for link in self.links:
            if "youtube" in link:
                self.youtubeLinks.append(link)
        return self.youtubeLinks
    
    def parse_url(self):
            e=r'/((http|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+\.[^#?\s]+)(#[\w\-]+)?/'
            e2=r'/^((http|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+\.[^#?\s]+)(#[\w\-]+)?$/'
            
    def simple_parse(self):
        
        for line in self.lines:
            if "www" in line:
                print line

                                                                        