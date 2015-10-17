import numpy as __np__
from numpy import cos as __cos__
from numpy import sin as __sin__
from numpy import arctan2 as __arctan2__
from numpy import sqrt as __sqrt__
import matplotlib.pyplot as __plt__
from matplotlib import cm as __cm__
from matplotlib.ticker import LinearLocator as __LinearLocator__
from matplotlib.ticker import FormatStrFormatter as __FormatStrFormatter__
import tools as __tools__


class Coefficient(object):
	"""
	Return a set of Seidel wavsfront aberrations Coefficient
	"""
	__coefficients__ = []
	__seidellist___=["Ap Piston",
					"At Tilt",
					"Ad Defocus",
		 			"As Astigmatism",
		 			"Ac Coma",
		 			"As Spherical"]
	def __init__(self,Ap=0,Bp=0,At=0,Bt=0,Ad=0,Bd=0,Aa=0,Ba=0,Ac=0,Bc=0,As=0,Bs=0):
		if type(Ap) == list:
			self.__coefficients__ = Ap
		else:
			self.__coefficients__ = [[Ap,Bp],[At,Bt],[Ad,Bd],[Aa,Ba],[Ac,Bc],[As,Bs]]
	def outputcoefficient(self):
		return self.__coefficients__

		
	def seidelsurface(self, label = True, zlim=[], matrix = False):
		r1 = __np__.linspace(0, 1, 100)
		u1 = __np__.linspace(0, 2*__np__.pi, 100)
		[u,r] = __np__.meshgrid(u1,r1)
		X = r*__cos__(u)
		Y = r*__sin__(u)
		W = __seidelpolar__(self.__coefficients__,r,u)
		fig = __plt__.figure(figsize=(12, 8), dpi=80)
		ax = fig.gca(projection='3d')
		surf = ax.plot_surface(X, Y, W, rstride=1, cstride=1, cmap=__cm__.RdYlGn,
	        linewidth=0, antialiased=False, alpha = 0.6)
		fig.colorbar(surf, shrink=1, aspect=30)
		__plt__.show()



	def twyman_green(self, lambda_1 = 632, PR = 1):
		lambda_1 = lambda_1*(10**-9)
		A = self.__coefficients__
		r = __np__.linspace(-PR, PR, 400)
		x, y = __np__.meshgrid(r,r) 
		OPD = __seidelcartesian__(A,x,y)*2/PR
		ph = 2 * __np__.pi * OPD
		I1 = 1
		I2 = 1
		Ixy = I1 + I2 + 2 * __np__.sqrt(I1*I2) * __np__.cos(ph)
		__tools__.makecircle(Ixy, r, PR) 
		fig = __plt__.figure(figsize=(9, 6), dpi=80)
		__plt__.imshow(-Ixy, extent=[-PR,PR,-PR,PR])
		__plt__.set_cmap('Greys')
		__plt__.show()


def __seidelpolar__(coefficient,r,u):
	W = coefficient
	h = 1
	Ap = W[0][0] * h**2
	At = W[1][0] * h*r*__cos__(u-W[1][1]*__np__.pi/180)
	Ad = W[2][0] * r**2
	Aa = W[3][0] * h**2*r**2*__cos__(u-W[3][1]*__np__.pi/180)
	Ac = W[4][0] * h*r*__cos__(u-W[4][1]*__np__.pi/180)
	As = W[5][0] * r**4

	W = Ap+At+Ad+Aa+Ac+As
	return W

def __seidelcartesian__(coefficient,x,y):
	W = coefficient
	h = 1
	u = __arctan2__(y,x)
	r = __sqrt__(x**2+y**2)
	W = __seidelpolar__(coefficient,r,u)
	return W
