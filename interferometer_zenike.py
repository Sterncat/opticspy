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
	PR: pupil radius, default = 1

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

def phase_shift(coefficients, lambda_1 = 632, PR = 1,type = '4-step',sample = 200):
	"""
	Genertate phase_shift Interferogram from interferometer
	based on zernike polynomials and twyman_green interferometer
	===========================================================
	
	input
	----------------------------------------------
	
	Class zernike polynomials coefficients in wavenumber
	 
	see Class:opticspy.zernike.Coefficients
	
	lambda_1: wavelength in nanometer, default = 632nm
	PR: pupil radius, default = 1
	type: PSI algorithm default:'4-step'
	sample: sample points

	output
	----------------------------------------------
	Interferogram of aberration
	"""
	if type == "4-step":
		lambda_1 = lambda_1*(10**-9)
		coefficients = coefficients.__coefficients__
		r = __np__.linspace(-PR, PR, sample)
		x, y = __np__.meshgrid(r,r) 
		rr = __np__.sqrt(x**2 + y**2)
		OPD = 	__zernike__.__zernikecartesian__(coefficients,x,y)*2/PR

		im = __plt__.imshow(OPD,extent=[-PR,PR,-PR,PR],cmap=__cm__.RdYlGn)
		__plt__.colorbar()
		__plt__.title('Surface figure',fontsize=16)
		__plt__.show()

		ph = 2 * __np__.pi * OPD
		Ia = 1
		Ib = 1
		I1 = Ia + Ib + 2 * __np__.sqrt(Ia*Ib) * __np__.cos(ph)
		I2 = Ia + Ib + 2 * __np__.sqrt(Ia*Ib) * __np__.cos(ph+90.0/180*__np__.pi)
		I3 = Ia + Ib + 2 * __np__.sqrt(Ia*Ib) * __np__.cos(ph+180.0/180*__np__.pi)
		I4 = Ia + Ib + 2 * __np__.sqrt(Ia*Ib) * __np__.cos(ph+270.0/180*__np__.pi)
		I = [I1,I2,I3,I4]
		
		f, axarr = __plt__.subplots(2, 2, figsize=(9, 9), dpi=80)
		axarr[0, 0].imshow(-I1, extent=[-PR,PR,-PR,PR],cmap=__cm__.Greys)
		axarr[0, 0].set_title(r'$Phase\ shift: 0$',fontsize=16)
		axarr[0, 1].imshow(-I2, extent=[-PR,PR,-PR,PR],cmap=__cm__.Greys)
		axarr[0, 1].set_title(r'$Phase\ shift: 1/2\pi$',fontsize=16)
		axarr[1, 0].imshow(-I3, extent=[-PR,PR,-PR,PR],cmap=__cm__.Greys)
		axarr[1, 0].set_title(r'$Phase\ shift: \pi$',fontsize=16)
		axarr[1, 1].imshow(-I4, extent=[-PR,PR,-PR,PR],cmap=__cm__.Greys)
		axarr[1, 1].set_title(r'$Phase\ shift: 3/2\pi$',fontsize=16)
		__plt__.suptitle('4-step Phase Shift Interferograms',fontsize=16)
		__plt__.show()
		return [I,PR]
	else:
		print "No this type of PSI"

def rebuild_surface(data, shifttype = "4-step", unwraptype = "simple"):
	I = data[0]
	PR = data[1]
	if shifttype == "4-step":
		ph = __np__.arctan2((I[3]-I[1]),(I[0]-I[2]))
		fig = __plt__.figure(figsize=(9, 6), dpi=80)
		im = __plt__.imshow(ph,extent=[-PR,PR,-PR,PR],cmap=__cm__.RdYlGn)
		__plt__.title('Wrapped phase',fontsize=16)
		__plt__.colorbar()
		__plt__.show()
		#-----------------------Phase unwrap-------------------------
		rebuild_ph = __unwrap2D__(ph,type = "simple")
		rebuild_surface = rebuild_ph/2/__np__.pi
		#------------------------------------------------------------
		fig = __plt__.figure(figsize=(9, 6), dpi=80)
		im = __plt__.imshow(rebuild_surface,extent=[-PR,PR,-PR,PR],cmap=__cm__.RdYlGn)
		__plt__.title('Rebuild Surface',fontsize=16)
		__plt__.colorbar()
		__plt__.show()
		return rebuild_surface
	else:
		print "No this kind of phase shift type"
		return 0










