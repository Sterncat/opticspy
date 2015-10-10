"""Simple Jones Vector class
see http://en.wikipedia.org/wiki/Jones_calculus
currently does not normalize the output
"""
from __future__ import division as __division__
import numpy as __np__
from numpy import pi as __pi__

def rotator(angle):
    s = __np__.sin(angle)
    c = __np__.cos(angle)
    rotator = __np__.matrix([[c,-s],[s,c]])
    return rotator

class Component(object):
    """Base Class for Waveplates and Filters"""
    def __init__(self, matrix):
        """Define component by its matrix"""
        self.matrix = matrix
    def factory(self,matrix):
        """Factory method to create this type again based on a matrix"""
        return Component(matrix)
    def rotate(self, angle):
        return Component(rotator(angle)*self.matrix*rotator(-angle))
    def v(self):
        return self.matrix
    def __repr__(self):
        return str(self.matrix)
    def __mul__(self, other):   
        return other.factory(self.v() * other.v())


class HalfWavePlate(Component):
    """Subclassed special case 1: HWP"""
    def __init__(self):
        self.matrix = __np__.matrix([[1,0],[0,-1]])
        
class QuaterWavePlate(Component):
    def __init__(self):
        self.matrix = __np__.matrix([[1,0],[0,1j]])
        
class Birefringence(Component):
    def __init__(self, w1, w2):
        self.matrix = __np__.matrix([[__np__.exp(1j*w1),0],[0,__np__.exp(1j*w2)]])
        
        

class Jones(object):
    def __init__(self, matrix):
        self.vector=matrix
    def v(self):
        return self.vector
    def __repr__(self):
        return str(self.vector)
    def factory(self,matrix):
        return Jones(matrix)
        
    
        
class Hpol(Jones):
    def __init__(self):
        self.vector=__np__.matrix([[1],[0]])
class Vpol(Jones):
    def __init__(self):
        self.vector=__np__.matrix([[0],[1]])    
        
class D1pol(Jones):
    def __init__(self):
        self.vector=__np__.matrix([[1],[1]]) 
class D2pol(Jones):
    def __init__(self):
        self.vector=__np__.matrix([[1],[-1]]) 
        
class C1pol(Jones):
    def __init__(self):
        self.vector=__np__.matrix([[1],[1j]]) 
class C2pol(Jones):
    def __init__(self):
        self.vector=__np__.matrix([[1],[-1j]]) 

if __name__ == "__main__":
    #Usage example
    print QuaterWavePlate().rotate(__pi__/4)*HalfWavePlate().rotate(__pi__/8)*D1pol()