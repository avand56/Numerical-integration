import numpy as np
from math import sin, pi, cos
##################
def simpson(f, a, b, n):
    h=(b-a)/n
    s1=0
    for k in range(1,int(n/2 - 1)):
        s1+=4*f(a+(2*k-1)*h)
    s2=0
    for k in range(1,int(n/2)):
        s2+=2*f(a+2*k*h)
    return (h/3)*(f(a)+f(b)+s1+s2)
####################
#example:
def f(x):
    return 1.5*sin(x)**3
####################
#call function
sol=simpson(f, 0, pi, 100)
print(sol)   
         
###########
#an integral without an analytical solution
def f(x):
    return np.exp(-x**2)
sol2=simpson(f,0,3,100)
print(sol2)
