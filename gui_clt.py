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





class CLT_gui():
    def __init__(self):
        self.information = {
            "uniform":[['min', "max"], np.random.uniform, []], "normal":[["mu", "sigma"], np.random.normal, []],
            "binomial":[['n', 'p'], np.random.binomial, []], "possion":[['lambda'], np.random.poisson, []], "gamma":[['shape'], np.random.gamma, []],
            "beta":[['a', 'b'], np.random.beta, []]
            }
        

        
        

    def gui(self):
        self.clt_gui= tk.Tk()
        self.clt_gui.title('gui.CLT')
        
        self.canvas = tk.Canvas(self.clt_gui, bg = 'white', height = 500, width = 500)
        self.canvas.grid(column = 4, row = 0)

        self.distri_label = tk.Label(self.clt_gui, text = 'Distribution.')
        self.distri_label.grid(column = 0, row = 0)

        distri_list = [i for i in self.information]
        self.distri_combobox = ttk.Combobox(self.clt_gui, values = distri_list, state = 'readonly')
        self.distri_combobox.grid(column = 1, row = 0)

        '''self.distri_button = tk.Button(self.clt_gui, text = 'Comfirm', command = self.distri_command)
        self.distri_button.grid(column = 1, row = 2)'''
        i = 1
        for d in self.information:
            for j in range(len(self.information[d][0])):
                label_text = self.information[d][0][j]
                l = tk.Label(self.clt_gui, text = label_text)
                l.grid(column = 0 + 2*j, row = i)
                e = tk.Entry(self.clt_gui)
                e.grid(column = 1 + 2*j, row = i)
                self.information[d][2].append(e)

            i += 1

        self.n_label = tk.Label(self.clt_gui, text = "sample size")
        self.n_label.grid(column = 0, row = i+1)
        self.n_entry = tk.Entry(self.clt_gui)
        self.n_entry.grid(column = 1, row = i+1)
        
        self.times_label = tk.Label(self.clt_gui, text = 'iteration')
        self.times_label.grid(column = 0, row = i+2)
        self.times_entry = tk.Entry(self.clt_gui)
        self.times_entry.grid(column = 1, row = i+2)

        self.run_button = tk.Button(self.clt_gui, command = self.ok, text = 'OK')
        self.run_button.grid(column = 1, row = i+3)        


        self.clt_gui.mainloop()
    
    '''def distri_command(self):
        if self.distri_combobox.get() == "":
            messagebox.showinfo(title='Error', message='please select the type of distribution.')
        else:
            para_info = self.information[self.distri_combobox.get()][0]
            if len(self.para_label_list) != []:
                for i in range(len(self.para_label_list)):
                    self.para_label_list[i].destroy()
                    self.para_entry_list[i].destroy()
                self.para_label_list = []
                self.para_entry_list = []

            for i in range(len(para_info)):
                para_label = tk.Label(self.clt_gui, text = para_info[i])
                para_label.grid(column = 2*i, row = 3, padx=2, pady=10)
                para_entry = tk.Entry(self.clt_gui)
                para_entry.grid(column = 2*i+1, row = 3, padx=2, pady=10)
                self.para_label_list.append(para_label)
                self.para_entry_list.append(para_entry)'''


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
        fig = plt.figure(figsize=(7,7))
        plt.subplot(3,1,1)
        drawer = self.information[self.dis_type][1]
        sa = []
        for i in range(self.times):
            sa.append(np.mean(drawer(size = 1, *self.parameter)))
        plt.hist(sa)
        plt.title('Distribution of '+str(self.distri_combobox.get()+' distribution'))
        plt.subplot(3,1,2)
        n, bins, patches = plt.hist(self.savier, bins = 50)
        plt.title('Distribution of Means')
        (mu, sigma) = norm.fit(self.savier)
        # add a 'best fit' line
        y = norm.pdf(bins, mu, sigma)
        l = plt.plot(bins, y/sum(y)*self.times, 'r--', linewidth=2)       
        plt.subplot(3,1,3)
        n, bins, patches = plt.hist(self.savier, bins = 50,cumulative=True)
        
    
        plt.title('Cumulative Distribution Function of Means')
        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

        
        canvas = FigureCanvasTkAgg(fig, master=self.clt_gui)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(column = 4, row = 0)
        


def p(*argv, a):
    print(a)
    for arg in argv:
        print(arg)
def b(d):
    L = 53
    ans = d*L/(L+ d/2)
    return ans
def three_edge(a, b, c):
    ang1 = acos((b**2 + c**2 - a**2)/(2*b*c))
    ang2 = acos((-b**2 + c**2 + a**2)/(2*a*c))
    ang3 = acos((b**2 - c**2 + a**2)/(2*b*a))

    return ang1/pi*180, ang2/pi*180, ang3/pi*180
    



if __name__ == "__main__":
    m = CLT_gui()
    m.gui()
    

    