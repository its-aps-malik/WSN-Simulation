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
        