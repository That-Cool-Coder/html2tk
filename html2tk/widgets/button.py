import tkinter as tk
import tkinter.ttk as ttk

from html2tk.widgets import Widget

class Button(Widget):
    def __init__(self, master, html_element, font):
        super().__init__(master, html_element)
        
        text = self.get_text_from_element(html_element)

        style_name = self.create_unique_ttk_style_name('TButton')
        style = ttk.Style(self.master)
        style.configure(style_name, font=font)
        self.tk_widget = ttk.Button(self.master, text=text, style=style_name)

    @property
    def command(self):
        return self.tk_widget.cget('command')

    @command.setter
    def command(self, callback):
        self.tk_widget.configure(command=callback)