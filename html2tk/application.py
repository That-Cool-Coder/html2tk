import tkinter as tk

from bs4 import BeautifulSoup

from html2tk import widgets
from html2tk import errors

class Application(widgets.Widget):
    def __init__(self, master=None, html=None, source_file_path=None,
            stylesheet=None):

        if master is None:
            self.master = tk.Tk()
        else:
            self.master = master

        self.body = widgets.Frame(self.master, None)
        self.body.pack()

        if source_file_path is not None or html is not None:
            self.load_html(html=html, source_file_path=source_file_path)
        else:
            self.html_element = None
        
        if stylesheet is not None:
            self.apply_stylesheet(stylesheet)
        else:
            self.stylesheet = None
    
    def mainloop(self):
        self.master.mainloop()
        
    def update(self):
        self.body.tk_widget.winfo_toplevel().update()
    
    def load_html(self, html=None, source_file_path=None):
        if source_file_path is not None:
            file = None
            try:
                file = open(source_file_path, 'r')
                html = file.read()
            finally:
                if file is not None:
                    file.close()

        elif html is None and source_file_path is None:
            raise errors.NoHtmlProvided

        self.html_element = BeautifulSoup(html, 'html.parser')

    def apply_stylesheet(self, stylesheet):
        self.stylesheet = stylesheet
    
    def populate_body(self):
        if self.html_element is None:
            raise errors.NoHtmlProvided

        self.body.clear()

        for html_element in self.html_element.recursiveChildGenerator():
            widget = None

            parent = html_element.parent.widget
            if parent is None:
                html_element.parent.widget = self.body
                parent = self.body

            if html_element.name == 'div':
                widget = widgets.Frame(parent.tk_widget, html_element)
            if html_element.name == 'br':
                widget = widgets.LineBreak(parent.tk_widget, html_element)
            elif html_element.name == 'p':
                widget = widgets.Paragraph(parent.tk_widget, html_element,
                    self.get_text_from_element(html_element),
                    self.stylesheet.paragraph_font)
            elif html_element.name == 'h1':
                widget = widgets.Paragraph(parent.tk_widget, html_element,
                    self.get_text_from_element(html_element),
                    self.stylesheet.heading_font)
            elif html_element.name == 'button':
                widget = widgets.Button(parent.tk_widget, html_element,
                    self.get_text_from_element(html_element),
                    self.stylesheet.button_font)
            elif html_element.name == 'input':
                input_type = html_element.attrs.get('type', None)
                if input_type == 'range':
                    widget = widgets.RangeInput(parent.tk_widget, html_element,
                        int(html_element.attrs.get('min', 0)),
                        int(html_element.attrs.get('max', 100)),
                        int(html_element.attrs.get('step', 1)))
                else:
                    widget = widgets.Input(parent.tk_widget, html_element,
                        self.stylesheet.input_font)

            if widget is not None:
                widget.pack()

                if html_element.has_attr('hidden'):
                    widget.hide()

                html_element.widget = widget
    
    def create_p_styled(self, html_element):
        print('Bold and italic aren\'t supported')
        return None # quit

        styling = None
        if html_element.name == 'b':
            styling = 'bold'
            # If we are inside an italic, then be italic as well
            if html_element.parent.name == 'i':
                styling += ' italic'
        elif html_element.name == 'i':
            styling = 'italic'
            # If we are inside a bold, then be bold as well
            if html_element.parent.name == 'b':
                styling += ' bold'

        if styling is not None:
            font = self.stylesheet.paragraph_font + (styling,)
            return tk.Label(self.body, text=self.get_text_from_element(html_element),
                font=font)

    def get_text_from_element(self, element):
        if element.text is None:
            return ''
        else:
            return ''.join(element.find_all(text=True, recursive=False)).strip()