import random
from csv import *

def packets ():

    real_pack = random.randint(1,100)
    non_real_pack = random.randint(1,100)
    control_pack = random.randint(1,100)
    time_out = random.uniform(0,10)
    
    return(str(real_pack), str(non_real_pack), str(control_pack), str(time_out))
    



