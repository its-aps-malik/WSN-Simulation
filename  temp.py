######### GUI


import tkinter as tk
from tkinter import ttk
#from classnode import *
# import os
# from time import time

no_of_nodes=0
#l1=[]

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

        


        #for i in range(int(no_of_nodes)):
        #     l1.append(Node(i))
        #     #print(l1[i].node_id)  
            
        # for j in  range(int(no_of_nodes)):
            
        #     l1[j].start()  
            
    start_button = ttk.Button(win, text='Start', command=action)                        
    start_button.grid(row=1,column=1)

    win.mainloop()










    ################# classnode#########




from threading import *
from time import *
from packets import packets
from files import *


class Node (Thread):
    def __init__(self, node_id):   
        Thread.__init__(self)
        self.node_id = node_id

    def run (self):
        flag=True
        
        i=0
        csv_file(self.node_id)
        while flag :
            #print (self.node_id, end=" ")
            packets()
            i=i+1
            sleep(0.1)
            if i > 10:
                i=0
                flag= False
        





################### FILE##########



import os
from csv import *
from packets import *
from classnode import *
#import gui

def csv_file(node):

    with open ( 'Results/' + "node" + str(node+1) + ".csv", 'w', newline='') as f:
        csv_writer = writer(f)
        
        for i in range(10) :
            RP,NRP,CP,TO = packets() 

            csv_writer.writerow([RP, NRP, CP, TO])

        f.close()






################## FILE_CREATOR








var = str(time())

if os.path.exists('Results'):
    print('already exists')
else:
    os.mkdir('Results')

os.mkdir('Results/' + var + '/')









################ PACKEST 



import random
from csv import *

def packets ():

    real_pack = random.randint(1,100)
    non_real_pack = random.randint(1,100)
    control_pack = random.randint(1,100)
    time_out = random.uniform(0,10)
    
    return(str(real_pack), str(non_real_pack), str(control_pack), str(time_out))
    




