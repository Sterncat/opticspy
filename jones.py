"""Simple Jones Vector class
see http://en.wikipedia.org/wiki/Jones_calculus
currently does not normalize the output
"""
import numpy as np
from numpy import pi

def rotator(angle):
    s = np.sin(angle)
    c = np.cos(angle)
    rotator = np.matrix([[c,-s],[s,c]])

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
        self.matrix = np.matrix([[1,0],[0,-1]])
        
class QuaterWavePlate(Component):
    def __init__(self):
        self.matrix = np.matrix([[1,0],[0,1j]])
        
class Birefringence(Component):
    def __init__(self, w1, w2):
        self.matrix = np.matrix([[np.exp(1j*w1),0],[0,np.exp(1j*w2)]])
        
        

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
        self.vector=np.matrix([[1],[0]])
class Vpol(Jones):
    def __init__(self):
        self.vector=np.matrix([[0],[1]])    
        
class D1pol(Jones):
    def __init__(self):
        self.vector=np.matrix([[1],[1]]) 
class D2pol(Jones):
    def __init__(self):
        self.vector=np.matrix([[1],[-1]]) 
        
class C1pol(Jones):
    def __init__(self):
        self.vector=np.matrix([[1],[1j]]) 
class C2pol(Jones):
    def __init__(self):
        self.vector=np.matrix([[1],[-1j]]) 

if __name__ == "__main__":
    #Usage example
    print QuaterWavePlate().rotate(pi/4)*HalfWavePlate().rotate(pi/8)*D1pol()