import numpy as np 
import tkinter as tk 
import tkinter.ttk as ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import pickle




class GUI_plot_circle():
    def __init__(self):
        pass
    def gui(self):
        self.gui_circle= tk.Tk()
        self.gui_circle.geometry("750x570+30+30") 
        self.gui_circle.title('gui.plot.circle')
        
        self.canvas = tk.Canvas(self.gui_circle, bg = 'white', height = 500, width = 500)
        self.canvas.place(x = 220, y = 30)

        x = 20
        y = 30
        xgap = 100
        ygap = 35
        i = 0
        self.xdata_label = tk.Label(self.gui_circle, text = 'Data')
        self.xdata_label.place(x = x, y = y + i*ygap)

        self.data_combobox = ttk.Combobox(self.gui_circle, textvariable = tk.StringVar())
        self.data_combobox["value"] = ['xdata']
        self.data_combobox.current(0)
        self.data_combobox.place(x = x + xgap, y = y + i*ygap, width = 100)
        i += 1
        
        self.px_label = tk.Label(self.gui_circle, text = 'x')
        self.px_label.place(x = x , y = y + i*ygap)


        self.px_entry = tk.Entry(self.gui_circle)
        self.px_entry.place(x = x + xgap, y = y + i*ygap, width = 100)
        i += 1

        self.py_label = tk.Label(self.gui_circle, text = 'y')
        self.py_label.place(x = x, y = y + i*ygap)

        self.py_entry = tk.Entry(self.gui_circle)
        self.py_entry.place(x = x + xgap, y =  y + i*ygap, width = 100)
        i += 1 

        self.pr_label = tk.Label(self.gui_circle, text = 'radius')
        self.pr_label.place(x = x, y =  y + i*ygap)
        
        self.pr_entry = tk.Entry(self.gui_circle)
        self.pr_entry.place(x = x + xgap, y =  y + i*ygap, width = 100)
        i += 1

        
        self.pedge_label = tk.Label(self.gui_circle, text = 'edge')
        self.pedge_label.place(x = x, y = y + i*ygap) 
        
        edge_list = ['NA']
        self.pedge_combobox = ttk.Combobox(self.gui_circle, values = edge_list, state = 'readonly', textvariable = tk.StringVar())
        self.pedge_combobox['values'] = ['NA']
        self.pedge_combobox.current(0)
        self.pedge_combobox.place(x = x + xgap, y = y + i*ygap, width = 100)
        i += 1

        self.ok_button =  tk.Button(self.gui_circle, command = self.do_ok, text = 'OK')
        self.ok_button.place(x = x + xgap, y = y + i*ygap, width = 75)
        i += 1

        self.gui_circle.mainloop()


    def do_ok(self):

        self.px = np.random.uniform(0, 500) if self.px_entry.get() == '' else float(self.px_entry.get())
        self.py = np.random.uniform(0, 500) if self.py_entry.get() == '' else float(self.py_entry.get())
        self.pr = np.random.uniform(1, 25) if self.pr_entry.get() == '' else float(self.pr_entry.get())
        
        self.search_inarea()
        self.search_shape()
 
        fig = plt.figure(figsize=(5,5))

        draw_in_x = [float(i) for i in np.array(self.inshape).T[1]]
        draw_in_y = [float(i) for i in np.array(self.inshape).T[2]]
        draw_out_x = [float(i) for i in np.array(self.outshape).T[1]]
        draw_out_y = [float(i) for i in np.array(self.outshape).T[2]]


        theta = np.linspace(0, 2 * np.pi, 200)
        plt.plot(self.px + self.pr*np.cos(theta), self.py + self.pr*np.sin(theta), color="red", linewidth=1)

        plt.scatter(draw_in_x, draw_in_y , c = 'black', s = 30/self.pr)
        plt.scatter(draw_out_x, draw_out_y, c = 'gray', s = 30/self.pr)
        plt.scatter(self.px, self.py, c = 'red', marker = 'x', s = 30/self.pr)
        
        plt.xlim(self.px - 1.6*self.pr, self.px + 1.6*self.pr)
        plt.ylim(self.py - 1.6*self.pr, self.py + 1.6*self.pr)

        
        
        
        
        canvas = FigureCanvasTkAgg(fig, master=self.gui_circle)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x = 220, y = 30)

    
    def search_inarea(self):
        with open('/Users/pengbohao/Sample_class/FORINVS-master/exdata1_sorted.pickle', 'rb') as f:
            data = pickle.load(f)
        for i in range(len(data)):
            for j in [1, 2, 3, 4]:
                data[i][j] = float(data[i][j])
        
        import copy
        searchkey = copy.copy(self.px)
        
        lower_bound = searchkey - (self.pr*1.5)
        upper_bound = searchkey + (self.pr*1.5)
        
        data_array = myarray(data)[:, 1]
        array = myarray([float(data_array[i]) for i in range(len(data_array))])

        l = abs(array - lower_bound)
        lower_bound_index = max(l.index(min(l))[0])
        
        u = abs(array - upper_bound)
        upper_bound_index = min(u.index(min(u))[0])

        self.inarea = []
        for i in np.arange(lower_bound_index, upper_bound_index):
            
            if abs(float(data[i][2]) - self.py) <= self.pr*1.5:
                self.inarea.append(data[i])
        

    def search_shape(self):
        self.inshape, self.outshape = [], []
        for i in range(len(self.inarea)):
            if (self.inarea[i][1] - self.px)**2 + (self.inarea[i][2] - self.py)**2 <= self.pr**2:
                self.inshape.append(self.inarea[i])
            else:
                self.outshape.append(self.inarea[i])
        print(self.inshape)
        self.inshape = np.array(self.inshape)
        self.outshape = np.array(self.outshape)

        
                


class myarray(np.ndarray):
    def __new__(cls, *args, **kwargs):
        return np.array(*args, **kwargs).view(myarray)
    def index(self, value):
        return np.where(self == value)



if __name__ == "__main__":
    G = GUI_plot_circle()
    G.gui()