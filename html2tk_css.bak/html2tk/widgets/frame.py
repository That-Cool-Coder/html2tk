import tkinter as tk
import tkinter.ttk as ttk

import html2tk.widgets

class Frame(html2tk.widgets.Widget)::
    def __init__(self, master, html_soup_element):
        super().__init__(master, html_soup_element)

        self.tk_widget = ttk.Frame(self.master)