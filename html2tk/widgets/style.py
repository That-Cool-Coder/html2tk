import tkinter as tk
import tkinter.ttk as ttk

class Style:
    # This counter allows us to create unique ttk style names
    style_count = 0

    def __init__(self, base_style_name, *args, **kwargs):
        self.base_style_name = base_style_name

        # create a name garanteed to be unique by using a counter
        self.name = f'html2tk-{str(self.__class__.style_count)}.{base_style_name}'
        self.__class__.style_count += 1

        # Create a style object so that we can lookup styles etc
        # (ttk styles are weird!)
        self.ttk_style = ttk.Style()

        for item in kwargs:
            self.__setattr__(item, kwargs[item])
        
    @property
    def color(self):
        return self.ttk_style.lookup(self.name, 'foreground')
    
    @color.setter
    def color(self, value):
        self.ttk_style.configure(self.name, foreground=value)
    
    @property
    def background_color(self):
        return self.ttk_style.lookup(self.name, 'background')
    
    @background_color.setter
    def background_color(self, value):
        self.ttk_style.configure(self.name, background=value)
    
    @property
    def font_size(self):
        print('Can\'t get font size of styles yet due to issues with ttk')
        font_name, size = self.ttk_style.lookup(self.name, 'font')
        return size
    
    @font_size.setter
    def font_size(self, value):
        font_name = self.ttk_style.lookup(self.name, 'font')
        self.ttk_style.configure(self.name, font=(font_name, value))
    
    @property
    def font(self):
        font_name = self.ttk_style.lookup(self.name, 'font')
        return font_name
    
    @font.setter
    def font(self, value):
        print('Can\'t set font of styles yet due to issues with ttk')
        old_font_name, old_size = self.ttk_style.lookup(self.name, 'font')
        self.ttk_style.configure(self.name, (value, old_size))