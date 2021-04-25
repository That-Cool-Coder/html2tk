import tkinter as tk
import tkinter.ttk as ttk

from html2tk.widgets import Widget

class Paragraph(Widget):
    def __init__(self, master, html_element, font):
        super().__init__(master, html_element)

        text = self.get_text_from_element(html_element)

        self.tk_widget = ttk.Label(self.master, text=text, font=font)