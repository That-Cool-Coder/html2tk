import tkinter as tk
import tkinter.ttk as ttk

import html2tk.errors

class Widget:
    def __init__(self, master, html_soup_element):
        # Note that master should be a tk widget (not a html2tk.widget)
        self.master = master
        self.html_soup_element = html_soup_element

    @property
    def text(self):
        return self.tk_widget.cget('text')
    
    @text.setter
    def text(self, text):
        self.tk_widget.configure(text=text)

    @property
    def font(self):
        return self.tk_widget.cget('font')
    
    @font.setter
    def font(self, font):
        self.tk_widget.configure(font=font)
    
    def clear(self):
        self.tk_widget.children.clear()
    
    def hide(self):
        self.tk_widget.pack_forget()

    def unhide(self):
        self.tk_widget.pack()

    def get_element_by_id(self, id:str):
        if self.html_soup_element is None:
            raise html2tk.errors.NoHtmlProvided

        html_soup_element = self.html_soup_element.find(id=id)
        if html_soup_element is None:
            return None
        else:
            return html_soup_element.widget
    
    def get_text_from_element(self, element):
        if element.text is None:
            return ''
        else:
            return ''.join(element.find_all(text=True, recursive=False)).strip()
    
    def pack(self):
        self.tk_widget.pack()