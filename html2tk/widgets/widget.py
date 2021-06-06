import tkinter as tk
import tkinter.ttk as ttk

from html2tk import errors

class Widget:
    def __init__(self, master, html_element):
        # Note that master should be a tk widget (not a html2tk.widget)
        self.master = master
        self.html_element = html_element

        self.hidden = True

    @property
    def text(self):
        return self.tk_widget.cget('text')
    
    @text.setter
    def text(self, text):
        self.tk_widget.configure(text=text)
    
    def clear(self):
        self.tk_widget.children.clear()
    
    def hide(self):
        self.hidden = True
        self.tk_widget.pack_forget()

    def show(self):
        self.hidden = False
        self.tk_widget.pack()

    def get_element_by_id(self, id:str):
        if self.html_element is None:
            raise errors.NoHtmlProvided

        html_element = self.html_element.find(id=id)
        if html_element is None:
            return None
        else:
            return html_element.widget
    
    def get_text_from_element(self, element):
        if element.text is None:
            return ''
        else:
            return ''.join(element.find_all(text=True, recursive=False)).strip()
    
    def pack(self):
        self.tk_widget.pack()