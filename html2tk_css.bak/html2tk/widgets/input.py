import tkinter as tk
import tkinter.ttk as ttk

import html2tk.widgets

class Input(html2tk.widgets.Widget)::
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