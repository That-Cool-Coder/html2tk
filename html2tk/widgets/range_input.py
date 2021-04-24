import tkinter as tk

from html2tk.widgets import Widget

class RangeInput(Widget):
    def __init__(self, master, html_element, min=0, max=100, step=1, value=None):
        super().__init__(master, html_element)

        if value is None:
            value = (min + max) / 2

        self.tk_widget = tk.Scale(self.master, from_=min, to=max, resolution=step,
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