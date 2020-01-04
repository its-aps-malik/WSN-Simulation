from sink import Drop
from gui import *
from gui import no_of_nodes
import random

temp_node_list=[]
network_node_list=[]
temp_node_list = node_list.copy()

def Network_creator():
    for i in range (temp_node_list):

        r1 = random.sample(temp_node_list)   # nodes list
        temp_node_list = temp_node_list
        r2 = random.sample(l2)    # sink list in which nodes will be added
        l2 = l2.append (r1)
