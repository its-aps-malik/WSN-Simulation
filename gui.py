import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('WSN Optimization')
nodes_label = ttk.Label(win, text='No. of nodes : ')
nodes_label.grid(row=0, column=0)
win.mainloop()