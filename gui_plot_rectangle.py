import numpy as np 
import tkinter as tk 
import tkinter.ttk as ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import pickle




class GUI_plot_rectangle():
    def __init__(self):
        pass
    def gui(self):
        self.gui_rectangle= tk.Tk()
        self.gui_rectangle.geometry("750x570+30+30") 
        self.gui_rectangle.title('gui.plot.rectangle')
        
        self.canvas = tk.Canvas(self.gui_rectangle, bg = 'white', height = 500, width = 500)
        self.canvas.place(x = 220, y = 30)

        x = 20
        y = 30
        xgap = 100
        ygap = 35
        i = 0
        self.xdata_label = tk.Label(self.gui_rectangle, text = 'Data')
        self.xdata_label.place(x = x, y = y + i*ygap)

        self.data_combobox = ttk.Combobox(self.gui_rectangle, textvariable = tk.StringVar())
        self.data_combobox["value"] = ['exdata1']
        self.data_combobox.current(0)
        self.data_combobox.place(x = x + xgap, y = y + i*ygap, width = 100)
        i += 1
        
        self.px_label = tk.Label(self.gui_rectangle, text = 'px (m)')
        self.px_label.place(x = x , y = y + i*ygap)


        self.px_entry = tk.Entry(self.gui_rectangle)
        self.px_entry.place(x = x + xgap, y = y + i*ygap, width = 100)
        i += 1

        self.py_label = tk.Label(self.gui_rectangle, text = 'py (m)')
        self.py_label.place(x = x, y = y + i*ygap)

        self.py_entry = tk.Entry(self.gui_rectangle)
        self.py_entry.place(x = x + xgap, y =  y + i*ygap, width = 100)
        i += 1 

        self.ph_label = tk.Label(self.gui_rectangle, text = 'width (m)')
        self.ph_label.place(x = x, y =  y + i*ygap)
        
        default_valueh = tk.StringVar()
        default_valueh.set(10)
        self.ph_entry = tk.Entry(self.gui_rectangle, textvariable = default_valueh)
        self.ph_entry.place(x = x + xgap, y =  y + i*ygap, width = 100)
        i += 1

        default_valuew = tk.StringVar()
        default_valuew.set(10)
        self.pw_label = tk.Label(self.gui_rectangle, text = 'length (m)')
        self.pw_label.place(x = x, y =  y + i*ygap)
        

        self.pw_entry = tk.Entry(self.gui_rectangle, textvariable = default_valuew)
        self.pw_entry.place(x = x + xgap, y =  y + i*ygap, width = 100)
        i += 1

        default_valuer = tk.StringVar()
        default_valuer.set(0)
        self.pr_label = tk.Label(self.gui_rectangle, text = 'rotation (degree)')
        self.pr_label.place(x = x, y =  y + i*ygap)
        
        self.pr_entry = tk.Entry(self.gui_rectangle, textvariable = default_valuer)
        self.pr_entry.place(x = x + xgap, y =  y + i*ygap, width = 100)
        i += 1

        
        self.pedge_label = tk.Label(self.gui_rectangle, text = 'boundary')
        self.pedge_label.place(x = x, y = y + i*ygap) 
        
        edge_list = ['NA']
        self.pedge_combobox = ttk.Combobox(self.gui_rectangle, values = edge_list, state = 'readonly', textvariable = tk.StringVar())
        self.pedge_combobox['values'] = ['NA']
        self.pedge_combobox.current(0)
        self.pedge_combobox.place(x = x + xgap, y = y + i*ygap, width = 100)
        i += 1

        self.ok_button =  tk.Button(self.gui_rectangle, command = self.do_ok, text = 'OK')
        self.ok_button.place(x = x + xgap, y = y + i*ygap, width = 75)
        i += 1

        self.gui_rectangle.mainloop()


    def do_ok(self):

        self.px = np.random.uniform(0, 500) if self.px_entry.get() == '' else float(self.px_entry.get())
        self.py = np.random.uniform(0, 500) if self.py_entry.get() == '' else float(self.py_entry.get())
        self.ph =float(self.ph_entry.get())
        self.pw =float(self.pw_entry.get())
        self.pr = float(self.pr_entry.get())
        
        self.edge = max(self.pw, self.ph)
        
        radian = np.pi*self.pr/180
        rotation_matrix = np.array([[np.cos(radian), -np.sin(radian)], [np.sin(radian), np.cos(radian)]])


        self.corner_LU = np.array([ - self.pw,  + self.ph])
        self.corner_LD = np.array([ - self.pw,  - self.ph])
        self.corner_RU = np.array([ + self.pw,  + self.ph])
        self.corner_RD = np.array([ + self.pw,  - self.ph])
        self.corner_LU, self.corner_LD = np.dot(rotation_matrix, self.corner_LU)+np.array([self.px, self.py]), np.dot(rotation_matrix, self.corner_LD)+np.array([self.px, self.py])
        self.corner_RU, self.corner_RD = np.dot(rotation_matrix, self.corner_RU)+np.array([self.px, self.py]), np.dot(rotation_matrix, self.corner_RD)+np.array([self.px, self.py])
        
        self.search_inarea()
        self.search_shape()
 
        fig = plt.figure(figsize=(5,5))

        draw_in_x = [float(i) for i in np.array(self.inshape).T[1]]
        draw_in_y = [float(i) for i in np.array(self.inshape).T[2]]
        draw_out_x = [float(i) for i in np.array(self.outshape).T[1]]
        draw_out_y = [float(i) for i in np.array(self.outshape).T[2]]



        plt.plot([self.corner_LU[0], self.corner_LD[0]], [self.corner_LU[1], self.corner_LD[1]], c = 'red')
        plt.plot([self.corner_LU[0], self.corner_RU[0]], [self.corner_LU[1], self.corner_RU[1]], c = 'red')
        plt.plot([self.corner_RD[0], self.corner_RU[0]], [self.corner_RD[1], self.corner_RU[1]], c = 'red')
        plt.plot([self.corner_RD[0], self.corner_LD[0]], [self.corner_RD[1], self.corner_LD[1]], c = 'red')


        plt.scatter(draw_in_x, draw_in_y , c = 'black', s = 30/self.edge)
        plt.scatter(draw_out_x, draw_out_y, c = 'gray', s = 30/self.edge)
        plt.scatter(self.px, self.py, c = 'red', marker = 'x', s = 10)
        
        plt.xlim(self.px - 1.6*self.edge, self.px + 1.6*self.edge)
        plt.ylim(self.py - 1.6*self.edge, self.py + 1.6*self.edge)

        
        
        
        
        canvas = FigureCanvasTkAgg(fig, master=self.gui_rectangle)  # A tk.DrawingArea.
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
        
        
        lower_bound = searchkey - (self.edge*1.5)
        upper_bound = searchkey + (self.edge*1.5)
        
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
        l1 = self.line_func(self.corner_LU, self.corner_RU) 
        l2 = self.line_func(self.corner_RD, self.corner_RU) 

        l3 = self.line_func(self.corner_LU, self.corner_LD) 
        l4 = self.line_func(self.corner_RD, self.corner_LD) 

        
        for i in range(len(self.inarea)):
            x = self.inarea[i][1]
            y = self.inarea[i][2]

            if (x*l1[0]-y*l1[1]+l1[2]) >= 0 and (x*l3[0]-y*l3[1]+l3[2]) <= 0 and (x*l2[0]-y*l2[1]+l2[2]) <= 0 and (x*l4[0]-y*l4[1]+l4[2]) >= 0:

                self.inshape.append(self.inarea[i])
            else:
                self.outshape.append(self.inarea[i])

        self.inshape = np.array(self.inshape)
        self.outshape = np.array(self.outshape)
    
    def line_func(self, p1, p2):

        m1 = (p2[1] - p1[1])
        m2 = (p2[0] - p1[0]) 

        b = (m2*p2[1] - m1*p2[0])
        
        return np.array([m1, m2, b])




class myarray(np.ndarray):
    def __new__(cls, *args, **kwargs):
        return np.array(*args, **kwargs).view(myarray)
    def index(self, value):
        return np.where(self == value)



if __name__ == "__main__":
    G = GUI_plot_rectangle()
    G.gui()