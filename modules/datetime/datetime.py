# datetime.py
# Author: Sébastien Combéfis
# Version: May 25, 2016

from bottle import template

from modules.module import Module

class DateTime(Module):
    '''Class representing a module that shows current date and time.'''
    def __init__(self):
        super().__init__('datetime')

    def widget(self):
        return None
        
    def page(self):
        return None
