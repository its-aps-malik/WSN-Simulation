import tkinter as tk
from tkinter import ttk
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
start_button = ttk.Button(win, text='Start', command=action)
start_button.grid(row=1,column=1)
win.mainloop()