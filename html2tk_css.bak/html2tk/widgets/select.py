import tkinter as tk
import tkinter.ttk as ttk

import html2tk.widgets

class Select(html2tk.widgets.Widget)::
    def __init__(self, master, html_element):
        super().__init__(master, html_element)

        options = []
        for child in html_element.children:
            if child.name is not None:
                options.append(child.attrs.get('value'))
        
        value = html_element.attrs.get('value', None)

        if value is None and len(options) > 0:
            value = options[0]
        else:
            value = ''

        self.tk_stringvar = tk.StringVar(self.master, value)
        self.tk_widget = ttk.OptionMenu(self.master, self.tk_stringvar, None, *options)
        self.value = value
    
    @property
    def value(self):
        return self.tk_stringvar.get()
    
    @value.setter
    def value(self, val):
        self.tk_stringvar.set(val)