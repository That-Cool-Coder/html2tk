import tkinter as tk
import tkinter.ttk as ttk

from html2tk.widgets import Widget

class Paragraph(Widget):
    def __init__(self, master, html_element, stylesheet):
        super().__init__(master, html_element)

        text = self.get_text_from_element(html_element)

        class_name = html_element.attrs.get('class', None)[0]
        print(class_name)
        ttk_style = stylesheet.ttk_styles[class_name]
        self.tk_widget = ttk.Label(self.master, text=text, style=ttk_style)