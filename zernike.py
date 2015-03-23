import numpy as __np__
from numpy import cos as __cos__
from numpy import sin as __sin__
import matplotlib.pyplot as __plt__
from mpl_toolkits.mplot3d import Axes3D as __Axes3D__
from matplotlib import cm as __cm__
from matplotlib.ticker import LinearLocator as __LinearLocator__
from matplotlib.ticker import FormatStrFormatter as __FormatStrFormatter__


class Coefficient(object):
	"""
	Return a set of Zernike Polynomials Coefficient

	These are the operations that Coefficient support:
	------------------------------------------------
	listcoefficient():

	List the coefficient in Coefficient

	------------------------------------------------
	zernikelist():

	List all Zernike Polynomials

	------------------------------------------------
	zernikesurface(self, label_1 = True):

	Return a 3D Zernike Polynomials surface figure

	label_1: default show label

	------------------------------------------------
	zernikemap(self, label_1 = True):

	Return a 2D Zernike Polynomials map figure

	label_1: default show label

	------------------------------------------------
	zernikeline()

	Return a 1D cutoff through x and y axis of a 3D 
	Zernike Polynomials surface figure
	
	================================================
	Internal method:
	------------------------------------------------
	__init__(self, 
			Z0=0, Z1=0, Z2=0, Z3=0, Z4=0, Z5=0, Z6=0, Z7=0, 
			Z8=0, Z9=0, Z10=0, Z11=0, Z12=0, Z13=0, Z14=0, 
			Z15=0, Z16=0, Z17=0, Z18=0, Z19=0, Z20=0, Z21=0, 
			Z22=0, Z23=0, Z24=0, Z25=0, Z26=0, Z27=0, Z28=0, 
			Z29=0, Z30=0, Z31=0, Z32=0, Z33=0, Z34=0, Z35=0):
	
	Initialize function
	------------------------------------------------
	__zernikepolar__(coefficient,r,u):

	Return combined aberration

	Zernike Polynomials Caculation in polar coordinates

	coefficient: Zernike Polynomials Coefficient from input
	r: rho in polar coordinates
	u: theta in polar coordinates

	------------------------------------------------
	__zernikecartesian__(coefficient,x,y):

	Return combined aberration

	Zernike Polynomials Caculation in Cartesian coordinates

	coefficient: Zernike Polynomials Coefficient from input
	x: x in Cartesian coordinates
	y: y in Cartesian coordinates
	"""

	__coefficients__ = []
	__zernikelist__ = [ "Piston or Bias",
						"Tilt x",
						"Tilt y",
						"Power",
						"Astigmatism x",
						"Astigmatism y",
						"Coma x",
						"Coma y",
						"Primary Spherical",
						"Trefoil x",
						"Trefoil y",
						"Secondary Astigmatism x",
						"Secondary Astigmatism y",
						"Secondary Coma x",
						"Secondary Coma y",
						"Secondary Spherical",
						"Tetrafoil x",
						"Tetrafoil y",
						"Secondary Trefoil x",
						"Secondary Trefoil y",
						"Tertiary Astigmatism x",
						"Tertiary Astigmatism y",
						"Tertiary Coma x",
						"Tertiary Coma y",
						"Tertiary Spherical",
						"Pentafoil x",
						"Pentafoil y",
						"Secondary Trefoil x",
						"Secondary Trefoil y",
						"Tertiary Trefoil x",
						"Tertiary Trefoil y",
						"Quaternary Astigmatism x",
						"Quaternary Astigmatism y",
						"Quaternary Coma x",
						"Quaternary Coma y",
						"Quaternary Spherical"]

	def __init__(self, 
			Z0=0, Z1=0, Z2=0, Z3=0, Z4=0, Z5=0, Z6=0, Z7=0, \
			Z8=0, Z9=0, Z10=0, Z11=0, Z12=0, Z13=0, Z14=0, \
			Z15=0, Z16=0, Z17=0, Z18=0, Z19=0, Z20=0, Z21=0, \
			Z22=0, Z23=0, Z24=0, Z25=0, Z26=0, Z27=0, Z28=0, \
			Z29=0, Z30=0, Z31=0, Z32=0, Z33=0, Z34=0, Z35=0):

		self.__coefficients__ = [Z0, Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, \
					Z11, Z12, Z13, Z14, Z15, Z16, Z17, Z18, Z19, \
					Z20, Z21, Z22, Z23, Z24, Z25, Z26, Z27, Z28, \
					Z29, Z30, Z31, Z32, Z33, Z34, Z35,]
	def listcoefficient(self):
		m = 0
		label1 = ""
		label2 = ""
		for i in self.__coefficients__:
			if i != 0:
				print 'Z'+str(m)+' = ',i,self.__zernikelist__[m]
				label1 = label1 + 'Z'+str(m)+' = '+str(i)+"\n"
				label2 = label2 + 'Z'+str(m)+' = '+str(i)+"  "
			m = m + 1
		return [label1,label2]

	def zernikelist(self):
		m = 0
		for i in self.__zernikelist__:
			print "Z"+str(m)+":"+i
			m = m + 1

	def zernikesurface(self, label_1 = True):
		theta = __np__.linspace(0, 2*__np__.pi, 50)
		rho = __np__.linspace(0, 1, 50)
		[u,r] = __np__.meshgrid(theta,rho)
		X = r*__cos__(u)
		Y = r*__sin__(u)
		Z = __zernikepolar__(self.__coefficients__,r,u)
		fig = __plt__.figure()
		ax = fig.gca(projection='3d')
		surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=__cm__.RdYlGn,
	        linewidth=0, antialiased=False, alpha = 0.6)
		v = max(abs(Z.max()),abs(Z.min()))
		ax.set_zlim(-v, v)
		ax.zaxis.set_major_locator(__LinearLocator__(10))
		ax.zaxis.set_major_formatter(__FormatStrFormatter__('%.02f'))

		cset = ax.contourf(X, Y, Z, zdir='z', offset=-v, cmap=__cm__.RdYlGn)

		fig.colorbar(surf, shrink=0.5, aspect=5)

		label = self.listcoefficient()[0]
		if label_1 == True:
			__plt__.title('Zernike Polynomials Surface',fontsize=15)
			ax.text2D(0.02, 0.1, label, transform=ax.transAxes)
		__plt__.show()

	def zernikemap(self, label_1 = True):
		theta = __np__.linspace(0, 2*__np__.pi, 100)
		rho = __np__.linspace(0, 1, 100)
		[u,r] = __np__.meshgrid(theta,rho)
		X = r*__cos__(u)
		Y = r*__sin__(u)
		Z = __zernikepolar__(self.__coefficients__,r,u)
		fig = __plt__.figure()
		ax = fig.gca()
		im = __plt__.pcolormesh(X, Y, Z, cmap=__cm__.RdYlGn)

		if label_1 == True:
			__plt__.title('Zernike Polynomials Surface Map',fontsize=15)
			ax.set_xlabel(self.listcoefficient()[1])

		__plt__.colorbar()
		__plt__.show()

	def zernikeline(self):
		X = __np__.linspace(-1, 1, 100)
		Y = __np__.linspace(-1, 1, 100)
		ZX = __zernikecartesian__(self.__coefficients__,X,0)
		ZY = __zernikecartesian__(self.__coefficients__,0,Y)
		fig = __plt__.figure()
		ax = fig.gca()
		__plt__.plot(X,ZX)
		__plt__.plot(Y,ZY)
		__plt__.grid()
		__plt__.show()

def __zernikepolar__(coefficient,r,u):
	Z = coefficient
	Z0  =  Z[0]  * 1                                 
	Z1  =  Z[1]  * r*__cos__(u)
	Z2  =  Z[2]  * r*__sin__(u)
	Z3  =  Z[3]  * (2*r**2-1)
	Z4  =  Z[4]  * r**2*__cos__(2*u)
	Z5  =  Z[5]  * r**2*__sin__(2*u)
	Z6  =  Z[6]  * (3*r**2-2)*r*__cos__(u)
	Z7  =  Z[7]  * (3*r**2-2)*r*__sin__(u)
	Z8  =  Z[8]  * (1-6*r**2+6*r**4)
	Z9  =  Z[9]  * r**3*__cos__(3*u)
	Z10 =  Z[10] * r**3*__sin__(3*u)
	Z11 =  Z[11] * (4*r**2-3)*r**2*__cos__(2*u)
	Z12 =  Z[12] * (4*r**2-3)*r**2*__sin__(2*u)
	Z13 =  Z[13] * (10*r**4-12*r**2+3)*r*__cos__(u)
	Z14 =  Z[14] * (10*r**4-12*r**2+3)*r*__sin__(u)
	Z15 =  Z[15] * (20*r**6-30*r**4+12*r**2-1)
	Z16 =  Z[16] * r**4*__cos__(4*u)
	Z17 =  Z[17] * r**4*__sin__(4*u)
	Z18 =  Z[18] * (5*r**2-4)*r**3*__cos__(3*u)
	Z19 =  Z[19] * (5*r**2-4)*r**3*__sin__(3*u)
	Z20 =  Z[20] * (15*r**4-20*r**2+6)*r**2*__cos__(2*u)
	Z21 =  Z[21] * (15*r**4-20*r**2+6)*r**2*__sin__(2*u)
	Z22 =  Z[22] * (35*r**6-60*r**4+30*r**2-4)*r*__cos__(u)
	Z23 =  Z[23] * (35*r**6-60*r**4+30*r**2-4)*r*__sin__(u)
	Z24 =  Z[24] * (70*r**8-140*r**6+90*r**4-20*r**2+1)
	Z25 =  Z[25] * r**5*__cos__(5*u)
	Z26 =  Z[26] * r**5*__sin__(5*u)
	Z27 =  Z[27] * (6*r**2-5)*r**4*__cos__(4*u)
	Z28 =  Z[28] * (6*r**2-5)*r**4*__sin__(4*u)
	Z29 =  Z[29] * (21*r**4-30*r**2+10)*r**3*__cos__(3*u)
	Z30 =  Z[30] * (21*r**4-30*r**2+10)*r**3*__sin__(3*u)
	Z31 =  Z[31] * (56*r**6-105*r**4+60*r**2-10)*r**2*__cos__(2*u)
	Z32 =  Z[32] * (56*r**6-105*r**4+60*r**2-10)*r**2*__sin__(2*u)
	Z33 =  Z[33] * (126*r**8-280*r**6+210*r**4-60*r**2+5)*r*__cos__(u)
	Z34 =  Z[34] * (126*r**8-280*r**6+210*r**4-60*r**2+5)*r*__sin__(u)
	Z35 =  Z[35] * (252*r**10-630*r**8+560*r**6-210*r**4+30*r**2-1)

	Z = Z0 + Z1 + Z2 +  Z3+  Z4+  Z5+  Z6+  Z7+  Z8+  Z9+ \
		Z10+ Z11+ Z12+ Z13+ Z14+ Z15+ Z16+ Z17+ Z18+ Z19+ \
		Z20+ Z21+ Z22+ Z23+ Z24+ Z25+ Z26+ Z27+ Z28+ Z29+ \
		Z30+ Z31+ Z32+ Z33+ Z34+ Z35
	return Z

def __zernikecartesian__(coefficient,x,y):
	Z = coefficient
	S = x**2 + y**2
	Z0  =  Z[0]  * 1
	Z1  =  Z[1]  * x
	Z2  =  Z[2]  * y
	Z3  =  Z[3]  * (-1+2*S)
	Z4  =  Z[4]  * S
	Z5  =  Z[5]  * (2*x*y)
	Z6  =  Z[6]  * (-2*x+3*x*S)
	Z7  =  Z[7]  * (1-2*y-6*S+3*y*S+6*S**2)
	Z8  =  Z[8]  * (1-6*S+6*S**2)
	Z9  =  Z[9]  * (x**3-3*x*y)
	Z10 =  Z[10] * (3*x**2*y-y**3)
	Z11 =  Z[11] * (-3*x**2+3*y**2+4*x**2*S-4*y**2*S)
	Z12 =  Z[12] * (-6*x*y+8*x*y*(x**2+y**2))
	Z13 =  Z[13] * (3*x-12*x*S+10*x*S**2)
	Z14 =  Z[14] * (3*y-12*y*S+10*y*S**2)
	Z15 =  Z[15] * (-1+12*S-30*S**2+20*S**3)
	Z16 =  Z[16] * (x**4-6*x**2*y**2+y**4)
	Z17 =  Z[17] * (4*x**3*y-4*x*y**3)
	Z18 =  Z[18] * (-4*x**3+12*x*y**2+5*x**3*S-15*x*y**2*S)
	Z19 =  Z[19] * (-12*x**2*y+4*y**3+15*x**2*y*S-5*y**3*S)
	Z20 =  Z[20] * (6*x**2-6*y**2-20*x**2*S+20*y**2*S+\
					15*x**2*S**2-15*y**2*S**2)
	Z21 =  Z[21] * (12*x*y-40*x*y*S+30*x*y*S*2)
	Z22 =  Z[22] * (-4*x+30*x*S-60*x*S**2+35*x*S**3)
	Z23 =  Z[23] * (-4*y+30*y*S-60*y*S**2+35*y*S**3)
	Z24 =  Z[24] * (1-20*S+90*S**2-140*S**3+70*S**4)
	Z25 =  Z[25] * (x**5-10*x**3*y**2+5*x*y**4)
	Z26 =  Z[26] * (5*x**4*y-10*x**2*y**3+y**5)
	Z27 =  Z[27] * (-5*x**4+30*x**2*y**2-5*y**4+6*x**4*S-\
					36*x**2*y**2*S+6*y**4*S)
	Z28 =  Z[28] * (-20*x**3*y+20*x*y**3+24*x**3*y*S-24*x*y**3*S)
	Z29 =  Z[29] * (10*x**3-30*x*y**2-30*x**3*S+90*x*y**2*S+\
					21*x**3*S**2-63*x*y**2*S**2)
	Z30 =  Z[30] * (30*x**2*y-10*y**3-90*x**2*y*S+30*y**3*S+\
					63*x**2*y*S**2-21*y**3*S**2)
	Z31 =  Z[31] * (-10*x**2+10*y**2+60*x**2*S-60*y**2*S-\
					105*x**2*S**2+105*y**2*S**2+\
					56*x**2*S**3-56*y**2*S**3)
	Z32 =  Z[32] * (-20*x*y+120*x*y*S-210*x*y*S**2+112*x*y*S**3)
	Z33 =  Z[33] * (5*x-60*x*S+210*x*S**2-280*x*S**3+126*x*S**4)
	Z34 =  Z[34] * (5*y-60*y*S+210*y*S**2-280*y*S**3+126*y*S**4)
	Z35 =  Z[35] * (-1+30*S-210*S**2+560*S**3-630*S**4+252*S**5)
	Z = 	Z0 + Z1 + Z2 +  Z3+  Z4+  Z5+  Z6+  Z7+  Z8+  Z9+ \
			Z10+ Z11+ Z12+ Z13+ Z14+ Z15+ Z16+ Z17+ Z18+ Z19+ \
			Z20+ Z21+ Z22+ Z23+ Z24+ Z25+ Z26+ Z27+ Z28+ Z29+ \
			Z30+ Z31+ Z32+ Z33+ Z34+ Z35
	return Z
