import numpy as np 
import tkinter as tk 
from tkinter import messagebox








class Forinvs():
    def __init__(self, ):
        pass

    def gui(self):
        self.window= tk.Tk()
        self.window.title('gui')


        self.canvas = tk.Canvas(self.window, height = 329, width = 637)
        self.canvas.grid(column = 0, row = 0)
        image_file = tk.PhotoImage(file='title.gif')
        self.canvas.create_image(0, 0, anchor='nw', image=image_file)



        # Menu bar 
        menubar = tk.Menu(self.window)


        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Close', command = self.window.quit)
        file_menu.add_separator()##这里就是一条分割线


        plot_design_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Plot Design', menu=plot_design_menu)
        plot_design_menu.add_command(label='Circle', command = self.do_job)
        plot_design_menu.add_command(label='Cluster', command = self.do_job)
        plot_design_menu.add_command(label='HPS', command = self.do_job)
        plot_design_menu.add_command(label='Rectangle', command = self.do_job)
        plot_design_menu.add_command(label='Polygon', command = self.do_job)

        sample_design_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Sample Design', menu=sample_design_menu)

        theory_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Theory', menu=theory_menu)

        help_menu = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label='Help', menu=help_menu)


        self.window.config(menu=menubar)



        self.window.mainloop()
        
    def do_job(self):
        print("do")
c = Forinvs()
c.gui()