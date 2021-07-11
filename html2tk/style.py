import tkinter as tk
import tkinter.ttk as ttk

class Style:
    # This counter allows us to create unique ttk style names
    style_count = 0

    TK_DEFAULT_FONT_SIZE = 10

    def __init__(self, base_style_name, **kwargs):
        self.base_style_name = base_style_name

        # create a name garanteed to be unique by using a counter
        self.name = f'html2tk-{str(self.__class__.style_count)}.{base_style_name}'
        self.__class__.style_count += 1

        self.initial_styling = kwargs
        self.fully_initiated = False
        
    def init(self):
        '''When creating a ttk.Style, a new window is created
        if one doesn't exist already.
        This is bad as styles will often be created prior to window starting,
        which then means we have a useless extra window.
        To fix that, we have a seperate init method that a stylesheet can call
        when the style is actually needed.'''

        # Create a style object so that we can lookup styles etc
        self.ttk_style = ttk.Style()

        # Apply the initial values for color etc that were set in kwargs
        for item in self.initial_styling:
            self.__setattr__(item, self.initial_styling[item])
        self.fully_initiated = True
        
    def copy(self):
        '''Create a totally independent style object identical to this
        '''

        new_style = Style(self.base_style_name,
            color=self.color, background_color=self.background_color,
            font_size=self.font_size, font=self.font)
        return new_style


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
        if self.ttk_style.lookup(self.name, 'font') == 'TkDefaultFont':
            return self.TK_DEFAULT_FONT_SIZE
        font_name, size = self.ttk_style.lookup(self.name, 'font')
        return size
    
    @font_size.setter
    def font_size(self, value):
        font_name = self.ttk_style.lookup(self.name, 'font')
        self.ttk_style.configure(self.name, font=(font_name, int(value)))
    
    @property
    def font(self):
        font_name = self.ttk_style.lookup(self.name, 'font')
        return font_name
    
    @font.setter
    def font(self, value):
        if self.ttk_style.lookup(self.name, 'font') == 'TkDefaultFont':
            old_size = self.TK_DEFAULT_FONT_SIZE
        else:
            old_font_name, old_size = self.ttk_style.lookup(self.name, 'font')
        self.ttk_style.configure(self.name, font=(value, old_size))