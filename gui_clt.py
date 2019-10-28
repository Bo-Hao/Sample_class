import numpy as np 
from math import *
import tkinter as tk 
import tkinter.ttk as ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.mlab as mlab
from scipy.stats import norm


# KS test


class CLT_gui():
    def __init__(self):
        self.information = {
            "uniform":[['min', "max"], np.random.uniform, []], "normal":[["mu", "sigma"], np.random.normal, []],
            "binomial":[['n', 'p'], np.random.binomial, []], "possion":[['lambda'], np.random.poisson, []], "gamma":[['shape'], np.random.gamma, []],
            "beta":[['a', 'b'], np.random.beta, []]
            }
        

    def gui(self):
        self.clt_gui= tk.Tk()
        self.clt_gui.geometry("750x570+30+30") 
        self.clt_gui.title('gui.CLT')
        
        self.canvas = tk.Canvas(self.clt_gui, bg = 'white', height = 500, width = 500)
        self.canvas.place(x = 220, y = 30)

        self.distri_label = tk.Label(self.clt_gui, text = 'Distribution')
        self.distri_label.place(x = 20, y = 30)

        distri_list = [i for i in self.information]
        self.distri_combobox = ttk.Combobox(self.clt_gui, values = distri_list, state = 'readonly')
        self.distri_combobox.place(x = 110, y = 30, width = 100)

        i = 1
        for d in self.information:
            for j in range(len(self.information[d][0])):
                label_text = self.information[d][0][j]
                l = tk.Label(self.clt_gui, text = label_text)
                l.place(x = 20, y = 30 + 35*i)
                e = tk.Entry(self.clt_gui)
                e.place(x = 110, y = 30 + 35*i, width = 100)
                self.information[d][2].append(e)

                i += 1

        self.n_label = tk.Label(self.clt_gui, text = "sample size")
        self.n_label.place(x = 20, y = 30 + 35 * (i+1))
        self.n_entry = tk.Entry(self.clt_gui)
        self.n_entry.place(x = 110, y = 30 + 35 * (i+1), width = 100)
        
        self.times_label = tk.Label(self.clt_gui, text = 'iteration')
        self.times_label.place(x = 20, y = 30 + 35 * (i+2))
        self.times_entry = tk.Entry(self.clt_gui)
        self.times_entry.place(x = 110, y = 30 + 35 * (i+2), width = 100)

        self.run_button = tk.Button(self.clt_gui, command = self.ok, text = 'OK')
        self.run_button.place(x = 50, y = 30 + 35 * (i+3), width = 100)        


        self.clt_gui.mainloop()


    def ok(self):
        if self.distri_combobox.get() == "":
            messagebox.showinfo(title='Error', message='please select the type of distribution.')
        
        elif self.n_entry.get() == '' or self.times_entry == '':
            messagebox.showinfo(title='Error', message='please entry the parameter of sample.')
        
        else:
            self.n = int(self.n_entry.get())
            self.times = int(self.times_entry.get())
            self.dis_type = self.distri_combobox.get()
            self.parameter = [float(i.get()) for i in self.information[self.dis_type][2]]
            self.cal()
            self.drawit()
            


    def cal(self):
        drawer = self.information[self.dis_type][1]
        self.savier = []
        for i in range(self.times):
            self.savier.append(np.mean(drawer(size = self.n, *self.parameter)))
        



    def drawit(self):
        fig = plt.figure(figsize=(5,5))
        plt.subplot(3,1,1)
        drawer = self.information[self.dis_type][1]
        sa = []
        for i in range(self.times):
            sa.append(np.mean(drawer(size = 1, *self.parameter)))
        plt.hist(sa)
        plt.title('Distribution of '+str(self.distri_combobox.get()+' distribution'))
        plt.subplot(3,1,2)
        n, bins, patches = plt.hist(self.savier, bins = 40)
        plt.title('Distribution of Means')
        (mu, sigma) = norm.fit(self.savier)
        # add a 'best fit' line
        y = norm.pdf(bins, mu, sigma)
        l = plt.plot(bins, y/sum(y)*self.times, 'r--', linewidth=2)       
        plt.subplot(3,1,3)
        n, bins, patches = plt.hist(self.savier, bins = 40,cumulative=True)
        
    
        plt.title('Cumulative Distribution Function of Means')
        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

        
        canvas = FigureCanvasTkAgg(fig, master=self.clt_gui)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x = 220, y = 30)
        




if __name__ == "__main__":
    m = CLT_gui()
    m.gui()
    

    