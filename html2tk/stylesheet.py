from copy import deepcopy

from html2tk.widgets import Style

class Stylesheet:
    DEFAULT_STYLES = {
        'paragraph' : Style('TLabel',
            font='helvetica',
            font_size=12,
            color='black',
            background_color='grey90'),
        'heading1' : Style('TLabel',
            font='helvetica',
            font_size=24,
            color='black',
            background_color='grey90'),
        'heading2' : Style('TLabel',
            font='helvetica',
            font_size=18,
            color='black',
            background_color='grey90'),
        'button' : Style('TButton',
            font='helvetica',
            font_size=12,
            color='black'),
        'input' : Style('TEntry',
            font='helvetica',
            font_size=12,
            color='black',
            background_color='white'),
        'checkbox_input' : Style('TCheckbutton',
            color='black',
            background_color='grey90'),
        'div' : Style('TFrame',
            background_color='grey90')
    }

    def __init__(self, **kwargs):
        self.styles = {}
        for class_name in kwargs:
            self.styles[class_name] = kwargs[class_name]
        
        self.init_default_styles()
    
    def init_default_styles(self):
        '''Set styles for the basic elements
        if the user hasn't specified them.
        '''

        for style_name in self.DEFAULT_STYLES:
            if style_name not in self.styles:
                self.styles[style_name] = self.DEFAULT_STYLES[style_name]
    
    def __getitem__(self, item):
        '''Get the style named item.
        If the style doesn't exist, returns a fallback style.
        Warning: do not call this before instantiating a Tk window,
        or an extra one will be made due to Tk weirdness.
        '''
        style = self.styles.get(item, self.styles['paragraph'])
        if not style.fully_initiated:
            style.init()
        return style