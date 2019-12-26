import tkinter as tk
from tkinter import ttk
from classnode import Node

no_of_nodes=0
l1=[]

win = tk.Tk()
win.title('WSN Optimization')

nodes_label = ttk.Label(win, text='No. of nodes : ')
nodes_label.grid(row=0, column=0)

nodes_var = tk.StringVar()

nodes_entrybox = ttk.Entry(win, width=10, textvariable = nodes_var)
nodes_entrybox.grid(row=0, column=1)

def action():

    no_of_nodes = nodes_var.get()

    for i in range(int(no_of_nodes)):
        l1.append(Node(i))
        print(l1[i].node_id)

start_button = ttk.Button(win, text='Start', command=action)
start_button.grid(row=1,column=1)

win.mainloop()