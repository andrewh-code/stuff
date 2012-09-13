#!/usr/bin/python

import urllib

class get_page:
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def get_page(url):
        try:
            return urllib.urlopen(url).read()
        except:
            return ""