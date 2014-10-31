# Author: Jeton Sinoimeri
# Counter.py
# Date: Sept 25, 2010

from random import *
from time import *

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
counter = 0

for i in range(11):    
    for x in range(10):        
        
        rand_num = []        
        rand_num[:i] = num[:i]          # 'Locks' in the numbers
        
        for t in range(counter, 10):     # as i increases, one less random num
            number = str(randint(0,9))   # is calculated
            rand_num += [number]
        
        sleep(0.1)
        
        print ''.join(rand_num)
    
    counter +=1    