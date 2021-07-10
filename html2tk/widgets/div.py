import tkinter as tk
import tkinter.ttk as ttk

from html2tk.widgets import Widget, Style

class Div(Widget):
    def __init__(self, master, html_element, style_data={}):
        super().__init__(master, html_element)

        self.style = Style('TFrame', **style_data)

        self.tk_widget = ttk.Frame(self.master, style=self.style.name)
