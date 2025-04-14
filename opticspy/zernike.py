# coding=utf-8
from __future__ import division as __division__
import numpy as __np__
from numpy import cos as __cos__
from numpy import sin as __sin__
from numpy import sqrt as __sqrt__
from numpy import arctan2 as __arctan2__
import math
import matplotlib.pyplot as __plt__
from matplotlib import cm as __cm__
from matplotlib.ticker import LinearLocator as __LinearLocator__
from matplotlib.ticker import FormatStrFormatter as __FormatStrFormatter__
from numpy.fft import fftshift as __fftshift__
from numpy.fft import ifftshift as __ifftshift__
from numpy.fft import fft2 as __fft2__
from numpy.linalg import inv
from numpy.fft import ifft2 as __ifft2__
import operator as op
from mpl_toolkits.mplot3d import Axes3D

from . import interferometer_zenike as __interferometer__
from . import seidel2 as __seidel2__
from . import tools as __tools__
from . import hartmann as __hartmann__

class Coefficient(object):
	"""
	Return a set of Zernike Polynomials Coefficient
	"""
	__coefficients__ = []
	__zernikelist__ = [ "Z00 Piston or Bias",
						"Z11 x Tilt",
						"Z11 y Tilt",
						"Z20 Defocus",
						"Z22 Primary Astigmatism at 45",
						"Z22 Primary Astigmatism at 0",
						"Z31 Primary y Coma",
						"Z31 Primary x Coma",
						"Z33 y Trefoil",
						"Z33 x Trefoil",
						"Z40 Primary Spherical",
						"Z42 Secondary Astigmatism at 0",
						"Z42 Secondary Astigmatism at 45",
						"Z44 x Tetrafoil",
						"Z44 y Tetrafoil",
						"Z51 Secondary x Coma",
						"Z51 Secondary y Coma",
						"Z53 Secondary x Trefoil",
						"Z53 Secondary y Trefoil",
						"Z55 x Pentafoil",
						"Z55 y Pentafoil",
						"Z60 Secondary Spherical",
						"Z62 Tertiary Astigmatism at 45",
						"Z62 Tertiary Astigmatism at 0",
						"Z64 Secondary x Trefoil",
						"Z64 Secondary y Trefoil",
						"Z66 Hexafoil Y",
						"Z66 Hexafoil X",
						"Z71 Tertiary y Coma",
						"Z71 Tertiary x Coma",
						"Z73 Tertiary y Trefoil",
						"Z73 Tertiary x Trefoil",
						"Z75 Secondary Pentafoil Y",
						"Z75 Secondary Pentafoil X",
						"Z77 Heptafoil Y",
						"Z77 Heptafoil X",
						"Z80 Tertiary Spherical"]

	def __init__(self,
			Z1=0, Z2=0, Z3=0, Z4=0, Z5=0, Z6=0, Z7=0, \
			Z8=0, Z9=0, Z10=0, Z11=0, Z12=0, Z13=0, Z14=0, \
			Z15=0, Z16=0, Z17=0, Z18=0, Z19=0, Z20=0, Z21=0, \
			Z22=0, Z23=0, Z24=0, Z25=0, Z26=0, Z27=0, Z28=0, \
			Z29=0, Z30=0, Z31=0, Z32=0, Z33=0, Z34=0, Z35=0, Z36=0, Z37=0):
		if type(Z1) == list:
			self.__coefficients__ = Z1 + [0]*(37-len(Z1))
		else:
			self.__coefficients__ = [Z1, Z2, Z3, Z4, Z5, Z6, Z7,
					Z8, Z9, Z10, Z11, Z12, Z13, Z14, Z15, Z16, Z17,
					Z18, Z19, Z20, Z21, Z22, Z23, Z24, Z25, Z26,
					Z27, Z28, Z29, Z30, Z31, Z32, Z33, Z34, Z35, Z36, Z37]
	def outputcoefficient(self):
		return self.__coefficients__
	def listcoefficient(self):
		"""
		------------------------------------------------
		listcoefficient():

		List the coefficient in Coefficient

		------------------------------------------------
		"""
		m = 0
		label1 = ""
		label2 = ""
		for i in self.__coefficients__:
			if i != 0:
				print('Z'+str(m+1)+' = ',i,self.__zernikelist__[m])
				label1 = label1 + 'Z'+str(m+1)+' = '+str(i)+"\n"
				label2 = label2 + 'Z'+str(m+1)+' = '+str(i)+"  "
			m = m + 1
		return [label1,label2]

	def zernikelist(self):
		"""
		------------------------------------------------
		zernikelist():

		List all Zernike Polynomials

		------------------------------------------------
		"""
		m = 1
		for i in self.__zernikelist__:
			print("Z"+str(m)+":"+i)
			m = m + 1

	def zernikesurface(self, label = True, zlim=[], matrix = False):
		"""
		------------------------------------------------
		zernikesurface(self, label_1 = True):

		Return a 3D Zernike Polynomials surface figure

		label_1: default show label

		------------------------------------------------
		"""
		theta = __np__.linspace(0, 2*__np__.pi, 100)
		rho = __np__.linspace(0, 1, 100)
		[u,r] = __np__.meshgrid(theta,rho)
		X = r*__cos__(u)
		Y = r*__sin__(u)
		Z = __interferometer__.__zernikepolar__(self.__coefficients__,r,u)
		fig = __plt__.figure(figsize=(12, 8), dpi=80)
		ax = Axes3D(fig)
		surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=__cm__.RdYlGn,
	        linewidth=0, antialiased=False, alpha = 0.6)

		if zlim == []:
			v = max(abs(Z.max()),abs(Z.min()))
			ax.set_zlim(-v*5, v*5)
			cset = ax.contourf(X, Y, Z, zdir='z', offset=-v*5, cmap=__cm__.RdYlGn)
		else:
			ax.set_zlim(zlim[0], zlim[1])
			cset = ax.contourf(X, Y, Z, zdir='z', offset=zlim[0], cmap=__cm__.RdYlGn)

		ax.zaxis.set_major_locator(__LinearLocator__(10))
		ax.zaxis.set_major_formatter(__FormatStrFormatter__('%.02f'))
		fig.colorbar(surf, shrink=1, aspect=30)


		p2v = round(__tools__.peak2valley(Z),5)
		rms1 = round(__tools__.rms(Z),5)

		label_1 = self.listcoefficient()[0]+"P-V: "+str(p2v)+"\n"+"RMS: "+str(rms1)
		if label == True:
			__plt__.title('Zernike Polynomials Surface',fontsize=18)
			ax.text2D(0.02, 0.1, label_1, transform=ax.transAxes,fontsize=14)
		else:
			pass
		__plt__.show()

		if matrix == True:
			return Z
		else:
			pass
	def zernikemap(self, label = True):
		"""
		------------------------------------------------
		zernikemap(self, label_1 = True):

		Return a 2D Zernike Polynomials map figure

		label: default show label

		------------------------------------------------
		"""


		theta = __np__.linspace(0, 2*__np__.pi, 400)
		rho = __np__.linspace(0, 1, 400)
		[u,r] = __np__.meshgrid(theta,rho)
		X = r*__cos__(u)
		Y = r*__sin__(u)
		Z = __interferometer__.__zernikepolar__(self.__coefficients__,r,u)
		fig = __plt__.figure(figsize=(12, 8), dpi=80)
		ax = fig.gca()
		im = __plt__.pcolormesh(X, Y, Z, cmap=__cm__.RdYlGn)

		if label == True:
			__plt__.title('Zernike Polynomials Surface Heat Map',fontsize=18)
			ax.set_xlabel(self.listcoefficient()[1],fontsize=18)
		__plt__.colorbar()
		ax.set_aspect('equal', 'datalim')
		__plt__.show()

	def zernikeline(self):
		"""
		------------------------------------------------
		zernikeline()

		Return a 1D cutoff through x and y axis of a 3D
		Zernike Polynomials surface figure
		------------------------------------------------
		"""

		X = __np__.linspace(-1, 1, 100)
		Y = __np__.linspace(-1, 1, 100)
		ZX = __interferometer__.__zernikecartesian__(self.__coefficients__,X,0)
		ZY = __interferometer__.__zernikecartesian__(self.__coefficients__,0,Y)
		fig = __plt__.figure()
		ax = fig.gca()
		__plt__.plot(X,ZX)
		__plt__.plot(Y,ZY)
		__plt__.grid()
		__plt__.show()

	def zernikematrix(self,l = 100):
		x = __np__.linspace(-1, 1, l)
		[X,Y] = __np__.meshgrid(x,x)
		Z = __interferometer__.__zernikecartesian__(self.__coefficients__,X,Y)
		return Z

	def __psfcaculator__(self,r=1,lambda_1=632*10**(-9),z=0.1):
		"""
		pupil: Exit pupil diameter
		z: Distance from exit pupil to image plane
		r: pupil radius, in unit of lambda
		"""
		pupil = l1 = 200 # exit pupil sample points
		x = __np__.linspace(-r, r, l1)
		[X,Y] = __np__.meshgrid(x,x)
		Z = __interferometer__.__zernikecartesian__(self.__coefficients__,X,Y)
		for i in range(len(Z)):
			for j in range(len(Z)):
				if x[i]**2+x[j]**2>r**2:
					Z[i][j] = 0
		d = 400 # background
		A = __np__.zeros([d,d])
		A[d//2-l1//2+1:d//2+l1//2+1,d//2-l1//2+1:d//2+l1//2+1] = Z
		axis_1 = d//pupil*r
		fig = __plt__.figure()
		# ax = fig.gca()
		# __plt__.imshow(A,extent=[-axis_1,axis_1,-axis_1,axis_1],cmap=__cm__.RdYlGn)
		# ax.set_xlabel('mm',fontsize=14)
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

	def psf(self,r=1,lambda_1=632*10**(-9),z=0.1):
		"""
		------------------------------------------------
		psf()

		Return the point spread function of a wavefront described by
		Zernike Polynomials
		------------------------------------------------
		Input:

		r: exit pupil radius(mm)

		lambda_1: wavelength(m)

		z: exit pupil to image plane distance(m)

		"""
		print(r,lambda_1,z)
		PSF = self.__psfcaculator__(r=r,lambda_1=lambda_1,z=z)
		fig = __plt__.figure(figsize=(9, 6), dpi=80)
		__plt__.imshow(abs(PSF),cmap=__cm__.RdYlGn)
		__plt__.colorbar()
		__plt__.show()
		return 0

	def otf(self,r=1,lambda_1=632*10**(-9),z=0.1):
		PSF = self.__psfcaculator__(r=r,lambda_1=lambda_1,z=z)
		OTF = __fftshift__(__fft2__(PSF))
		return 0


	def mtf(self,r=1,lambda_1=632*10**(-9),z=0.1,matrix = False):
		"""
		Modulate Transfer function
		"""
		PSF = self.__psfcaculator__(r=r,lambda_1=lambda_1,z=z)
		MTF = __fftshift__(__fft2__(PSF))
		MTF = MTF/MTF.max()
		f0 = r/1000/lambda_1/z/10000   # cutoff frequency?
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
		b = 400
		R = (200)**2
		for i in range(b):
			for j in range(b):
				if (i-b/2)**2+(j-b/2)**2>R:
					PTF[i][j] = 0
		__plt__.imshow(abs(PTF),cmap=__cm__.rainbow)
		__plt__.colorbar()
		__plt__.show()
		return 0



	def twyman_green(self,lambda_1=632,PR=1):
		__interferometer__.twyman_green(self,lambda_1=lambda_1,PR=PR)


	def hartmann(self,r=1,R=1):
		M = __hartmann__.hartmann(self,r=r,R=R)
		return M

	def zernike2seidel(self):
		'''
		Ap is the piston aberration,coefficients Ai represent the
		peak value of the corresponding Seidel aberration term,
		'''
		a = [0]+self.__coefficients__
		#Piston
		Ap = a[1]-__sqrt__(3)*a[4]+__sqrt__(5)*a[11]
		#tilt
		At = 2*__sqrt__((a[2]-__sqrt__(8)*a[8])**2+(a[3]-__sqrt__(8)*a[7])**2)
		Bt = __arctan2__(a[3]-__sqrt__(8)*a[7],a[2]-__sqrt__(8)*a[8])*180/__np__.pi
		#Astigmatism
		Aa = 2*__sqrt__(6*(a[5]**2+a[6]**2))
		Ba = 0.5*__arctan2__(a[5],a[6])*180/__np__.pi
		#defocus
		Ad = 2*(__sqrt__(3)*a[4]-3*__sqrt__(5)*a[11]-Aa)
		#Coma
		Ac = 6*__sqrt__(2*(a[7]**2+a[8]**2))
		Bc = __arctan2__(a[7],a[8])*180/__np__.pi
		#Spherical
		As = 6*__sqrt__(5)*a[11]
		A = [Ap,At,Bt,Ad,Aa,Ba,Ac,Bc,As]


		seidellist=["Piston",
				 	"Tilt",
				 	"Defocus",
				 	"Astigmatism",
				 	"Coma",
				 	"Spherical"]
		Atable = [[Ap,0.0],[At,Bt],[Ad,0.0],[Aa,Ba],[Ac,Bc],[As,0.0]]
		print("                 Magnitude  Angle (Degrees)")
		print("-------------------------------------------")
		for i in range(len(seidellist)):
			print("| {0:>13s} |  {1:>8s}  | {2:>8s}   |".\
			format(seidellist[i],str(round(Atable[i][0],3)),str(round(Atable[i][1],3))))
		print("-------------------------------------------")
		SeidelCoefficient = __seidel2__.Coefficient(Atable)
		return SeidelCoefficient
	def removepiston(self):
		"""
		Remove piston, it is just same value for whole aberration map
		"""
		Z = self.__coefficients__
		Z[0] = 0
		return Z
	def removetilt(self):
		"""
		Remove tilt, it is mainly caused by system tilt, not aberration
		on surface
		"""
		tilt = [2,3]
		Z = self.__coefficients__
		for i in tilt:
			Z[i-1] = 0
		return Z
	def removecoma(self):
		"""
		Remove coma, most of coma is caused by misalinement
		??? Is high order coma also caused by misalinement ???
		"""
		coma = [7,8,16,17,29,30]
		Z = self.__coefficients__
		for i in coma:
			Z[i-1] = 0
		return Z




def fitting(Z,n,remain3D=False,remain2D=False,barchart=False,interferogram=False,removepiston=True):
	"""
	------------------------------------------------
	fitting(Z,n)

	Fitting an aberration to several orthonormal Zernike
	polynomials.

	Return: n-th Zernike coefficients for a fitting surface aberration
			Zernike coefficients barchart
			Remaining aberration
			Fiting surface plot
	Input:
	Z: A surface or aberration matrix measure from inteferometer
	   or something else.

	n: How many order of Zernike Polynomials you want to fit

	reamin(default==Flase): show the surface after remove fitting
	aberrations.

	removepiston: if remove piston, default = True
	------------------------------------------------
	"""


	fitlist = []
	l = len(Z)
	x2 = __np__.linspace(-1, 1, l)
	y2 = __np__.linspace(-1, 1, l)
	[X2,Y2] = __np__.meshgrid(x2,y2)
	r = __np__.sqrt(X2**2 + Y2**2)
	u = __np__.arctan2(Y2, X2)
	for i in range(n):
		C = [0]*i+[1]+[0]*(37-i-1)
		ZF = __interferometer__.__zernikepolar__(C,r,u)
		for i in range(l):
			for j in range(l):
				if x2[i]**2+y2[j]**2>1:
					ZF[i][j]=0
		a = sum(sum(Z*ZF))*2*2/l/l/__np__.pi
		fitlist.append(round(a,3))


	l1 = len(fitlist)
	fitlist = fitlist+[0]*(37-l1)
	Z_new = Z - __interferometer__.__zernikepolar__(fitlist,r,u)
	for i in range(l):
		for j in range(l):
			if x2[i]**2+y2[j]**2>1:
				Z_new[i][j]=0

	#plot bar chart of zernike
	if barchart == True:
		fitlist1 = fitlist[0:n]
		index = __np__.arange(n)
		fig = __plt__.figure(figsize=(9, 6), dpi=80)
		xticklist = []
		width = 0.6
		for i in index:
			xticklist.append('Z'+str(i+1))
		barfigure = __plt__.bar(index, fitlist1, width,color = '#2E9AFE',edgecolor = '#2E9AFE')
		__plt__.xticks( index+width//2, xticklist )
		__plt__.xlabel('Zernike Polynomials',fontsize=18)
		__plt__.ylabel('Coefficient',fontsize=18)
		__plt__.title('Fitting Zernike Polynomials Coefficient',fontsize=18)

		__plt__.show()
	else:
		pass


	if remain3D == True:

		fig = __plt__.figure(figsize=(12, 8), dpi=80)
		ax = Axes3D(fig)
		surf = ax.plot_surface(X2, Y2, Z_new, rstride=1, cstride=1, cmap=__cm__.RdYlGn,
	        linewidth=0, antialiased=False, alpha = 0.6)
		v = max(abs(Z.max()),abs(Z.min()))
		ax.set_zlim(-v, v)
		ax.zaxis.set_major_locator(__LinearLocator__(10))
		ax.zaxis.set_major_formatter(__FormatStrFormatter__('%.02f'))
		cset = ax.contourf(X2, Y2, Z_new, zdir='z', offset=-v, cmap=__cm__.RdYlGn)
		fig.colorbar(surf, shrink=1, aspect=30)
		__plt__.title('Remaining Aberration',fontsize=18)
		p2v = round(__tools__.peak2valley(Z_new),5)
		rms1 = round(__tools__.rms(Z_new),5)
		label_new = "P-V: "+str(p2v)+"\n"+"RMS: "+str(rms1)
		ax.text2D(0.02, 0.1,label_new, transform=ax.transAxes)
		__plt__.show()
	else:
		pass

	if remain2D == True:
		fig = __plt__.figure(figsize=(9, 6), dpi=80)
		ax = fig.gca()
		im = __plt__.pcolormesh(X2, Y2, Z_new, cmap=__cm__.RdYlGn)
		__plt__.colorbar()
		__plt__.title('Remaining Aberration',fontsize=18)
		ax.set_aspect('equal', 'datalim')
		__plt__.show()
	else:
		pass

	if interferogram == True:
		zernike_coefficient = Coefficient(fitlist)
		__interferometer__.twyman_green(zernike_coefficient)
	else:
		pass
	if removepiston == True:
		fitlist[0] = 0
	else:
		pass
	C = Coefficient(fitlist)  #output zernike Coefficient class
	__tools__.zernikeprint(fitlist)
	return fitlist,C

def transform(zernikes, tx, ty, thetaR, scaling=1.0):
	"""
		------------------------------------------------
		transform(zernikes, scaling, tx, ty, thetaR):

		scale (concentric), translation of center, and rotate your zernike polynomial without re-sampling.
		scaling and translation is performed first and then rotation.

		zernikes: Zernike coefficients in standard ANSI order - a list of floats with arbitrary length. The first index
		 is the pivot, then x-tilt, y-tilt, first astigmatism,...
		tx: Horizontal translation
		ty: Vertical translation
		thetaR: rotation in _degrees_
		scaling: concentring scaling factor.

		return: Zernike coefficients in standard ANSI order - same list length as the input.

		Based on: Linda Lundström and Peter Unsbo, "Transformation of Zernike coefficients: scaled, translated, and
		rotated wavefronts with circular and elliptical pupils," J. Opt. Soc. Am. A 24, 569-577 (2007)
		Translated into Python by: Oskar Truffer
		------------------------------------------------
		"""
	C1 = __np__.array(zernikes)
	etaS = scaling
	etaT = 2 * __np__.sqrt(__np__.square(tx) + __np__.square(ty)) / 1.0
	thetaT = __np__.arctan2(ty, tx)
	thetaR = thetaR * __np__.pi / 180
	jnm = len(C1) - 1
	nmax = int(__np__.ceil((-3 + __np__.sqrt(9 + 8 * jnm)) / 2))
	jmax = int(nmax * (nmax + 3) / 2)
	S = __np__.zeros((jmax + 1, 1))
	S[0:len(C1)] = C1.reshape((len(C1), 1))
	C1 = S
	jmaxTuple = (jmax + 1, jmax + 1)
	P = __np__.zeros(jmaxTuple)
	N = __np__.zeros(jmaxTuple)
	R = __np__.zeros(jmaxTuple)
	CC1 = __np__.zeros((jmax + 1, 1), dtype=__np__.complex)
	counter = 0
	for m in xrange(-nmax, nmax + 1):
		for n in xrange(__np__.abs(m), nmax + 1, 2):
			jnm = (m + n * (n + 2)) / 2
			P[counter, jnm] = 1
			N[counter, counter] = __np__.sqrt(n + 1)
			for s in xrange(0, int((n - abs(m)) / 2 + 1)):
				R[counter - s, counter] = math.pow((-1), s) * math.factorial(n - s) / (
					math.factorial(s) * math.factorial((n + m) / 2 - s) * math.factorial((n - m) / 2 - s))
			if m < 0:
				CC1[jnm] = complex(C1[(-m + n * (n + 2)) / 2], C1[jnm]) / __np__.sqrt(2)
			elif m == 0:
				CC1[jnm] = complex(C1[jnm], 0)
			else:
				CC1[jnm] = complex(C1[jnm], -C1[(-m + n * (n + 2)) / 2]) / math.sqrt(2)
			counter += 1

	ETA = None
	for m in xrange(-nmax, nmax + 1):
		for n in xrange(abs(m), nmax + 1, 2):
			transd = _transformMatrix(n, m, jmax, etaS, etaT, thetaT, thetaR)
			if ETA is None:
				ETA = __np__.matmul(P, transd)
			else:
				ETA = __np__.hstack([ETA, __np__.matmul(P, transd)])

	C = __np__.matmul(__np__.matmul(__np__.matmul(__np__.matmul(__np__.matmul(__np__.matmul(inv(P), inv(N)), inv(R)), ETA), R), N), P)
	CC2 = __np__.matmul(C, CC1)
	C2 = __np__.zeros((jmax + 1, 1))
	for m in xrange(-nmax, nmax + 1):
		for n in xrange(abs(m), nmax + 1, 2):
			jnm = (m + n * (n + 2)) / 2
			if m < 0:
				C2[jnm] = __np__.imag(CC2[jnm] - CC2[(-m + n * (n + 2)) / 2]) / __np__.sqrt(2)
			elif m == 0:
				C2[jnm] = __np__.real(CC2[jnm])
			else:
				C2[jnm] = __np__.real(CC2[jnm] + CC2[(-m + n * (n + 2)) / 2]) / __np__.sqrt(2)

	return C2


def _transformMatrix(n, m, jmax, etaS, etaT, thetaT, thetaR):
	Eta = __np__.zeros((jmax + 1, 1), dtype=__np__.complex)
	for p in xrange(0, int((n + m) / 2 + 1)):
		for q in xrange(0, int((n - m) / 2 + 1)):
			nnew = n - p - q
			mnew = m - p + q
			jnm = (mnew + nnew * (nnew + 2)) / 2
			Eta[int(math.floor(jnm))] += _ncr((n + m) / 2, p) * _ncr((n - m) / 2, q) * __np__.power(etaS,
																										n - p - q) * __np__.power(
				etaT, p + q) * __np__.exp(complex(0, ((p - q) * (thetaT - thetaR) + m * thetaR)))
	return Eta


def _ncr(n, r):
	r = min(r, n - r)
	if r == 0: return 1
	numer = reduce(op.mul, xrange(n, n - r, -1))
	denom = reduce(op.mul, xrange(1, r + 1))
	return numer // denom
