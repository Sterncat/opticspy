from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
import zernike as __zernike__
import tools as __tools__
from phaseunwrap import unwrap2D as __unwrap2D__
from matplotlib import cm as __cm__



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
	OPD = 	__zernike__.__zernikecartesian__(coefficients,x,y)*2/PR

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
	OPD = 	__zernike__.__zernikecartesian__(coefficients,x,y)*2/PR
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
		print "No this type of PSI"

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
		print "No this kind of phase shift type"
		return 0



