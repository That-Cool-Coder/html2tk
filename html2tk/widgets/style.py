import tkinter as tk
import tkinter.ttk as ttk

class Style:
    # This allows us to create unique ttk style names
    style_count = 0

    def __init__(self, base_style_name, *args **kwargs):
        self.base_style_name = base_style_name

        # create a name garanteed to be unique by using a counter
        self.name = f'html2tk-{str(self.__class__.style_count)}.{base_style}'
        self.__class__.style_count += 1

        self.ttk_style = ttk.Style()
        
    @property
    def color(self):
        return self.ttk_style.lookup(self.name, 'fg')
    
    @property
    def background_color(self):
        return self.ttk_style.lookup(self.name, 'bg')