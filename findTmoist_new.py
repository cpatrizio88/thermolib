"""This is the docstring for the findTmoist.py module. This module
contains two functions: findTmoist and thetaEchange."""

import numpy as np
from constants import constants
from theta import theta
from wsat import wsat 
import thermo
from scipy import optimize 
#from thetaes import thetaes

def thetaes(T, p):
    """
    thetaes(T, p)

    Calculates the pseudo equivalent potential temperature of an air
    parcel.

    Parameters
    - - - - - -
    T : float
        Temperature (K).
    p : float
        Pressure (Pa).


    Returns
    - - - -
    thetaep : float
        Pseudo equivalent potential temperature (K).


    Notes
    - - -
    It should be noted that the pseudo equivalent potential
    temperature (thetaep) of an air parcel is not a conserved
    variable.


    References
    - - - - - -
    Emanuel 4.7.9 p. 132


    Examples
    - - - - -
    >>> thetaes(300., 8.e4)
    412.97362667593831
    
    """
    c = constants();
    # The parcel is saturated - prohibit supersaturation with Td > T.
    Tlcl = T;
    wv = wsat(T, p);
    thetaval = theta(T, p, wv);
    power = 0.2854 * (1 - 0.28 * wv);
    thetaep = thetaval * np.exp(wv * (1 + 0.81 * wv) * \
                                (3376. / Tlcl - 2.54))\
    
    #if thetaep > 550:
   #    thetaep = 550
                                
    return thetaep

def findTmoist(thetaE0, press):
    """
    findTmoist(thetaE0, press)
    
    Calculates the temperatures along a moist adiabat.
    
    Parameters
    - - - - - -
    thetaE0 : float
        Initial equivalent potential temperature (K).
    press : float or array_like
        Pressure (Pa).

    Returns
    - - - -
    Temp : float or array_like
        Temperature (K) of thetaE0 adiabat at 'press'.

    Examples
    - - - - -
    >>> findTmoist(300., 8.e4)
    270.59590841970277
    
    >>> findTmoist(330., 800)
    83.1818
    
    """

    # First determine if press can be indexed
    try: len(press)
    except: #press is a single value
        Temp = optimize.zeros.brenth(thetaEchange, 50, 450,  \
                                        (thetaE0, press), maxiter=1000);
    else: #press is a vector           
        Temp = []
        press = list(press)        
        for i in press:            
            # This assumes that the dewpoint is somewherebetween 
            # 250K and 350K.
            Temp.append(optimize.zeros.brenth(thetaEchange, 50, \
                                                 450, (thetaE0, i)), maxiter=1000);
            #{'in Tmoist: ',i, result(i)}  
        
    return Temp
    

def thetaEchange(Tguess, thetaE0, press):
    """
    thetaEchange(Tguess, thetaE0, press)

    Evaluates the equation and passes it back to brenth.

    Parameters
    - - - - - -
    Tguess : float
        Trial temperature value (K).
    ws0 : float
        Initial saturated mixing ratio (kg/kg).
    press : float
        Pressure (Pa).

    Returns
    - - - -
    theDiff : float
        The difference between the values of 'thetaEguess' and
        'thetaE0'. This difference is then compared to the tolerance
        allowed by brenth.
        
    """
    q = wsat(Tguess, press)
    #assume no liquid water
    thetaEguess = thermo.theta_e(Tguess, press, q, 0);
    
    #when this result is small enough we're done
    theDiff = thetaEguess - thetaE0;
    return theDiff


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
