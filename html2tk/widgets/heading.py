import tkinter as tk
import tkinter.ttk as ttk

from bs4 import BeautifulSoup

from html2tk.widgets import Widget

class Heading(Widget):
    def __init__(self, master: Widget, html_soup_element: BeautifulSoup):
        super().__init__(master, html_soup_element)

        text = self.get_text_from_element(html_soup_element)

        elem_name = self.html_soup_element.name
        if elem_name == 'h1':
            style_name = 'heading1'
        elif elem_name == 'h2':
            style_name = 'heading2'
        else:
            style_name = 'heading1'

        self.style = self.parent_application().stylesheet[style_name]

        self.tk_widget = ttk.Label(self.master.tk_widget, text=text, style=self.style.name)
