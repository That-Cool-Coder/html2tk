import tkinter as tk
import tkinter.ttk as ttk
import os

from bs4 import BeautifulSoup

from html2tk import errors

class Widget:
    '''Base class of html2tk
    Handles loading and parsing HTML, interfaces with tk,
    and provides some utilities.
    '''

    def __init__(self, master, html_soup_element: BeautifulSoup):

        self.master = master
        self.html_soup_element = html_soup_element
        self.is_windows = os.name == 'nt'
        self.tk_widget = None

        self.hidden = True

    @property
    def text(self):
        '''The text inside of the widget'''
        return self.tk_widget.cget('text')
    
    @text.setter
    def text(self, text):
        '''The text inside of the widget'''
        self.tk_widget.configure(text=text)
<<<<<<< HEAD
    
    def parent_tk_window(self):
        '''Find the tkinter window which contains this widget'''
        return self.tk_widget.winfo_toplevel()
=======
>>>>>>> fa69abf4e3701e6adcd1b1f342b475016c52368b
    
    def parent_application(self):
        '''Find the html2tk.Application which contains this widget'''
        return self.master.parent_application()

    def clear(self):
        '''Remove all children from this widget'''
        self.tk_widget.children.clear()
    
    def hide(self):
<<<<<<< HEAD
        '''Make the widget no longer visible and no longer take up space'''
        self.tk_widget.pack_forget()

    def unhide(self):
        '''Make the widget visible.
        Note that this is functionally identical to pack()'''
=======
        self.hidden = True
        self.tk_widget.pack_forget()

    def show(self):
        self.hidden = False
>>>>>>> fa69abf4e3701e6adcd1b1f342b475016c52368b
        self.tk_widget.pack()

    def get_element_by_id(self, id:str):
        '''Find the element contained by this that has id.
        Returns None if no widget is found'''

        html_soup_element = self.html_soup_element.find(id=id)
        if html_soup_element is None:
            return None
        else:
            return html_soup_element.widget
    
    def get_text_from_element(self, element):
        '''Get the text from inside a BeautifulSoup element'''
        if element.text is None:
            return ''
        else:
            return ''.join(element.find_all(text=True, recursive=False)).strip()
    
    def pack(self):
        '''Make the widget show up on screen initially.
        Note that this is functionally identical to unhide()'''
        self.tk_widget.pack()