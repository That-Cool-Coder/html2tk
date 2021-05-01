import tkinter as tk
import tkinter.ttk as ttk

import colorutils

from html2tk.widgets import Widget

class ColorInput(Widget):
    width = 100
    height = 70
    resolution = 20

    def __init__(self, master, html_element):
        super().__init__(master, html_element)

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