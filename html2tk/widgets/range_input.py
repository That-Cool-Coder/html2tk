import tkinter as tk
import tkinter.ttk as ttk

from bs4 import BeautifulSoup

from html2tk.widgets import Widget
from html2tk.widgets import WidgetName

class RangeInput(Widget):
    '''A widget representing the HTML <input type="range"> element'''
    def __init__(self, master: Widget, html_soup_element: BeautifulSoup):
        super().__init__(master, html_soup_element)

        min = int(html_soup_element.attrs.get('min', 0))
        max = int(html_soup_element.attrs.get('max', 100))
        self.increment = int(html_soup_element.attrs.get('increment', 1))
        value = int(html_soup_element.attrs.get('value', (min + max) / 2))

        print('Note that range inputs don\'t have styling yet')
        self.tk_widget = ttk.Scale(self.master.tk_widget, from_=min, to=max,
            orient=tk.HORIZONTAL)
        self.value = value

    @property
    def value(self):
        return self.tk_widget.get()
    
    @value.setter
    def value(self, val):
        self.tk_widget.set(val)
    
    @property
    def min(self):
        return self.tk_widget.cget('from')
    
    @min.setter
    def min(self, val):
        self.tk_widget.configure(from_=val)
    
    @property
    def max(self):
        return self.tk_widget.cget('to')
    
    @max.setter
    def max(self, val):
        self.tk_widget.configure(to=val)