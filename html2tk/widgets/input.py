import tkinter as tk
import tkinter.ttk as ttk

from bs4 import BeautifulSoup

from html2tk.widgets import Widget

class Input(Widget):
    '''A widget representing the html <input> element'''
    def __init__(self, master: Widget, html_soup_element: BeautifulSoup):
        super().__init__(master, html_soup_element)

        value = html_soup_element.attrs.get('value', '')
        placeholder = html_soup_element.attrs.get('placeholder', '')

        self.tk_widget = ttk.Entry(self.master.tk_widget)
        self.value = value

        self.showing_placeholder = False
        self.placeholder = placeholder
        self.tk_widget.bind('<KeyPress>', self.try_hide_placeholder)
        self.tk_widget.bind('<KeyRelease>', self.try_show_placeholder)
        self.try_show_placeholder()
    
    def try_show_placeholder(self, event=None):
        if self.value == '':
            self.showing_placeholder = True
            self.value = self.placeholder

    def try_hide_placeholder(self, event=None):
        if self.showing_placeholder and self.value != '':
            self.value = ''
            self.showing_placeholder = False
    
    @property
    def value(self):
        '''The value that a user has typed into this widget'''
        return self.tk_widget.get()
    
    @value.setter
    def value(self, val):
        '''The value that a user has typed into this widget'''
        self.tk_widget.delete(0, 'end')
        self.tk_widget.insert(0, val)