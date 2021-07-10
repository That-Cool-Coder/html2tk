import tkinter as tk
import tkinter.ttk as ttk

import html2tk.widgets

class RangeInput(html2tk.widgets.Widget)::
    def __init__(self, master, html_soup_element):
        super().__init__(master, html_soup_element)

        min = int(html_soup_element.attrs.get('min', 0))
        max = int(html_soup_element.attrs.get('max', 100))
        self.increment = int(html_soup_element.attrs.get('increment', 1))
        value = int(html_soup_element.attrs.get('value', (min + max) / 2))

        self.tk_widget = ttk.Scale(self.master, from_=min, to=max,
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