#
# ps7pr2.py (Problem Set 7, Problem 2)
#
# Estimating the value of pi
#
# Computer Science 111
#

import random
import math

def throw_dart():
    """ Simulates the throwing of a random dart at a 2 x 2 square that.
        is centered on the origin. Returns True if the dart hits a circle
        inscribed in the square, and False if the dart misses the circle.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1.0:
        return True
    else:
        return False

### PUT YOUR WORK FOR PROBLEM 2 BELOW. ###

def est_pi1(error):
    """ takes a positive floating-point input, error, and returns the number of
        dart throws needed to produce an estimate of pi that is less than error
        away from the "actual" value of pi """
    num_darts_thrown = 0
    num_darts_circle = 0
    circle_area = 0
    while abs(math.pi - circle_area) >= error:
        throw_dart()
        if throw_dart(): 
            num_darts_circle += 1
        num_darts_thrown += 1
        circle_area = (4*num_darts_circle)/num_darts_thrown
        print(num_darts_circle, 'hits out of', num_darts_thrown, 'so that pi is', circle_area)
    return num_darts_thrown

def est_pi2(n):
    """ takes a positive integer n and returns an estimate of pi that is based
        on n randomly thrown darts """
    num_darts_thrown = 0
    num_darts_circle = 0
    for num in range(1,n+1):
        throw_dart()
        if throw_dart(): 
            num_darts_circle += 1
        num_darts_thrown += 1
        circle_area = (4*num_darts_circle)/num_darts_thrown
        print(num_darts_circle, 'hits out of', num_darts_thrown, 'so that pi is', circle_area)
    return circle_area        
    
