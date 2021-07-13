import tkinter as tk
import tkinter.ttk as ttk

from bs4 import BeautifulSoup

from html2tk.widgets import Widget
from html2tk.widgets import WidgetName

class Button(Widget):
    def __init__(self, master: Widget, html_soup_element: BeautifulSoup):
        super().__init__(master, html_soup_element)
        
        text = self.get_text_from_element(html_soup_element)
        self.style = self.parent_application().stylesheet[WidgetName.BUTTON]
        self.tk_widget = ttk.Button(self.master.tk_widget,
            text=text, style=self.style.name)

    @property
    def command(self):
        '''A function to be run when the button is clicked'''
        return self.tk_widget.cget('command')

    @command.setter
    def command(self, callback):
        '''A function to be run when the button is clicked'''
        self.tk_widget.configure(command=callback)

'''
from .widget import Widget

class Button(Widget):
    def __init__(self, master, html_soup_element, font):
        super().__init__(master, html_soup_element)
        
        text = self.get_text_from_element(html_soup_element)

        self.style = Style('TButton', **style_data)

        self.tk_widget = ttk.Button(self.master, text=text, style=self.style.name)

    @property
    def command(self):
        return self.tk_widget.cget('command')

    @command.setter
    def command(self, callback):
        self.tk_widget.configure(command=callback)
'''