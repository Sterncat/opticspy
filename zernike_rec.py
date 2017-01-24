from __future__ import division as __division__
import numpy as __np__
from numpy import cos as __cos__
from numpy import sin as __sin__
from numpy import sqrt as __sqrt__
from numpy import arctan2 as __arctan2__
import matplotlib.pyplot as __plt__
from matplotlib import cm as __cm__
from matplotlib.ticker import LinearLocator as __LinearLocator__
from matplotlib.ticker import FormatStrFormatter as __FormatStrFormatter__
from numpy.fft import fftshift as __fftshift__
from numpy.fft import ifftshift as __ifftshift__
from numpy.fft import fft2 as __fft2__
from numpy.fft import ifft2 as __ifft2__

from .zernike_rec_coeffs import __zernikepolar__, __zernikecartesian__
from . import tools as __tools__

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

