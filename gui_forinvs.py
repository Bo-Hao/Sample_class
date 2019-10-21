import numpy as np 
import tkinter as tk 
from tkinter import messagebox
from gui_clt import CLT_gui







class Forinvs():
    def __init__(self, ):
        pass

    def gui(self):
        self.Entry_gui= tk.Tk()
        self.Entry_gui.title('gui')


        self.canvas = tk.Canvas(self.Entry_gui, height = 329, width = 637)
        self.canvas.grid(column = 0, row = 0)
        image_file = tk.PhotoImage(file='title.gif')
        self.canvas.create_image(0, 0, anchor='nw', image=image_file)



        # Menu bar 
        menubar = tk.Menu(self.Entry_gui)


        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Close', command = self.Entry_gui.quit)
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
        theory_menu.add_command(label='CLT', command = self.theory_clt)
        menubar.add_cascade(label='Theory', menu=theory_menu)

        help_menu = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label='Help', menu=help_menu)


        self.Entry_gui.config(menu=menubar)



        self.Entry_gui.mainloop()
        
    def do_job(self):
        print("do")

    def theory_clt(self):
        CLT_gui().gui()
        

c = Forinvs()
c.gui()