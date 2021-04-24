import tkinter as tk

from .widget import Widget

class Frame(Widget):
    def __init__(self, master, html_element):
        super().__init__(master, html_element)

        self.tk_widget = tk.Frame(self.master)