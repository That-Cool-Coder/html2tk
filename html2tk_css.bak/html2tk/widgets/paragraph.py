import tkinter as tk
import tkinter.ttk as ttk

import html2tk.widgets

class Paragraph(html2tk.widgets.Widget)::
    def __init__(self, master, html_soup_element, stylesheet):
        super().__init__(master, html_soup_element)

        text = self.get_text_from_element(html_soup_element)

        class_name = html_soup_element.attrs.get('class', None)[0]
        print(class_name)
        ttk_style = stylesheet.ttk_styles[class_name]
        self.tk_widget = ttk.Label(self.master, text=text, style=ttk_style)