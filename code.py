import numpy as np
import matplotlib.pyplot as plt
from math import comb
# A = Odd number on First throw :
prob_A = 1/2
# B = Odd number on second throw :
prob_B = 1/2
# A cap B = Odd number on the First & Second throw :
prob_A_cap_B = 1/4

#To find if the events are independent or not

if(prob_A*prob_B == prob_A_cap_B):

    print('A and B are independent events')
else:
    print('A and B are not independent events')