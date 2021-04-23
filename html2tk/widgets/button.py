import tkinter as tk

from html2tk.widgets import Widget

class Button(Widget):
    def __init__(self, master, html_element, text, font):
        super().__init__(master, html_element)

        self.widget = tk.Button(self.master, text=text, font=font)

    @property
    def command(self):
        return self.widget.cget('command')

    @command.setter
    def command(self, callback):
        self.widget.configure(command=callback)