import numpy as np 
import tkinter as tk 
import tkinter.ttk as ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import pickle
from shapely.geometry import Polygon, MultiPolygon
from matplotlib.path import Path


class GUI_plot_polygon():
    def __init__(self):
        pass
    def gui(self):
        self.gui_polygon= tk.Tk()
        self.gui_polygon.geometry("750x570+30+30") 
        self.gui_polygon.title('gui.plot.polygon')
        
        self.canvas = tk.Canvas(self.gui_polygon, bg = 'white', height = 500, width = 500)
        self.canvas.place(x = 220, y = 30)

        x = 20
        y = 30
        xgap = 100
        ygap = 35
        i = 0
        self.xdata_label = tk.Label(self.gui_polygon, text = 'Data')
        self.xdata_label.place(x = x, y = y + i*ygap)

        self.data_combobox = ttk.Combobox(self.gui_polygon, textvariable = tk.StringVar())
        self.data_combobox["value"] = ['exdata1']
        self.data_combobox.current(0)
        self.data_combobox.place(x = x + xgap, y = y + i*ygap, width = 100)
        i += 1
        
        self.px_label = tk.Label(self.gui_polygon, text = 'px (m)')
        self.px_label.place(x = x , y = y + i*ygap)


        self.px_entry = tk.Entry(self.gui_polygon)
        self.px_entry.place(x = x + xgap, y = y + i*ygap, width = 100)
        i += 1

        self.py_label = tk.Label(self.gui_polygon, text = 'py (m)')
        self.py_label.place(x = x, y = y + i*ygap)

        self.py_entry = tk.Entry(self.gui_polygon)
        self.py_entry.place(x = x + xgap, y =  y + i*ygap, width = 100)
        i += 1 

        default_valuew = tk.StringVar()
        default_valuew.set("10,10,10,10,10")
        self.pl_label = tk.Label(self.gui_polygon, text = 'length (m)')
        self.pl_label.place(x = x, y =  y + i*ygap)
        

        self.pl_entry = tk.Entry(self.gui_polygon, textvariable = default_valuew)
        self.pl_entry.place(x = x + xgap, y =  y + i*ygap, width = 100)
        i += 1

        default_valuer = tk.StringVar()
        default_valuer.set("0,72,144,216,288")
        self.pr_label = tk.Label(self.gui_polygon, text = 'angle(degree)')
        self.pr_label.place(x = x, y =  y + i*ygap)
        
       
        self.pr_entry = tk.Entry(self.gui_polygon, textvariable = default_valuer)
        self.pr_entry.place(x = x + xgap, y =  y + i*ygap, width = 100)
        i += 1
        
        default_valueo = tk.StringVar()
        default_valueo.set("0")
        self.po_label = tk.Label(self.gui_polygon, text = 'rotation(degree)')
        self.po_label.place(x = x, y =  y + i*ygap)
        
       
        self.po_entry = tk.Entry(self.gui_polygon, textvariable = default_valueo)
        self.po_entry.place(x = x + xgap, y =  y + i*ygap, width = 100)
        i += 1


        
        self.pedge_label = tk.Label(self.gui_polygon, text = 'boundary')
        self.pedge_label.place(x = x, y = y + i*ygap) 
        
        edge_list = ['NA']
        self.pedge_combobox = ttk.Combobox(self.gui_polygon, values = edge_list, state = 'readonly', textvariable = tk.StringVar())
        self.pedge_combobox['values'] = ['NA']
        self.pedge_combobox.current(0)
        self.pedge_combobox.place(x = x + xgap, y = y + i*ygap, width = 100)
        i += 1

        self.ok_button =  tk.Button(self.gui_polygon, command = self.do_ok, text = 'OK')
        self.ok_button.place(x = x + xgap, y = y + i*ygap, width = 75)
        i += 1

        self.gui_polygon.mainloop()


    def do_ok(self):

        self.px = np.random.uniform(0, 500) if self.px_entry.get() == '' else float(self.px_entry.get())
        self.py = np.random.uniform(0, 500) if self.py_entry.get() == '' else float(self.py_entry.get())
        self.pg =self.pl_entry.get().split(',')
        self.pr =self.pr_entry.get().split(',')
        self.po=self.po_entry.get()
        
        self.pl=[]
        for i in range(len(self.pg)):
            self.pl.append(float(self.pg[i]))
        
        listx=[]
        listy=[]
        for i in range(len(self.pl)):
            listx.append(self.px+float(self.pl[i])*np.cos(np.pi*((float(self.pr[i])+float(self.po))/180)))
            listy.append(self.py+float(self.pl[i])*np.sin(np.pi*((float(self.pr[i])+float(self.po))/180)))


        self.arrayx = np.array(listx)
        self.arrayy = np.array(listy)
        polygon = Polygon(np.c_[self.arrayx, self.arrayy])
        
        self.edge = max(self.pl)      
        self.search_inarea()
        self.search_shape()
 
        fig = plt.figure(figsize=(5,5))

        draw_in_x = [float(i) for i in np.array(self.inshape).T[1]]
        draw_in_y = [float(i) for i in np.array(self.inshape).T[2]]
        draw_out_x = [float(i) for i in np.array(self.outshape).T[1]]
        draw_out_y = [float(i) for i in np.array(self.outshape).T[2]]

        plt.plot(*polygon.exterior.xy)
        plt.scatter(draw_in_x, draw_in_y , c = 'black', s = 30/self.edge)
        plt.scatter(draw_out_x, draw_out_y, c = 'gray', s = 30/self.edge)
        plt.scatter(self.px, self.py, c = 'red', marker = 'x', s = 10)
        
        plt.xlim(self.px - 1.6*self.edge, self.px + 1.6*self.edge)
        plt.ylim(self.py - 1.6*self.edge, self.py + 1.6*self.edge)
                
        canvas = FigureCanvasTkAgg(fig, master=self.gui_polygon)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x = 220, y = 30)

    
    def search_inarea(self):
        with open('exdata1_sorted.pickle', 'rb') as f:
            data = pickle.load(f)
        for i in range(len(data)):
            for j in [1, 2, 3, 4]:
                data[i][j] = float(data[i][j])
        
        import copy
        searchkey = copy.copy(self.px)
        
        
        lower_bound = int(searchkey) - int((self.edge*1.5))
        upper_bound = int(searchkey) + int((self.edge*1.5))
        
        data_array = myarray(data)[:, 1]
        array = myarray([float(data_array[i]) for i in range(len(data_array))])

        l = abs(array - lower_bound)
        lower_bound_index = max(l.index(min(l))[0])
        
        u = abs(array - upper_bound)
        upper_bound_index = min(u.index(min(u))[0])

        self.inarea = []
        for i in np.arange(lower_bound_index, upper_bound_index):
            
            if abs(float(data[i][2]) - self.py) <= self.edge*1.5:
                self.inarea.append(data[i])
        

    def search_shape(self):
        self.inshape, self.outshape = [], []
        p = Path(np.c_[self.arrayx, self.arrayy])  
        for i in range(len(self.inarea)):
            x = self.inarea[i][1]
            y = self.inarea[i][2]
            if p.contains_points([(x, y)]):
                self.inshape.append(self.inarea[i])
            else:
                self.outshape.append(self.inarea[i])

        self.inshape = np.array(self.inshape)
        self.outshape = np.array(self.outshape)
    
 


class myarray(np.ndarray):
    def __new__(cls, *args, **kwargs):
        return np.array(*args, **kwargs).view(myarray)
    def index(self, value):
        return np.where(self == value)



if __name__ == "__main__":
    G = GUI_plot_polygon()
    G.gui()