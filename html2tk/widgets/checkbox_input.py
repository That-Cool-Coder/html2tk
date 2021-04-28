import tkinter as tk
import tkinter.ttk as ttk

from .widget import Widget

class CheckboxInput(Widget):
    def __init__(self, master, html_element):
        super().__init__(master, html_element)

        self.tk_intvar = tk.IntVar()
        self.tk_widget = ttk.Checkbutton(self.master, variable=self.tk_intvar,
            command=self.update_checked)
        
        if self.html_element.has_attr('checked'):
            self.tk_intvar.set(1)

        self.update_checked()
    
    def update_checked(self, event=None):
        self.checked = bool(self.tk_intvar.get())
    
    