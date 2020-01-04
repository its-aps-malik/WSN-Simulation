
import os
from time import time
from packets import *
from csv import *



var = str(time())


def folder_creator():

    if os.path.exists('Results'):
        print('already exists')
    else:
        os.mkdir('Results')

    os.mkdir('Results/' + var + '/')

def f_creator(node_id):

    with open ( 'Results/' + var + "/node" + str(node_id+1) + ".csv", 'w', newline='') as f:
        csv_writer = writer(f)
        
        for i in range(10) :
            RP,NRP,CP,TO = packets() 

            csv_writer.writerow([RP, NRP, CP, TO])

        f.close()


