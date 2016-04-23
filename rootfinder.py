#!/usr/bin/env python

import numpy
from scipy import optimize

def find_interval(f, x, *args):
    x1 = x
    x2 = x
    if x == 0.:
        dx = 1./50.
    else:
        dx = x/50.
        
    maxiter = 40
    twosqrt = numpy.sqrt(2)
    a = x
    fa = f(a, *args)
    b = x
    fb = f(b, *args)
    
    for i in range(maxiter):
        dx = dx*twosqrt
        a = x - dx
        fa = f(a, *args)
        b = x + dx
        fb = f(b, *args)
        if (fa*fb < 0.): return (a, b)
        
    raise "Couldn't find a suitable range."

# This function evaluates a new point, sets the y range,
# and tests for convergence
def get_y(x, f, eps, ymax, ymin, *args):
    y = f(x, *args)
    ymax = max(ymax, y)
    ymin = min(ymin, y)
    converged = (abs(y) < eps*(ymax-ymin))
    return (y, ymax, ymin, converged)

def fzero(the_func, root_bracket, *args, **parms):
    # the_func is the function we wish to find the zeros of
    # root_bracket is an initial guess of the zero location 
    # root_bracket must be a sequence of two floats specifying a range 
    #(the_func must differ in sign when evaluated at these points)
    # Note: brenth() seems to require a bracketing interval, 
    # so a single float can't be passed to fzero, as in MATLAB.
    # *args contains any other parameters needed for f
    # **parms can be xtol (allowable error) or maxiter (max number of iterations.)
    answer=optimize.zeros.brenth(the_func, root_bracket[0], root_bracket[1], *args, **parms)
    return answer
    
def testfunc(x):
    return numpy.sin(x)
     
 
if __name__=="__main__":
    f = testfunc
    x = [-1,1]
    print fzero(f, x)
    print fzero(f, x, xtol=1.e-300, maxiter=80)
