import tkinter as tk
import tkinter.ttk as ttk

from bs4 import BeautifulSoup

from html2tk import widgets
from html2tk.widgets import WidgetName

class Div(widgets.Widget):
    def __init__(self, master: widgets.Widget, html_soup_element: BeautifulSoup):
        super().__init__(master, html_soup_element)

        self.style = self.parent_application().stylesheet[WidgetName.DIV]
        self.tk_widget = ttk.Frame(self.master, style=self.style.name)

    def add_html_file(self, file_name: str):
        '''Open file_name and read its contents as HTML.
        Create elements from the HTML and append them to this widget'''
        if file_name is not None:
            file = None
            try:
                file = open(file_name, 'r', encoding='utf-8')
                html = file.read()
                self.add_html(html)
            finally:
                if file is not None:
                    file.close()

    def add_html(self, html: str):
        '''Create elements from html and append them to this widget'''
        html_soup_element = BeautifulSoup(html, 'html.parser')
        self.add_soup(html_soup_element)

    def add_soup(self, soup: BeautifulSoup):
        '''Create elements from soup and append them to this widget'''
        self.html_soup_element = soup

        title_element = self.html_soup_element.find('title')
        if title_element is not None:
            self.parent_application().set_title(title_element.get_text())

        for html_soup_element in self.html_soup_element.recursiveChildGenerator():
            widget = None

            widget = self.create_widget_from_soup_element(html_soup_element)

            if widget is not None:
                widget.pack()

                if html_soup_element.has_attr('hidden'):
                    widget.hide()

                html_soup_element.widget = widget
    
    def create_widget_from_soup_element(self, html_soup_element: BeautifulSoup):
        parent = html_soup_element.parent.widget
        if parent is None:
            html_soup_element.parent.widget = self.parent_application()
            parent = self.parent_application()

        widget = None
        if html_soup_element.name == 'div':
            widget = Div(parent, html_soup_element)
        if html_soup_element.name == 'br':
            widget = widgets.LineBreak(parent, html_soup_element)
        elif html_soup_element.name == 'p':
            widget = widgets.Paragraph(parent, html_soup_element)
        elif html_soup_element.name == 'h1':
            widget = widgets.Heading(parent, html_soup_element)
        elif html_soup_element.name == 'h2':
            widget = widgets.Heading(parent, html_soup_element)
        elif html_soup_element.name == 'button':
            widget = widgets.Button(parent, html_soup_element)
        elif html_soup_element.name == 'input':
            input_type = html_soup_element.attrs.get('type', None)
            if input_type == 'range':
                widget = widgets.RangeInput(parent, html_soup_element)
            elif input_type == 'checkbox':
                widget = widgets.CheckboxInput(parent, html_soup_element)
            elif input_type == 'color':
                widget = widgets.ColorInput(parent, html_soup_element)
            else:
                widget = widgets.Input(parent, html_soup_element)
        elif html_soup_element.name == 'select':
            widget = widgets.Select(parent, html_soup_element)
        return widget