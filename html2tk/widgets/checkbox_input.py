import tkinter as tk
import tkinter.ttk as ttk

from bs4 import BeautifulSoup

from html2tk.widgets import Widget
from html2tk.widgets import WidgetName

class CheckboxInput(Widget):
    '''A widget representing HTML <input type="checkbox">'''
    def __init__(self, master: Widget, html_soup_element: BeautifulSoup):
        super().__init__(master, html_soup_element)

        self.tk_intvar = tk.IntVar()
        self.style = self.parent_application().stylesheet[WidgetName.CHECKBOX_INPUT]
        self.tk_widget = ttk.Checkbutton(self.master.tk_widget, variable=self.tk_intvar,
            command=self.update_checked, style=self.style.name)
        
        if self.html_soup_element.has_attr('checked'):
            self.tk_intvar.set(1)

        self.update_checked()
    
    def update_checked(self, event=None):
        self.checked = bool(self.tk_intvar.get())
    
    