from threading import *
from time import *
from packets import packets
from file_creator import *




class Node (Thread):
    def __init__(self, node_id, level = 999, s_energy = 0, r_energy = 0, packetsa_to_send = 100, nodes_to_send = None, connected_list = []):   
        Thread.__init__(self)
        self.node_id = node_id
        self.level = level
        self.s_energy = s_energy
        self.r_energy = r_energy
        self.packets_to_send = packetsa_to_send
        self.nodes_to_send = nodes_to_send
        self.connected_list = connected_list



    def run (self):
        flag=True
        
        i=0

        while flag :
            #print (self.node_id, end=" ")
            packets()
            i=i+1
            sleep(0.1)
            if i > 10:
                i=0
                flag= False
        