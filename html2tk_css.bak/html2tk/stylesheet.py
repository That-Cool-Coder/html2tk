import tkinter as tk
import tkinter.ttk as ttk

import cssutils

from html2tk import errors

class Stylesheet:
    # This allows us to create unique ttk style names
    ttk_style_count = 0

    def __init__(self, css:str=None, source_file_name:str=None):
        if css is None and source_file_name is None:
            raise errors.NoHtmlProvided
        elif source_file_name is not None:
            try:
                file = open(source_file_name, 'r', encoding='utf-8')
                css = file.read()
            finally:
                file.close()
        
        self.rules = cssutils.parseString(css)

        self.create_ttk_styles()
    
    def create_ttk_styles(self):
        self.ttk_styles = {}
        for rule in self.rules:
            class_name = rule.selectorText
            ttk_style_name ='html2tk-' + str(self.__class__.ttk_style_count) + '.TLabel'
            ttk_style = ttk.Style()
            for prop in rule.style:
                if prop.name == 'background-color':
                    ttk_style.configure(ttk_style_name, background=prop.value)
                elif prop.name == 'color':
                    ttk_style.configure(ttk_style_name, foreground=prop.value)
                elif prop.name == 'font-size':
                    ttk_style.configure(ttk_style_name, font=('helvetica', int(prop.value)))
            self.ttk_styles[class_name] = ttk_style_name

'''
tinycss2 version:
class Stylesheet:
    def __init__(self, css:str=None, source_file_name:str=None):
        if css is None and source_file_name is None:
            raise errors.NoHtmlProvided
        elif source_file_name is not None:
            try:
                file = open(source_file_name, 'r', encoding='utf-8')
                css = file.read()
            finally:
                file.close()
        
        self.rules = tinycss2.parse_stylesheet(css, skip_comments=True,
            skip_whitespace=True)

        self.create_ttk_styles()
    
    def create_ttk_styles(self):
        self.ttk_styles = []
        print('create_ttk')
        for rule in self.rules:
            class_name = rule.prelude[0]
            declaration_list = tinycss2.parse_declaration_list(rule.content)
            attributes = {}
            for declaration in declaration_list:
                if type(declaration) != tinycss2.ast.Declaration:
                    continue
                for token in declaration.value:
                    print(token.value)

'''


''' Old (pre-css) stylesheet:
class Stylesheet:
    def __init__(self, paragraph_font:tuple, heading_font:tuple, button_font:tuple, input_font:tuple):
        self.paragraph_font = paragraph_font
        self.heading_font = heading_font
        self.button_font = button_font
        self.input_font = input_font
'''