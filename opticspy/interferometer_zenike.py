from __future__ import division as __division__
import numpy as __np__
from numpy import cos as __cos__
from numpy import sin as __sin__
from numpy import sqrt as __sqrt__
import matplotlib.pyplot as __plt__
from matplotlib import cm as __cm__

from . import tools as __tools__
from .phaseunwrap import unwrap2D as __unwrap2D__

def __zernikecartesian__(coefficient,x,y):
	"""
	------------------------------------------------
	__zernikecartesian__(coefficient,x,y):

	Return combined aberration

	Zernike Polynomials Caculation in Cartesian coordinates

	coefficient: Zernike Polynomials Coefficient from input
	x: x in Cartesian coordinates
	y: y in Cartesian coordinates
	------------------------------------------------
	"""
	Z = [0]+coefficient
	r = __sqrt__(x**2 + y**2)
	Z1  =  Z[1]  * 1
	Z2  =  Z[2]  * 2*x
	Z3  =  Z[3]  * 2*y
	Z4  =  Z[4]  * __sqrt__(3)*(2*r**2-1)
	Z5  =  Z[5]  * 2*__sqrt__(6)*x*y
	Z6  =  Z[6]  * __sqrt__(6)*(x**2-y**2)
	Z7  =  Z[7]  * __sqrt__(8)*y*(3*r**2-2)
	Z8  =  Z[8]  * __sqrt__(8)*x*(3*r**2-2)
	Z9  =  Z[9]  * __sqrt__(8)*y*(3*x**2-y**2)
	Z10 =  Z[10] * __sqrt__(8)*x*(x**2-3*y**2)
	Z11 =  Z[11] * __sqrt__(5)*(6*r**4-6*r**2+1)
	Z12 =  Z[12] * __sqrt__(10)*(x**2-y**2)*(4*r**2-3)
	Z13 =  Z[13] * 2*__sqrt__(10)*x*y*(4*r**2-3)
	Z14 =  Z[14] * __sqrt__(10)*(r**4-8*x**2*y**2)
	Z15 =  Z[15] * 4*__sqrt__(10)*x*y*(x**2-y**2)
	Z16 =  Z[16] * __sqrt__(12)*x*(10*r**4-12*r**2+3)
	Z17 =  Z[17] * __sqrt__(12)*y*(10*r**4-12*r**2+3)
	Z18 =  Z[18] * __sqrt__(12)*x*(x**2-3*y**2)*(5*r**2-4)
	Z19 =  Z[19] * __sqrt__(12)*y*(3*x**2-y**2)*(5*r**2-4)
	Z20 =  Z[20] * __sqrt__(12)*x*(16*x**4-20*x**2*r**2+5*r**4)
	Z21 =  Z[21] * __sqrt__(12)*y*(16*y**4-20*y**2*r**2+5*r**4)
	Z22 =  Z[22] * __sqrt__(7)*(20*r**6-30*r**4+12*r**2-1)
	Z23 =  Z[23] * 2*__sqrt__(14)*x*y*(15*r**4-20*r**2+6)
	Z24 =  Z[24] * __sqrt__(14)*(x**2-y**2)*(15*r**4-20*r**2+6)
	Z25 =  Z[25] * 4*__sqrt__(14)*x*y*(x**2-y**2)*(6*r**2-5)
	Z26 =  Z[26] * __sqrt__(14)*(8*x**4-8*x**2*r**2+r**4)*(6*r**2-5)
	Z27 =  Z[27] * __sqrt__(14)*x*y*(32*x**4-32*x**2*r**2+6*r**4)
	Z28 =  Z[28] * __sqrt__(14)*(32*x**6-48*x**4*r**2+18*x**2*r**4-r**6)
	Z29 =  Z[29] * 4*y*(35*r**6-60*r**4+30*r**2-4)
	Z30 =  Z[30] * 4*x*(35*r**6-60*r**4+30*r**2-4)
	Z31 =  Z[31] * 4*y*(3*x**2-y**2)*(21*r**4-30*r**2+10)
	Z32 =  Z[32] * 4*x*(x**2-3*y**2)*(21*r**4-30*r**2+10)
	Z33 =  Z[33] * 4*(7*r**2-6)*(4*x**2*y*(x**2-y**2)+y*(r**4-8*x**2*y**2))
	Z34 =  Z[34] * (4*(7*r**2-6)*(x*(r**4-8*x**2*y**2)-4*x*y**2*(x**2-y**2)))
	Z35 =  Z[35] * (8*x**2*y*(3*r**4-16*x**2*y**2)+4*y*(x**2-y**2)*(r**4-16*x**2*y**2))
	Z36 =  Z[36] * (4*x*(x**2-y**2)*(r**4-16*x**2*y**2)-8*x*y**2*(3*r**4-16*x**2*y**2))
	Z37 =  Z[37] * 3*(70*r**8-140*r**6+90*r**4-20*r**2+1)
	ZW = 	Z1 + Z2 +  Z3+  Z4+  Z5+  Z6+  Z7+  Z8+  Z9+ \
			Z10+ Z11+ Z12+ Z13+ Z14+ Z15+ Z16+ Z17+ Z18+ Z19+ \
			Z20+ Z21+ Z22+ Z23+ Z24+ Z25+ Z26+ Z27+ Z28+ Z29+ \
			Z30+ Z31+ Z32+ Z33+ Z34+ Z35+ Z36+ Z37
	return ZW

def __zernikepolar__(coefficient,r,u):
	"""
	------------------------------------------------
	__zernikepolar__(coefficient,r,u):

	Return combined aberration

	Zernike Polynomials Caculation in polar coordinates

	coefficient: Zernike Polynomials Coefficient from input
	r: rho in polar coordinates
	u: theta in polar coordinates

	------------------------------------------------
	"""
	Z = [0]+coefficient
	Z1  =  Z[1]  * 1*(__cos__(u)**2+__sin__(u)**2)
	Z2  =  Z[2]  * 2*r*__cos__(u)
	Z3  =  Z[3]  * 2*r*__sin__(u)
	Z4  =  Z[4]  * __sqrt__(3)*(2*r**2-1)
	Z5  =  Z[5]  * __sqrt__(6)*r**2*__sin__(2*u)
	Z6  =  Z[6]  * __sqrt__(6)*r**2*__cos__(2*u)
	Z7  =  Z[7]  * __sqrt__(8)*(3*r**2-2)*r*__sin__(u)
	Z8  =  Z[8]  * __sqrt__(8)*(3*r**2-2)*r*__cos__(u)
	Z9  =  Z[9]  * __sqrt__(8)*r**3*__sin__(3*u)
	Z10 =  Z[10] * __sqrt__(8)*r**3*__cos__(3*u)
	Z11 =  Z[11] * __sqrt__(5)*(1-6*r**2+6*r**4)
	Z12 =  Z[12] * __sqrt__(10)*(4*r**2-3)*r**2*__cos__(2*u)
	Z13 =  Z[13] * __sqrt__(10)*(4*r**2-3)*r**2*__sin__(2*u)
	Z14 =  Z[14] * __sqrt__(10)*r**4*__cos__(4*u)
	Z15 =  Z[15] * __sqrt__(10)*r**4*__sin__(4*u)
	Z16 =  Z[16] * __sqrt__(12)*(10*r**4-12*r**2+3)*r*__cos__(u)
	Z17 =  Z[17] * __sqrt__(12)*(10*r**4-12*r**2+3)*r*__sin__(u)
	Z18 =  Z[18] * __sqrt__(12)*(5*r**2-4)*r**3*__cos__(3*u)
	Z19 =  Z[19] * __sqrt__(12)*(5*r**2-4)*r**3*__sin__(3*u)
	Z20 =  Z[20] * __sqrt__(12)*r**5*__cos__(5*u)
	Z21 =  Z[21] * __sqrt__(12)*r**5*__sin__(5*u)
	Z22 =  Z[22] * __sqrt__(7)*(20*r**6-30*r**4+12*r**2-1)
	Z23 =  Z[23] * __sqrt__(14)*(15*r**4-20*r**2+6)*r**2*__sin__(2*u)
	Z24 =  Z[24] * __sqrt__(14)*(15*r**4-20*r**2+6)*r**2*__cos__(2*u)
	Z25 =  Z[25] * __sqrt__(14)*(6*r**2-5)*r**4*__sin__(4*u)
	Z26 =  Z[26] * __sqrt__(14)*(6*r**2-5)*r**4*__cos__(4*u)
	Z27 =  Z[27] * __sqrt__(14)*r**6*__sin__(6*u)
	Z28 =  Z[28] * __sqrt__(14)*r**6*__cos__(6*u)
	Z29 =  Z[29] * 4*(35*r**6-60*r**4+30*r**2-4)*r*__sin__(u)
	Z30 =  Z[30] * 4*(35*r**6-60*r**4+30*r**2-4)*r*__cos__(u)
	Z31 =  Z[31] * 4*(21*r**4-30*r**2+10)*r**3*__sin__(3*u)
	Z32 =  Z[32] * 4*(21*r**4-30*r**2+10)*r**3*__cos__(3*u)
	Z33 =  Z[33] * 4*(7*r**2-6)*r**5*__sin__(5*u)
	Z34 =  Z[34] * 4*(7*r**2-6)*r**5*__cos__(5*u)
	Z35 =  Z[35] * 4*r**7*__sin__(7*u)
	Z36 =  Z[36] * 4*r**7*__cos__(7*u)
	Z37 =  Z[37] * 3*(70*r**8-140*r**6+90*r**4-20*r**2+1)


	Z = Z1 + Z2 +  Z3+  Z4+  Z5+  Z6+  Z7+  Z8+  Z9+ \
		Z10+ Z11+ Z12+ Z13+ Z14+ Z15+ Z16+ Z17+ Z18+ Z19+ \
		Z20+ Z21+ Z22+ Z23+ Z24+ Z25+ Z26+ Z27+ Z28+ Z29+ \
		Z30+ Z31+ Z32+ Z33+ Z34+ Z35+ Z36+ Z37
	return Z


def twyman_green(coefficients, lambda_1 = 632, PR = 1):
	"""
	Genertate Twyman_Green Interferogram based on zernike polynomials
	=============================================

	input
	----------------------------------------------

	Class zernike polynomials coefficients in wavenumber

	see Class:opticspy.zernike.Coefficients

	lambda_1: wavelength in nanometer, default = 632nm
	PR: pupil radius, default = 1mm

	output
	----------------------------------------------
	Interferogram of aberration
	"""
	lambda_1 = lambda_1*(10**-9)
	coefficients = coefficients.__coefficients__
	r = __np__.linspace(-PR, PR, 400)
	x, y = __np__.meshgrid(r,r)
	rr = __np__.sqrt(x**2 + y**2)
	OPD = __zernikecartesian__(coefficients,x,y)*2/PR

	ph = 2 * __np__.pi * OPD
	I1 = 1
	I2 = 1
	Ixy = I1 + I2 + 2 * __np__.sqrt(I1*I2) * __np__.cos(ph)
	__tools__.makecircle(Ixy, r, PR)
#======================================================
	fig = __plt__.figure(figsize=(9, 6), dpi=80)
	__plt__.imshow(-Ixy, extent=[-PR,PR,-PR,PR])
	__plt__.set_cmap('Greys')

	label = 'Zernike Coefficients:'
	m = 1
	for i in coefficients:
		if i!=0:
			label = label + "Z" + str(m) + "=" + str(i) +" "
		m = m + 1
	__plt__.xlabel(label,fontsize=16)
	__plt__.title('Twyman Green Interferogram',fontsize=16)
	fig.set_tight_layout(True)
	__plt__.show()

################################################################

def phase_shift(coefficients, lambda_1 = 632, PR = 1, type = '4-step', noise = 0, sample = 200):
	"""
	Genertate phase_shift Interferogram from interferometer
	based on zernike polynomials and twyman_green interferometer
	===========================================================

	input
	----------------------------------------------

	Class zernike polynomials coefficients in wavenumber

	see Class:opticspy.zernike.Coefficients

	lambda_1: wavelength in nanometer, default = 632nm
	PR: pupil radius, default = 1(also use this value for aperture matrix generate)
	type: PSI algorithm default:'4-step'
	boundary: if have a aperture
	noise: from 0 to 1, default 0
	sample: sample points

	output
	----------------------------------------------
	Interferogram of aberration
	"""
	lambda_1 = lambda_1*(10**-9)
	coefficients = coefficients.__coefficients__
	r = __np__.linspace(-PR, PR, sample)
	x, y = __np__.meshgrid(r,r)
	rr = __np__.sqrt(x**2 + y**2)
	OPD = __zernikecartesian__(coefficients,x,y)*2/PR
	Ia = 1
	Ib = 1
	ph = 2 * __np__.pi * OPD

	if type == "4-step":
		__tools__.makecircle_boundary(OPD, r, PR, 0)
		im = __plt__.imshow(OPD,extent=[-PR,PR,-PR,PR],cmap=__cm__.RdYlGn)
		__plt__.colorbar()
		__plt__.title('Surface figure',fontsize=16)
		__plt__.show()

		I1 = Ia + Ib + 2 * __np__.sqrt(Ia*Ib) * __np__.cos(ph)
		I2 = Ia + Ib + 2 * __np__.sqrt(Ia*Ib) * __np__.cos(ph+90.0/180*__np__.pi)
		I3 = Ia + Ib + 2 * __np__.sqrt(Ia*Ib) * __np__.cos(ph+180.0/180*__np__.pi)
		I4 = Ia + Ib + 2 * __np__.sqrt(Ia*Ib) * __np__.cos(ph+270.0/180*__np__.pi)
		if noise != 0:
			# add noise / default noise 0
			I1 = I1 + I1*noise*__np__.random.randn(sample,sample)
			I2 = I2 + I2*noise*__np__.random.randn(sample,sample)
			I3 = I3 + I3*noise*__np__.random.randn(sample,sample)
			I4 = I4 + I4*noise*__np__.random.randn(sample,sample)
		__tools__.makecircle_boundary(I1, r, PR, 0)
		__tools__.makecircle_boundary(I2, r, PR, 0)
		__tools__.makecircle_boundary(I3, r, PR, 0)
		__tools__.makecircle_boundary(I4, r, PR, 0)
		I = [I1,I2,I3,I4]
		__tools__.phase_shift_figure(I,PR,type = "4-step")
		M = __np__.ones([sample,sample])	 #map matrix, which is boundary
		__tools__.makecircle_boundary(M, r, PR, 0)

		# fig = __plt__.figure(figsize=(8, 6), dpi=80)
		# im = __plt__.pcolormesh(M,cmap=__cm__.RdYlGn)
		# __plt__.title('Phase value map',fontsize=16)
		# __plt__.colorbar()
		# __plt__.show()

		return [I,PR,M,sample]
	else:
		print("No this type of PSI")

def rebuild_surface(data, shifttype = "4-step", unwraptype = "unwrap2D", noise = True):
	"""
	Rebuild surface function
	============================================
	input
	--------------------------------------------
	data: Interferogram data from PSI
	shifttype: PSI type, default 4-step PSI
	unwraptype: phaseunwrap type, default "simple"

	output
	--------------------------------------------
	rebuild surface matrix
	"""
	if shifttype == "4-step" and unwraptype == "simple" and noise == False:
		I = data[0]
		PR = data[1]
		ph = __np__.arctan2((I[3]-I[1]),(I[0]-I[2]))
		fig = __plt__.figure(figsize=(9, 6), dpi=80)
		im = __plt__.imshow(ph,extent=[-PR,PR,-PR,PR],cmap=__cm__.RdYlGn)
		__plt__.title('Wrapped phase',fontsize=16)
		__plt__.colorbar()
		__plt__.show()
		#-----------------------Phase unwrap-------------------------
		rebuild_ph = __unwrap2D__(ph,type = "simple")
		rebuild_surface = rebuild_ph/2/__np__.pi*PR/2
		#------------------------------------------------------------
		fig = __plt__.figure(figsize=(9, 6), dpi=80)
		im = __plt__.imshow(rebuild_surface,extent=[-PR,PR,-PR,PR],cmap=__cm__.RdYlGn)
		__plt__.title('Rebuild Surface',fontsize=16)
		__plt__.colorbar()
		__plt__.show()
		return rebuild_surface

	elif shifttype == "4-step" and unwraptype == "unwrap2D" and noise == True:
		I = data[0]
		PR = data[1]
		M = data[2]
		s = data[3]
		r = __np__.linspace(-PR, PR, s)
		ph = __np__.arctan2((I[3]-I[1]),(I[0]-I[2]))
		fig = __plt__.figure(figsize=(9, 6), dpi=80)
		im = __plt__.imshow(ph,extent=[-PR,PR,-PR,PR],cmap=__cm__.RdYlGn)
		__plt__.title('Wrapped phase',fontsize=16)
		__plt__.colorbar()
		__plt__.show()
		#-----------------------Phase unwrap-------------------------
		ph1 = [ph,M,s]
		rebuild_ph = __unwrap2D__(ph1,noise = True)
		rebuild_surface = rebuild_ph/2/__np__.pi*PR/2
		__tools__.makecircle_boundary(rebuild_surface, r, PR, 0)
		fig = __plt__.figure(figsize=(9, 6), dpi=80)
		im = __plt__.imshow(rebuild_surface,extent=[-PR,PR,-PR,PR],cmap=__cm__.RdYlGn)
		__plt__.title('Rebuild Surface',fontsize=16)
		__plt__.colorbar()
		__plt__.show()
		return rebuild_surface

	else:
		print("No this kind of phase shift type")
		return 0



