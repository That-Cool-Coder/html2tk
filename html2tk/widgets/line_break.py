import tkinter as tk

from .widget import Widget

class LineBreak(Widget):
    def __init__(self, master, html_element):
        super().__init__(master, html_element)

        self.tk_widget = tk.Label(self.master)