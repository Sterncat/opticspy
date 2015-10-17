import numpy as __np__
from numpy import cos as __cos__
from numpy import sin as __sin__
import matplotlib.pyplot as __plt__
from matplotlib import cm as __cm__
from matplotlib.ticker import LinearLocator as __LinearLocator__
from matplotlib.ticker import FormatStrFormatter as __FormatStrFormatter__

class Coefficient(object):
	"""
	Return a set of Seidel wavsfront aberrations Coefficient
	"""
	__coefficients__ = []
	__seidellist___=["W200 piston",
					 "W111 tilt",
					 "W020 defocus",
					 "W040 spherical",
					 "W131 coma",
					 "W222 astigmatism",
					 "W220 field curvature",
					 "W311 distortion"]
	def __init__(self, h=0, W200=0,W111=0,W020=0,W040=0,W131=0,W222=0,W220=0,W311=0):
		if type(h) == list:
			self.__coefficients__ = h
		else:
			self.__coefficients__ = [h,W200,W111,W020,W040,W131,W222,W220,W311]
	def outputcoefficient(self):
		return self.__coefficients__
	def listcoefficient(self):
		"""
		------------------------------------------------
		listcoefficient():

		List the coefficient in Coefficient

		------------------------------------------------
		"""
		print "h="+str(self.__coefficients__[0])
		for i in range(len(self.__coefficients__)-1):
			print self.__seidellist___[i][0:4]+"="+\
				str(self.__coefficients__[i+1])+self.__seidellist___[i][4:]
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
		


def __seidelpolar__(coefficient,r,u):
	h = coefficient[0]
	W = coefficient
	W200 = W[1] * h**2
	W111 = W[2] * h*r*__cos__(u)
	W020 = W[3] * r**2
	W040 = W[4] * r**4
	W131 = W[5] * h*r**3*__cos__(u)
	W222 = W[6] * h**2*r**2*__cos__(u)
	W220 = W[7] * h**2*r**2
	W311 = W[8] * h**3*r*__cos__(u)
	W = W200+W111+W020+W040+W131+W222+W220+W311

	return W

