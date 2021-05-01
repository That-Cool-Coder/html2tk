import tkinter as tk
import tkinter.ttk as ttk

import html2tk.widgets

class LineBreak(html2tk.widgets.Widget)::
    def __init__(self, master, html_element):
        super().__init__(master, html_element)

        self.tk_widget = ttk.Label(self.master)