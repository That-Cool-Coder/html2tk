import tkinter as tk
import tkinter.ttk as ttk
import os

from bs4 import BeautifulSoup

from html2tk import widgets
from html2tk import errors
from .stylesheet import Stylesheet

class Application(widgets.Div):
    '''Create a new application using htm2tk.
    An application is just a special frame that handles window creation'''
    def __init__(self, html: str = None, html_file:str = None,
        soup:BeautifulSoup = None):
        
        # Don't run constructor of Div because it needs to be overridden

        self.stylesheet = Stylesheet()

        self.tk_widget = tk.Tk()
        self.style = self.parent_application().stylesheet['div']
        self.tk_widget.configure(background=self.style.background_color)
        self.is_windows = os.name == 'nt'
    
    def parent_application(self):
        return self
    
    def parent_tk_window(self):
        return self.tk_widget
    
    def set_stylesheet(self, stylesheet: Stylesheet):
        self.stylesheet = stylesheet
    
    def mainloop(self):
        '''Enter the main phase of the application.
        Runs mainloop() on the underlying tkinter structure'''
        self.tk_widget.mainloop()
    
    def maximize(self):
        '''Make this application fill up the whole screen'''
        if self.is_windows:
            self.tk_widget.state('zoomed')
        else:
            self.tk_widget.attributes('-zoomed', True)
        
    def set_title(self, title: str):
        '''Set the title of this application'''
        self.tk_widget.title(title)
    
    def set_background(self, color: str):
        '''Set the background color of this application'''
        self.tk_widget.configure(background=color)

    def update(self):
        '''Force the application to redraw
        by calling update() on the underlying tk structure'''
        self.tk_widget.update()
    
    def create_p_styled(self, html_soup_element):
        # A testing function that might be useful later so don't delete it
        print('Bold and italic aren\'t supported')
        return None # quit

        styling = None
        if html_soup_element.name == 'b':
            styling = 'bold'
            # If we are inside an italic, then be italic as well
            if html_soup_element.parent.name == 'i':
                styling += ' italic'
        elif html_soup_element.name == 'i':
            styling = 'italic'
            # If we are inside a bold, then be bold as well
            if html_soup_element.parent.name == 'b':
                styling += ' bold'

        if styling is not None:
            font = self.stylesheet.paragraph_font + (styling,)
            return tk.Label(self.body, text=self.get_text_from_element(html_soup_element),
                font=font)