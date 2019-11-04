import numpy as np 
import math
import tkinter as tk 
import tkinter.ttk as ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.mlab as mlab
from scipy.stats import norm
import configparser
import seaborn as sns
from scipy import stats
from PIL import Image  
from PIL import ImageDraw  
from PIL import ImageFont  
# KS test


class CLT_gui():
    def __init__(self):
        self.information = {
            "Uniform":[['min', "max"], np.random.uniform, []], "Normal":[["mu", "sigma"], np.random.normal, []],
            "Binomial":[['n', 'p'], np.random.binomial, []], "Possion":[['lambda'], np.random.poisson, []], "gamma":[['shape'], np.random.gamma, []],
            "Beta":[['a', 'b'], np.random.beta, []]
            }
        

    def gui(self):
        self.clt_gui= tk.Tk()
        self.clt_gui.geometry("750x570+30+30") 
        self.clt_gui.title('gui.CLT')
        
        self.canvas = tk.Canvas(self.clt_gui, bg = 'white', height = 500, width = 500)
        self.canvas.place(x = 250, y = 30)

        self.distri_label = tk.Label(self.clt_gui, text = 'Distribution')
        self.distri_label.place(x = 10, y = 20)
        self.v=tk.StringVar()
        self.distri_radio1 = tk.Radiobutton(self.clt_gui,text='Uniform',variable=self.v,
                                            value='Uniform' )
        self.distri_radio1.place(x = 10, y = 30+35*1)
        
        self.distri_radio2 = tk.Radiobutton(self.clt_gui,text='Normal',variable=self.v,
                                            value='Normal')
        self.distri_radio2.place(x = 10, y = 30+35*3)
        self.distri_radio3 = tk.Radiobutton(self.clt_gui,text='Binomial',variable=self.v,
                                            value='Binomial')
        self.distri_radio3.place(x = 10, y = 30+35*5)
        self.distri_radio4= tk.Radiobutton(self.clt_gui,text="Possion",variable=self.v,
                                            value="Possion" )
        self.distri_radio4.place(x = 10, y = 30+35*7)
        self.distri_radio5= tk.Radiobutton(self.clt_gui,text="gamma",variable=self.v,
                                            value="gamma")
        self.distri_radio5.place(x = 10, y = 30+35*8)
        self.distri_radio5= tk.Radiobutton(self.clt_gui,text="Beta",variable=self.v,
                                            value="Beta")
        self.distri_radio5.place(x = 10, y = 30+35*9)
        
        i = 1
        for d in self.information:
            for j in range(len(self.information[d][0])):
                label_text = self.information[d][0][j]
                l = tk.Label(self.clt_gui, text = label_text)
                l.place(x = 90, y = 30 + 35*i)
                e = tk.Entry(self.clt_gui)
                e.place(x = 140, y = 30 + 35*i, width = 100)
                self.information[d][2].append(e)

                i += 1

        self.n_label = tk.Label(self.clt_gui, text = "Sample size")
        self.n_label.place(x = 20, y = 30 + 35 * (i+1))
        self.n_entry = tk.Entry(self.clt_gui)
        self.n_entry.place(x = 110, y = 30 + 35 * (i+1), width = 100)
        
        self.times_label = tk.Label(self.clt_gui, text = 'Iteration')
        self.times_label.place(x = 20, y = 30 + 35 * (i+2))
        self.times_entry = tk.Entry(self.clt_gui)
        self.times_entry.place(x = 110, y = 30 + 35 * (i+2), width = 100)

        self.run_button = tk.Button(self.clt_gui, command = self.ok, text = 'OK')
        self.run_button.place(x = 50, y = 30 + 35 * (i+3), width = 100)        


        self.clt_gui.mainloop()


    def ok(self):
        if self.n_entry.get() == '' or self.times_entry == '':
            messagebox.showinfo(title='Error', message='please entry the parameter of sample.')
    
        else:
            self.n = int(self.n_entry.get())
            self.times = int(self.times_entry.get())
            self.parameter = [float(i.get()) for i in self.information[self.v.get()][2]]
            self.cal()
            self.drawit()
            


    def cal(self):
        drawer = self.information[self.v.get()][1]
        self.savier = []
        for i in range(self.times):
            self.savier.append(np.mean(drawer(size = self.n, *self.parameter)))
        



    def drawit(self):
        fig = plt.figure(figsize=(6,6))
        plt.subplot(3,1,1)
        drawer = self.information[self.v.get()][1]
        sa = []
        for i in range(self.times):
            sa.append(np.mean(drawer(size = 1, *self.parameter)))
        sns.set()
        sns.distplot(sa,color='blue',kde=False,bins=40)
        plt.title('Distribution of '+self.v.get()+' distribution')
        plt.subplot(3,1,2)
        sns.distplot(self.savier,fit=norm,bins=40,color='blue')
        plt.title('Distribution of Means')      
        plt.subplot(3,1,3)
        plt.hist(self.savier, bins =40,cumulative=True,density=True,color='blue')
        samples=np.random.normal(np.mean(self.savier),np.std(self.savier),self.times)
        sns.distplot(samples,kde_kws={'cumulative': True},hist=False,color='red')       
        plt.title('Cumulative Distribution Function of Means')
        #Compute mean and standard deviation: mu, sigma
     
        # Sample out of a normal distribution with this mu and sigma: samples
        
  
        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)        
        plt.legend(loc='upper left',title='ks test: pvalue='+str((round(stats.kstest(self.savier,'norm')[1],5)))) 

      
        canvas = FigureCanvasTkAgg(fig, master=self.clt_gui)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x = 250, y = 30)
        




if __name__ == "__main__":
    m = CLT_gui()
    m.gui()