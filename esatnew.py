import numpy as np

def esat(T):

     Tc = T - 273.15
     es = 611.2 * np.exp(17.67 * Tc / (Tc + 243.5))
     return es
