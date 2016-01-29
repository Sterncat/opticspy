from __future__ import division as __division__
import numpy as __np__
from numpy import cos as __cos__
from numpy import sin as __sin__
from numpy import sqrt as __sqrt__
from numpy import arctan2 as __arctan2__
import matplotlib.pyplot as __plt__
from mplot3d import Axes3D as __Axes3D__
from matplotlib import cm as __cm__
from matplotlib.ticker import LinearLocator as __LinearLocator__
from matplotlib.ticker import FormatStrFormatter as __FormatStrFormatter__
from numpy.fft import fftshift as __fftshift__
from numpy.fft import ifftshift as __ifftshift__
from numpy.fft import fft2 as __fft2__
from numpy.fft import ifft2 as __ifft2__
import tools as __tools__


class Coefficient(object):
	"""
	Return a set of Orthonormal Rectangular Polynomials For Rectangle aperture

	Reference: Mahajan, Virendra N., and Guang-ming Dai. 
	"Orthonormal polynomials in wavefront analysis: analytical 
	solution." JOSA A 24.9 (2007): 2994-3016.
	"""
	__coefficients__ = []
	__a__ = 1/__sqrt__(2)
	__zernikelist__ = []

	def __init__(self, a = __a__,\
			R1=0, R2=0, R3=0, R4=0, R5=0, R6=0, R7=0, R8=0, \
			R9=0, R10=0, R11=0, R12=0, R13=0, R14=0, R15=0):
		if type(R1) == list:
			self.__coefficients__ = R1 + [0]*(15-len(R1))
			self.__a__ = a
		else:
			self.__coefficients__ = [R1, R2, R3, R4, R5, R6, R7, 
					R8, R9, R10, R11, R12, R13, R14, R15]
			self.__a__ = a
	def outputcoefficient(self):
		return [self.__a__,self.__coefficients__]

	def zernikesurface(self):
		"""
		------------------------------------------------
		zernikesurface(self, label_1 = True):

		Return a 3D Zernike Polynomials surface figure

		label_1: default show label

		------------------------------------------------
		"""
		a = self.__a__
		b = __sqrt__(1-a**2)
		x1 = __np__.linspace(-a, a, 50)
		y1 = __np__.linspace(-b, b, 50)
		[X,Y] = __np__.meshgrid(x1,y1)
		Z = __zernikecartesian__(self.__coefficients__,a,X,Y)
		fig = __plt__.figure(figsize=(12, 8), dpi=80)
		ax = fig.gca(projection='3d')
		surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=__cm__.RdYlGn,
	        linewidth=0, antialiased=False, alpha = 0.6)

		ax.auto_scale_xyz([-1, 1], [-1, 1], [Z.max(), Z.min()])
		# ax.set_xlim(-a, a)
		# ax.set_ylim(-b, b)
		# v = max(abs(Z.max()),abs(Z.min()))
		# ax.set_zlim(-v*5, v*5)
		# cset = ax.contourf(X, Y, Z, zdir='z', offset=-v*5, cmap=__cm__.RdYlGn)

		# ax.zaxis.set_major_locator(__LinearLocator__(10))
		# ax.zaxis.set_major_formatter(__FormatStrFormatter__('%.02f'))
		fig.colorbar(surf, shrink=1, aspect=30)

		# p2v = round(__tools__.peak2valley(Z),5)
		# rms1 = round(__tools__.rms(Z),5)
		__plt__.show()
	def zernikemap(self):
		a = self.__a__
		b = __sqrt__(1-a**2)
		x1 = __np__.linspace(-a, a, 100)
		y1 = __np__.linspace(-b, b, 100)
		[X,Y] = __np__.meshgrid(x1,y1)
		Z = __zernikecartesian__(self.__coefficients__,a,X,Y)
		fig = __plt__.figure(figsize=(12, 8), dpi=80)
		ax = fig.gca()
		im = __plt__.pcolormesh(X, Y, Z, cmap=__cm__.RdYlGn)
		__plt__.colorbar()
		ax.set_aspect('equal', 'datalim')
		__plt__.show()

		return 0

	def __psfcaculator__(self,lambda_1=632*10**(-9),z=0.1):
		"""
		height: Exit pupil height
		width: Exit pupil width
		z: Distance from exit pupil to image plane
		"""
		a = self.__a__
		b = __sqrt__(1-a**2)
		l1 = 100;
		x1 = __np__.linspace(-a, a, l1)
		y1 = __np__.linspace(-b, b, l1)
		[X,Y] = __np__.meshgrid(x1,y1)
		Z = __zernikecartesian__(self.__coefficients__,a,X,Y)
		d = 400 # background
		A = __np__.zeros([d,d])
		A[d/2-l1/2+1:d/2+l1/2+1,d/2-l1/2+1:d/2+l1/2+1] = Z
		# fig = __plt__.figure()
		# __plt__.imshow(A)
		# __plt__.colorbar()
		# __plt__.show()
		abbe = __np__.exp(-1j*2*__np__.pi*A)
		for i in range(len(abbe)):
			for j in range(len(abbe)):
				if abbe[i][j]==1:
					abbe[i][j]=0
		PSF = __fftshift__(__fft2__(__fftshift__(abbe)))**2
		PSF = PSF/PSF.max()
		return PSF

	def psf(self,lambda_1=632*10**(-9),z=0.1):
		"""
		------------------------------------------------
		psf()

		Return the point spread function of a wavefront described by
		Orthonormal Rectangular Polynomials
		------------------------------------------------
		Input: 

		r: exit pupil radius(mm)

		lambda_1: wavelength(m)

		z: exit pupil to image plane distance(m)

		"""
		PSF = self.__psfcaculator__(lambda_1=lambda_1,z=z)
		fig = __plt__.figure(figsize=(9, 6), dpi=80)
		__plt__.imshow(abs(PSF),cmap=__cm__.RdYlGn)
		__plt__.colorbar()
		__plt__.show()
		return 0

	def mtf(self,lambda_1=632*10**(-9),z=0.1,matrix = False):
		"""
		Modulate Transfer function
		"""
		PSF = self.__psfcaculator__(lambda_1=lambda_1,z=z)
		MTF = __fftshift__(__fft2__(PSF))
		MTF = MTF/MTF.max()
		fig = __plt__.figure(figsize=(9, 6), dpi=80)
		__plt__.imshow(abs(MTF),cmap=__cm__.bwr)
		__plt__.colorbar()
		__plt__.show()
		if matrix == True:
			return MTF
		else:
			return 0

	def ptf(self):
		"""
		Phase transfer function
		"""
		PSF = self.__psfcaculator__()
		PTF = __fftshift__(__fft2__(PSF))
		PTF = __np__.angle(PTF)
		l1 = 100
		d = 400
		A = __np__.zeros([d,d])
		A[d/2-l1/2+1:d/2+l1/2+1,d/2-l1/2+1:d/2+l1/2+1] = PTF[d/2-l1/2+1:d/2+l1/2+1,d/2-l1/2+1:d/2+l1/2+1]
		__plt__.imshow(abs(A),cmap=__cm__.rainbow)
		__plt__.colorbar()
		__plt__.show()
		return 0

def __zernikepolar__(coefficient,a,r,u):
	"""
	------------------------------------------------
	__zernikepolar__(coefficient,r,u):

	Return combined aberration

	Orthonormal Rectangle Aperture Polynomials Caculation in polar coordinates

	coefficient: Orthonormal Rectangle Aperture Polynomials Coefficient from input
	r: rho in polar coordinates
	u: theta in polar coordinates
	------------------------------------------------
	"""
	mu = __sqrt__(9-36*a**2+103*a**4-134*a**6+67*a**6+67*a**8)
	v = __sqrt__(49-196*a**2+330*a**4-268*a**6+134*a**8)
	tau = 1/(128*v*a**4*(1-a**2)**2)
	eta = 9-45*a**2+139*a**4-237*a**6+210*a**8-67*a**10

	R = [0]+coefficient
	R1  =  R[1]  * 1                              
	R2  =  R[2]  * __sqrt__(3)/a*r*__cos__(u)
	R3  =  R[3]  * __sqrt__(3/(1-a**2))*r*__sin__(u)
	R4  =  R[4]  * __sqrt__(5)/2/__sqrt__(1-2*a**2+2*a**4)*(3*r**2-1)
	R5  =  R[5]  * 3/2/a/__sqrt__(1-a**2)*r**2*__sin__(2*u)
	R6  =  R[6]  * __sqrt__(5)/2/a**2/(1-a**2)/__sqrt__(1-2*a**2+2*a**4)*\
					(3*(1-2*a**2+2*a**4)*r**2*__cos__(2*u)+3*(1-2*a**2)*r**2-\
					2*a**2*(1-a**2)*(1-2*a**2))
	R7  =  R[7]  * __sqrt__(21)/2/__sqrt__(27-81*a**2+116*a**4-62*a**6)*\
					(15*r**2-9+4*a**2)*r*__sin__(u)
	R8  =  R[8]  * __sqrt__(21)/2/a/__sqrt__(35-70*a**2+62*a**4)*\
					(15*r**2-5-4*a**2)*r*__cos__(u)
	R9  =  R[9]  * (__sqrt__(5)*__sqrt__((27-54*a**2+62*a**4)/(1-a**2))/\
					(8*a**2*(27-81*a**2+116*a**4-62*a**6)))*((27-54*a**2+62*a**4)*\
					r*__sin__(3*u)-3*(4*a**2*(3-13*a**2+10*a**4)-(9-18*a**2-26*a**4))\
					*r*__sin__(u))
	r1  = 35-70*a**2+62*a**4
	R10 =  R[10] * (__sqrt__(5)/(8*a**3*(1-a**2)*__sqrt__(r1)))*((r1)*r**3*__cos__(3*u)-\
					3*(4*a**2*(7-17*a**2+10*a**4)-(r1)*r**2)*r*__cos__(u))
	R11 =  R[11] * 1/8/mu*(315*r**4+30*(1-2*a**2)*r**2*__cos__(2*u)-240*r**2+27+16*a*2-16*a**4)
	R12 =  R[12] * (3*mu/(8*a**2*v*eta))*(315*(1-2*a**2)*(1-2*a**2+2*a**4)*r**4+\
					5*(7*mu**2*r**2-21+72*a**2-225*a**4+306*a**6-152*a**8)*r**2*__cos__(2*u)-\
					15*(1-2*a**2)*(7+4*a**2-71*a**4+134*a**6-67*a**8)*r**2+\
						a**2*(1-a**2)*(1-2*a**2)*(70-233*a**2+233*a**4))
	R13 =  R[13] * __sqrt__(21)/(4*a*__sqrt__(1-3*a**2+4*a**4-2*a**6))*(5*r**2-3)*r**2*__sin__(2*u)
	R14 =  R[14] * 6*tau*(5*v**2*r**4*__cos__(4*u)-20*(1-2*a**2)*(6*a**2*(7-16*a**2+18*a**4-9*a**6)-\
					49*(1-2*a**2+2*a**4)*r**2)*r**2*__cos__(u)+8*a**4*(1-a**2)**2*(21-62*a**2+62*a**4)-\
					120*a**2*(7-30*a**2+46*a**4-23*a**6)*r**2+\
					15*(49-196*a**2+282*a**4-172*a**6+86*a**8)*r**4)
	R15 =  R[15] * (__sqrt__(21)/(8*a**3*__sqrt__((1-a**2)**3))/__sqrt__(1-2*a**2+2*a**4))*\
					(-(1-2*a**2)*(6*a**2-6*a**4-5*r**2)*r**2*__sin__(2*u)+\
					(5/2)*(1-2*a**2+2**a**4)*r**4*__sin__(4*u))
	RW = 	R1 + R2 +  R3+  R4+  R5+  R6+  R7+  R8+  R9+ \
			R10+ R11+ R12+ R13+ R14+ R15
	return RW

def __zernikecartesian__(coefficient,a,x,y):
	"""
	------------------------------------------------
	__zernikecartesian__(coefficient,a,x,y):

	Return combined aberration

	Orthonormal Rectangle Aperture Polynomials Caculation for 
	Rectangle aperture in Cartesian coordinates

	coefficient: Zernike Polynomials Coefficient from input
	a: 1/2 aperture width in a circle(See reference)
	x: x in Cartesian coordinates
	y: y in Cartesian coordinates
	------------------------------------------------
	"""
	mu = __sqrt__(9-36*a**2+103*a**4-134*a**6+67*a**6+67*a**8)
	v = __sqrt__(49-196*a**2+330*a**4-268*a**6+134*a**8)
	tau = 1/(128*v*a**4*(1-a**2)**2)
	eta = 9-45*a**2+139*a**4-237*a**6+210*a**8-67*a**10
	r = x**2+y**2

	R = [0]+coefficient
	R1  =  R[1]  * 1                              
	R2  =  R[2]  * __sqrt__(3)/a*x
	R3  =  R[3]  * __sqrt__(3/(1-a**2))*y
	R4  =  R[4]  * __sqrt__(5)/2/__sqrt__(1-2*a**2+2*a**4)*(3*r**2-1)
	R5  =  R[5]  * 3/a/__sqrt__(1-a**2)*x*y
	R6  =  R[6]  * __sqrt__(5)/4/a**2/(1-a**2)/__sqrt__(1-2*a**2+2*a**4)*\
					(3*(1-a**2)**2*x**2-3*a**4*y**2-a*82*(1-3*a**2+2*a**4))
	R7  =  R[7]  * __sqrt__(21)/2/__sqrt__(27-81*a**2+116*a**4-62*a**6)*\
					(15*r**2-9+4*a**2)*y
	R8  =  R[8]  * __sqrt__(21)/2/a/__sqrt__(35-70*a**2+62*a**4)*\
					(15*r**2-5-4*a**2)*x
	R9  =  R[9]  * (__sqrt__(5)*__sqrt__((27-54*a**2+62*a**4)/(1-a**2))/\
					(2*a**2*(27-81*a**2+116*a**4-62*a**6)))*(27*(1-a**2)**2*x**2-\
					35*a**4*y**2-a**2*(9-39*a**2+30*a**4))*y
	r1  = 35-70*a**2+62*a**4
	R10 =  R[10] * (__sqrt__(5)/(2*a**3*(1-a**2)*__sqrt__(r1)))*(35*(1-a**2)**2*x**2-\
					27*a**4*y**2-a**2*(21-51*a**2+30*a**4))*x
	R11 =  R[11] * 1/8/mu*(315*r**4+30*(7+2*a**2)*x**2-30*(9-2*a**2)*y**2+27+16*a**2-16*a**4)

	R12 =  R[12] * (3*mu/(8*a**2*v*eta))*(35*(1-a**2)**2*(18-36*a**2+67*a**4)*x**4+\
					630*(1-2*a**2)*(1-2*a**2+2*a**4)*x**2*y**2-35*a**4*(49-98*a**2+67*a**4)*y**4-\
					30*(1-a**2)*(7-10*a**2-12*a**4+75*a**6-67*a**8)*x**2-\
					30*a**2*(7-77*a**2+189*a**4-193*a**6+67*a**8)*y**2+\
					a**2*(1-a**2)*(1-2*a**2)*(70-233*a**2+233*a**4))
	R13 =  R[13] * __sqrt__(21)/(2*a*__sqrt__(1-3*a**2+4*a**4-2*a**6))*(5*r**2-3)*x*y
	R14 =  R[14] * 16*tau*(735*(1-a**2)**4*x**4-540*a**4*(1-a**2)**2*x**2*y**2+735*a**8*y**4-\
					90*a**2*(1-a**2)**3*(7-9*a**2)*x**2+90*a**6*(1-a**2)*(2-9*a**2)*y**2+\
					+3*a**4*(1-a**2)**2*(21-62*a**2+62*a**4))
	R15 =  R[15] * __sqrt__(21)/(2*a**3*(1-a**2)*__sqrt__(1-3*a**2+4*a**4-2*a**6))*\
					(5*(1-a**2)**2*x**2-5*a**4*y**2-a**2*(3-9*a**2+6*a**4))*x*y

	RW = 	R1 + R2 +  R3+  R4+  R5+  R6+  R7+  R8+  R9+ \
			R10+ R11+ R12+ R13+ R14+ R15
	return RW



