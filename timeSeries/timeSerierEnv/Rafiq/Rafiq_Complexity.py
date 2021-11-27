# example code for Rafiq
import numpy as np 
#import Complexity
import KC
a_binary_string = '01011010101010101010101110'

k = KC.calc_KC(a_binary_string)
k = np.round(k,1)

print ('the complexity of the string is ',k) # Test
