import random

def packets ():

    real_pack = random.randint(1,100)
    print("RP :- " + str(real_pack))

    non_real_pack = random.randint(1,100)
    print("NRP :- " + str(non_real_pack))

    control_pack = random.randint(1,100)
    print("CP :- " + str(control_pack))

    time_out = random.uniform(0,10)
    print("TO :- " + str(time_out))

