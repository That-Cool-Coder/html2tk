import tkinter as tk

from bs4 import BeautifulSoup

class Application:
    def __init__(self, master=None, raw_html=None, source_file_name=None):
        if master is None:
            self.master = tk.Tk()
        else:
            self.master = master

        self.soup = None
        

        self.body = tk.Frame(self.master)
        self.body.pack()

        if source_file_name is not None or raw_html is not None:
            self.populate_body(raw_html=raw_html, source_file_name=source_file_name)

        self.master.mainloop()
    
    def populate_body(self, raw_html=None, source_file_name=None):
        self.body.children.clear()
        if source_file_name is not None:
            file = None
            try:
                file = open(source_file_name, 'r')
                raw_html = file.read()
            except FileNotFoundError:
                print('Error: could not find file ' + source_file_name)
                return
            except PermissionError:
                print('Error: insufficient permissions to read file ' + source_file_name)
                return
            except:
                print('Error: unknown error')
                return
            finally:
                if file is not None:
                    file.close()
        elif raw_html is None and source_file_name is None:
            print('Error: Both raw_html and source_file_name are None')
            return
        
        print(raw_html)

        try:
            self.soup = BeautifulSoup(raw_html)
        except:
            print('Error: error decoding html')
            raise
            return
        
        for element in self.soup.recursiveChildGenerator():
            if element.name == 'p':
                print(element.text)
                label = tk.Label(self.body, text=element.text)
                label.pack()
