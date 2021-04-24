import tkinter as tk

from html2tk.widgets import Widget

class Input(Widget):
    def __init__(self, master, html_element, font, value=''):
        super().__init__(master, html_element)

        self.tk_widget = tk.Entry(self.master, font=font)
        self.value = value
    
    @property
    def value(self):
        return self.tk_widget.get()
    
    @value.setter
    def value(self, val):
        self.tk_widget.insert(0, val)