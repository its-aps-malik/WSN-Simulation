import tkinter as tk
from tkinter import ttk
from classnode import *
from file_creator import *

# import os
# from time import time

no_of_nodes=0
node_list=[]

# var = str(time())

# if os.path.exists('Results'):
#     print('already exists')
# else:
#     os.mkdir('Results')

# os.mkdir('Results/' + var + '/')


def gui_loader():


    win = tk.Tk()
    win.title('WSN Optimization')

    nodes_label = ttk.Label(win, text='No. of nodes : ')
    nodes_label.grid(row=0, column=0)

    nodes_var = tk.StringVar()

    nodes_entrybox = ttk.Entry(win, width=10, textvariable = nodes_var)
    nodes_entrybox.grid(row=0, column=1)

    def action():

        no_of_nodes = nodes_var.get()
        print(f' No. of nodes is {no_of_nodes}')

        for i in range(int(no_of_nodes)):
            node_list.append(Node(i))
            #print(i)

            f_creator(i)
        




        for j in  range(int(no_of_nodes)):            
            node_list[j].start()  
            
            
    start_button = ttk.Button(win, text='Start', command=action)                        
    start_button.grid(row=1,column=1)

    win.mainloop()
