from math import *
from TurtleWorld import *

def circle(t,r):
    circumference=2*math.pi*r
    n=int(circumference/3)+1
    length=circunference/n
    polygon(t,n,length)

circle(t,50)   
