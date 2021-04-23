import tkinter as tk

from html2tk import errors

class Widget:
    def __init__(self, master, html_element):
        self.master = master
        self.html_element = html_element

    @property
    def text(self):
        return self.widget.cget('text')
    
    @text.setter
    def text(self, text):
        self.widget.configure(text=text)

    @property
    def font(self):
        return self.widget.cget('font')
    
    @font.setter
    def font(self, font):
        self.widget.configure(font=font)
    
    def hide(self):
        self.widget.pack_forget()

    def unhide(self):
        self.widget.pack()

    def get_element_by_id(self, id:str):
        if self.html_element is None:
            raise errors.NoHtmlProvided

        html_element = self.html_element.find(id=id)
        if html_element is None:
            return None
        else:
            return html_element.widget
    
    def pack(self):
        self.widget.pack()