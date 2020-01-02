import os
from csv import *
from packets import *
from classnode import *

def csv_file(node):

    with open ( "node" + str(node+1) + ".csv", 'w', newline='') as f:
        csv_writer = writer(f)
        
        for i in range(10) :
            RP,NRP,CP,TO = packets() 

            csv_writer.writerow([RP, NRP, CP, TO])

        f.close()