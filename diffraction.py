import numpy as __np__
from numpy import sin as __sin__
from numpy import cos as __cos__
import matplotlib.pyplot as __plt__

def doubleslit(b=0.1,a=0.4,lambda_1=632,z=0.5):
    """
    Return a Young's doubleslit(Frauhofer Diffraction)
    Input:
    --------------------------------
    b: slit of width in mm
    a: slit separation of in mm
    lambda_1: wavelength in nm
    z: slit-to-screen distance in m.
    """
    lambda_1 = float(lambda_1)
    theta = __np__.linspace(-0.04,0.04,1000)
    theta1 = __np__.ones(100)
    [theta,theta1] = __np__.meshgrid(theta,theta1)
    beta = __np__.pi*(b/1000)/(lambda_1/(10**9))*__sin__(theta)
    alpha = __np__.pi*(a/1000)/(lambda_1/(10**9))*__sin__(theta)
    y = 4*(__sin__(beta)**2/(beta**2)*__cos__(alpha)**2)
    fig = __plt__.figure(1,figsize=(12,8), dpi=80)
    __plt__.imshow(-y)
    __plt__.set_cmap('Greys')
    __plt__.show()
    
    theta = __np__.linspace(-0.04,0.04,1000)
    beta = __np__.pi*(b/1000)/(lambda_1/(10**9))*__sin__(theta)
    alpha = __np__.pi*(a/1000)/(lambda_1/(10**9))*__sin__(theta)
    y = 4*(__sin__(beta)**2/(beta**2)*__cos__(alpha)**2)
    fig = __plt__.figure(2,figsize=(12, 8), dpi=80)
    __plt__.plot(theta*z*1000,y)
    __plt__.show()

