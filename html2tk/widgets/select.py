import tkinter as tk

from html2tk.widgets import Widget

class Select(Widget):
    def __init__(self, master, html_element):
        super().__init__(master, html_element)

        options = []
        for child in html_element.children:
            if child.name is not None:
                options.append(child.value)

        self.tk_stringvar = tk.StringVar(None, value='')
        self.tk_widget = tk.OptionMenu(self.master, self.tk_stringvar, '', *options)
        #self.value = value
    
    @property
    def value(self):
        return self.tk_stringvar.get()
    
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