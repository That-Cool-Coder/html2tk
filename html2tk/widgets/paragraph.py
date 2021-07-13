import tkinter as tk
import tkinter.ttk as ttk

from bs4 import BeautifulSoup

from html2tk.widgets import Widget
from html2tk.widgets import WidgetName

class Paragraph(Widget):
    def __init__(self, master: Widget, html_soup_element: BeautifulSoup):
        super().__init__(master, html_soup_element)

        text = self.get_text_from_element(html_soup_element)
        self.style = self.parent_application().stylesheet[WidgetName.PARAGRAPH]
        self.tk_widget = ttk.Label(self.master.tk_widget, text=text,
            style=self.style.name)