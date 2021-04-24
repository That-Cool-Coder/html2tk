import tkinter as tk

from html2tk.widgets import Widget

class Label(Widget):
    def __init__(self, master, html_element, text, font):
        super().__init__(master, html_element)

        self.tk_widget = tk.Label(self.master, text=text, font=font)