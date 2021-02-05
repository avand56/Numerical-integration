## Code to numerically integrate functions using trapezoid rule.
# can alter function and boundaries as you would like
# Note that more complex an poorly behaved functions work better with simpsons rule or trapezoid rule and not gaussian quadrature, which is better for simpler, smoother functions.
#Alex Vanderhoeff
##################
#import libraries
import numpy as np
from math import sin, pi, cos
##################
# can choose any function, i just chose this as example 
# eval h[1/2f(a)+1/2f(b)+ sum(f(a+kh))].
def f(x):
    return x**4-2*x+1 
##################
# Assign variables
N=10 # number of slices under curve. larger is more accurate but longer.
a=0
b=2 #integrating from a to b
h=(b-a)/N # each slice has width h
s= 0.5*f(a)+0.5*f(b)
###################
#kth slice, N total slices. s is area of the
for k in range(1,N):
    s+=f(a+k*h)
# note += adds another value to variables value and updates the variable to new value
###################
#print out answer
print(h*s)
#######################
















