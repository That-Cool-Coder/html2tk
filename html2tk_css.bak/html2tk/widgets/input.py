import tkinter as tk
import tkinter.ttk as ttk

from html2tk.widgets import Widget

class Input(Widget):
    def __init__(self, master, html_element, font):
        super().__init__(master, html_element)

        value = html_element.attrs.get('value', '')

        self.tk_widget = ttk.Entry(self.master, font=font)
        self.value = value
    
    @property
    def value(self):
        return self.tk_widget.get()
    
    @value.setter
    def value(self, val):
        self.tk_widget.insert(0, val)