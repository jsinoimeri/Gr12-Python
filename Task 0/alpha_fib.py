# Author: Jeton Sinoimeri
# Alpha_fib.py
# Date: Sept 25, 2010
from time import *
def alpha_fib(length):
    '''
    This function is basically like the fibonacci sequence however
    instead of a number sequence, it is with the alphabet using
    the chr() and ord() functions to make the sequence.
    '''       

    start = clock()
    char = ['a', 'b']
    if length <= 1:
        if length == 1:
            return '[a]'        
        else:
            return '[]'    
    
    elif length > 1:
        while len(char) < length:                                   
            if ord(char[-2]) +ord(char[-1]) -96 <= 122:
                char += [chr(ord(char[-2]) +ord(char[-1])  - 96)]            
           
            elif ord(char[-2]) +ord(char[-1]) -96 >= 123:
                char += [chr((ord(char[-2]) +ord(char[-1])  - 88) % 26 + 96)]
    
    end = clock()
    
    return char, end-start
print alpha_fib(25)