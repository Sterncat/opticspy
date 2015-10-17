from __future__ import division as __division__
import numpy as __np__
from numpy import sqrt as __sqrt__
from numpy import cos as __cos__
from numpy import sin as __sin__
import matplotlib.pyplot as __plt__
from matplotlib import cm as __cm__
from mplot3d import Axes3D as __Axes3D__
from matplotlib.ticker import LinearLocator as __LinearLocator__
from matplotlib.ticker import FormatStrFormatter as __FormatStrFormatter__

class Coefficient(object):
	"""
	Return a set of Asphere Coefficient
	R,k,a2,a3,a4,a5,a6,a7,a8,a9,a10
	"""
	__coefficients__ = []
	def __init__(self,R=0,k=0,a2=0,a3=0,a4=0,a5=0,a6=0,a7=0,a8=0,a9=0,a10=0):

		if type(R) == list:
			self.__coefficients__ = R + [0]*(11-len(R))
		else:
			self.__coefficients__ = [R,k,a2,a3,a4,a5,a6,a7,a8,a9,a10]
			
	def outputcoefficient(self):
		return self.__coefficients__

	def aspheresurface(self):
		"""
		Show the surface of an asphere.
		=============================================================
		Try: 
		A = opticspy.asphere.Coefficient(R=50,a2=0.18*10**(-8),a3 = 0.392629*10**(-13))

		"""
		R = self.__coefficients__[0]
		theta = __np__.linspace(0, 2*__np__.pi, 100)
		rho = __np__.linspace(0, R, 100)
		[u,r] = __np__.meshgrid(theta,rho)
		X = r*__cos__(u)
		Y = r*__sin__(u)
		Z = __aspherepolar__(self.__coefficients__,r)
		fig = __plt__.figure(figsize=(12, 8), dpi=80)
		ax = fig.gca(projection='3d')
		surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=__cm__.RdYlGn,
	        linewidth=0, antialiased=False, alpha = 0.6)
		__plt__.show()
		return 0

	def aspherematrix(self):
		l = 100
		R = self.__coefficients__[0]
		x1 = __np__.linspace(-R, R, l)
		[X,Y] = __np__.meshgrid(x1,x1)
		r = __sqrt__(X**2+Y**2)
		Z = __aspherepolar__(self.__coefficients__,r)
		for i in range(l):
			for j in range(l):
				if x1[i]**2+x1[j]**2 > R**2:
					Z[i][j] = 0
		fig = __plt__.figure(figsize=(12, 8), dpi=80)
		ax = fig.gca(projection='3d')
		surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=__cm__.RdYlGn,
	        linewidth=0, antialiased=False, alpha = 0.6)
		__plt__.show()
		return Z

	def asphereline(self):
		R,k,a2,a3,a4,a5,a6,a7,a8,a9,a10 = self.__coefficients__
		r = __np__.linspace(-R,R,100)
		C = 1/R
		Z = C*r**2*(1+__sqrt__(1-(1+k)*r**2*C**2)) + a2*r**4 + a3*r**6 + a4*r**8 + \
		+ a5*r**10 + a6*r**12 + a7*r**14 + a8*r**16 + a9*r**18 + a10*r**20
		Z = -Z
		fig = __plt__.figure(figsize=(12, 8), dpi=80)
		__plt__.plot(r,Z)
		__plt__.axis('equal')
		__plt__.show()

def __aspherepolar__(coefficient,r):
	R,k,a2,a3,a4,a5,a6,a7,a8,a9,a10 = coefficient
	C = 1/R
	Z = C*r**2*(1+__sqrt__(1-(1+k)*r**2*C**2)) + a2*r**4 + a3*r**6 + a4*r**8 + \
		+ a5*r**10 + a6*r**12 + a7*r**14 + a8*r**16 + a9*r**18 + a10*r**20
	return -Z












