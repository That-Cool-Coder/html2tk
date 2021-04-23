import tkinter as tk

from bs4 import BeautifulSoup

from html2tk import errors

class Application:


    def __init__(self, master=None, html=None, source_file_path=None,
            stylesheet=None):
        if master is None:
            self.master = tk.Tk()
        else:
            self.master = master

        self.body = tk.Frame(self.master)
        self.body.pack()

        if source_file_path is not None or html is not None:
            self.load_html(html=html, source_file_path=source_file_path)
        else:
            self.html_soup = None
        
        if stylesheet is not None:
            self.apply_stylesheet(stylesheet)
        else:
            self.stylesheet = None
    
    def mainloop(self):
        self.master.mainloop()
    
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
            raise errors.NO_HTML_PROVIDED

        self.html_soup = BeautifulSoup(html)

    def apply_stylesheet(self, stylesheet):
        self.stylesheet = stylesheet
    
    def populate_body(self):
        if self.html_soup is None:
            self.load_html()

        self.body.children.clear()
        
        for element in self.html_soup.recursiveChildGenerator():
            widget = None
            if element.name == 'p':
                widget = tk.Label(self.body, text=element.text,
                    font=self.stylesheet.paragraph_font)
            elif element.name == 'h1':
                widget = tk.Label(self.body, text=element.text,
                    font=self.stylesheet.heading_font)

            if widget is not None:
                widget.pack()

    def get_text_from_element(self, element):
        if element.text is None:
            return ''
        else:
            return ''.join(element.find_all(text=True, recursive=False)).strip()