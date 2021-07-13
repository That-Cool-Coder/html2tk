import tkinter as tk
import tkinter.ttk as ttk

from bs4 import BeautifulSoup

from html2tk.widgets import Widget
from html2tk.widgets import WidgetName

class LineBreak(Widget):
    def __init__(self, master: Widget, html_soup_element: BeautifulSoup):
        super().__init__(master, html_soup_element)

        self.style = self.parent_application().stylesheet[WidgetName.LINE_BREAK]
        self.tk_widget = ttk.Label(self.master.tk_widget, style=self.style.name)