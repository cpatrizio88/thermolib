from rootfinder import fzero
from new_thermo import theta, invtheta, Tdfind


def findLCL0(wv, press0, temp0):
    """
    
    findLCL0(wv, press0, temp0)
   
    Finds the temperature and pressure at the lifting condensation
    level (LCL) of an air parcel (using a rootfinder).

    Parameters
    - - - - - -
    wv : float
         Mixing ratio (K).
    temp0 : float
           Temperature (K).
    press0: float
            pressure (Pa)

    Returns
    - - - - -
    plcl : float
        Pressure at the LCL (Pa).
    Tlcl : float
        Temperature at the LCL (K).
    
    Raises
    - - - -
    NameError
        If the air is saturated at a given wv, temp0 and press0 (i.e. Tdew(wv, press0) >= temp0)
        
    Tests
    - - - - -
    >>> Td = Tdfind(5., 9.e4)
    >>> Td > 280.
    True
    >>> findLCL0(5., 9.e4, 280.)
    Traceback (most recent call last):
        ...
    NameError: parcel is saturated at this pressure
    >>> p1, T1 =  findLCL0(0.001, 9.e4, 280.)
    >>> print T1, p1
    250.226034799 60692.0428535
    
    """
    
    
    Td = Tdfind(wv, press0)
    
    if (Td >= temp0):
        #raise NameError('parcel is saturated at this pressure')
        return press0, temp0
    
    theta0 = theta(temp0, press0, wv)
   
    #evalzero = lambda pguess: lclzero(pguess, wv, theta0)
    
    #will return plcl, Tlcl when Tchange returns approx. 0 
    #(i.e. when the parcel temperature = Td)
    plcl = fzero(Tchange, [1000*100, 200*100], (wv, theta0))
    Tlcl = invtheta(theta0, plcl, wv)
    
    return plcl, Tlcl
    
    
def Tchange(pguess, wv0, theta0):
    """
    
    Returns the result of the equation T - Td.  
    
    Parameters 
    - - - - - -
    pguess: float, a guess at the pressure at the LCL (input via fzero) (Pa)
    wv0: float, mixing ratio of the parcel (kg/kg)
    theta0: float, potential temperature of the parcel
    
    Returns 
    - - - - - -
    
    T - Td: float, T is the temperature on the theta0 dry adiabat, 
    and Td is the dewpoint temperature of a parcelat mixing ratio wv0 and pressure pguess.
    
    """
    T = invtheta(theta0, pguess, wv0)
    Td = Tdfind(wv0, pguess)
    return T - Td

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()