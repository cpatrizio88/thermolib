import numpy as np
from esatnew import esat
from constants import constants

c = constants()

def wsat(T, p):
    
    es = esat(T)
    wsat =  c.eps * es/ (p - es)
    return wsat 

    
    