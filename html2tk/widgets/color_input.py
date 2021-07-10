import tkinter as tk
import tkinter.ttk as ttk

from bs4 import BeautifulSoup
import tkcolorpicker
import colorutils

from html2tk.widgets import Widget

class ColorInput(Widget):
    width = 40
    height = 20

    def __init__(self, master: Widget, html_soup_element: BeautifulSoup):
        super().__init__(master, html_soup_element)

        self.__value = self.html_soup_element.attrs.get('value', '#FFFFFF')

        self.tk_widget = tk.Canvas(self.master.tk_widget,
            width=self.width, height=self.height, bg='white')
        self.tk_widget.bind('<Button-1>', self.ask_color)

        self.callbacks = []
    
    def ask_color(self, event=None):
        new_color = tkcolorpicker.askcolor(self.__value)[1]
        if new_color is not None:
            self.__value = new_color
            self.tk_widget.configure(bg=self.__value)
            for callback in self.callbacks:
                callback()

    def add_callback(self, func):
        self.callbacks.append(func)
    
    def remove_callback(self, func):
        raise NotImplementedError

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        # Expects string like '#ff785e'
        self.__value = value

    @property
    def value_hsv(self):
        return colorutils.hex_to_hsv(self.__value)
    
    @value_hsv.setter
    def value_hsv(self, value):
        # Expects a tuple (h, s, v)
        self.__value = colorutils.hsv_to_hex(value)

    @property
    def value_hsl(self):
        return colorutils.hex_to_hsl(self.__value)
    
    @value_hsl.setter
    def value_hsl(self, value):
        # Expects a tuple (h, s, l)
        self.__value = colorutils.hsl_to_hex(value)

    @property
    def value_rgb(self):
        return colorutils.hex_to_rgb(self.__value)
    
    @value_rgb.setter
    def value_rgb(self, value):
        # Expects a tuple (r, g, b)
        self.__value = colorutils.rgb_to_hex(value)
    


'''
class ColorInput(Widget):
    width = 100
    height = 70
    resolution = 20

    def __init__(self, master, html_soup_element):
        super().__init__(master, html_soup_element)

        self.tk_widget = ttk.Frame(self.master)

        self.hue = 40

        # sv = saturation + value (as in hsv colors)
        self.sv_area = tk.Canvas(self.tk_widget,
            width=self.width, height=self.height)
        self.sv_area.pack()

        self.populate_sv_area()

        self.hue_slider = ttk.Scale(self.tk_widget, from_=0, to=359,
            command=self.update_sv_area)
        self.hue_slider.pack()
        self.update_sv_area()
    
    def populate_sv_area(self):
        col_width = self.width /self.resolution
        row_height = self.height / self.resolution

        self.sv_area_rects = []
        for row_num in range(self.resolution):
            crnt_row = []
            for col_num in range(self.resolution):
                pos_x = col_width * col_num
                pos_y = row_height * row_num
                rect = self.sv_area.create_rectangle(pos_x, pos_y,
                    pos_x + col_width, pos_y + col_width,
                    outline='')
                crnt_row.append(rect)
            self.sv_area_rects.append(crnt_row)
    
    def update_sv_area(self, *args):
        hue = self.hue_slider.get()
        for row_num, row in enumerate(self.sv_area_rects):
            for col_num, rect in enumerate(row):
                saturation = col_num / self.resolution
                value = (1 - row_num / self.resolution)
                hex_color = colorutils.hsv_to_hex((hue, saturation, value))
                self.sv_area.itemconfigure(rect, fill=hex_color)
'''