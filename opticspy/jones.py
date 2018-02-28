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
    return __np__.matrix([[c,-s],[s,c]])

    
class Component(__np__.matrix):

    def __new__(self,matrix):
        return super(Component,self).__new__(self,matrix)
    
    def rotate(self, angle):
        return rotator(angle)*self*rotator(-angle)

    
def HalfWavePlate():
    return Component([[1,0],[0,-1]])
def QuaterWavePlate():
    return Component([[1,0],[0,1j]])
def Birefringence( w1, w2):
    return Component([[__np__.exp(1j*w1),0],[0,__np__.exp(1j*w2)]])


def Hpol():
    return __np__.matrix([[1],[0]])
def Vpol():
    return __np__.matrix([[0],[1]])
def D1pol():
    return __np__.matrix([[1],[1]])/__np__.sqrt(2)
def D2pol():
    return __np__.matrix([[1],[-1]])/__np__.sqrt(2)
def C1pol():
    return __np__.matrix([[1],[1j]])/__np__.sqrt(2)
def C2pol():
    return __np__.matrix([[1],[-1j]])/__np__.sqrt(2)
    

def PolarizerH():
    return Component(Hpol()*Hpol().T)
def PolarizerV():
    return Component(Vpol()*Vpol().T)


if __name__ == "__main__":
    #Usage example
    print(QuaterWavePlate().rotate(__pi__/4)*HalfWavePlate().rotate(__pi__/8)*D1pol())

