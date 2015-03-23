import numpy as __np__
import matplotlib.pyplot as __plt__
import zernike as __zernike__

def __makecircle__(a, r, PR):
	max = a.max()
	size = __np__.sqrt(a.size)
	for i in range(int(size)):
		for j in range(int(size)):
			if __np__.sqrt(r[i]**2+r[j]**2) > PR:
				a[i,j] = max

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
	def wavenumber(n):
	     return n*lambda_1/PR
	coefficients_new =  map(wavenumber, coefficients)
	OPD = 	__zernike__.__zernikecartesian__(coefficients_new,x,y)
	ph = 2 * __np__.pi / lambda_1 * OPD

	I1 = 1
	I2 = 1
	Ixy = I1 + I2 + 2 * __np__.sqrt(I1*I2) * __np__.cos(ph)
	__makecircle__(Ixy, r, PR) 
#======================================================
	fig = __plt__.figure(1)
	__plt__.imshow(-Ixy, extent=[-PR,PR,-PR,PR])
	__plt__.set_cmap('Greys')

	label = 'Zernike Coefficients:'
	m = 0
	for i in coefficients:
		if i!=0:
			label = label + "Z" + str(m) + "=" + str(i) +" "
		m = m + 1	
	__plt__.xlabel(label,fontsize=15)
	__plt__.title('Twyman Green Interferogram',fontsize=15)
	fig.set_tight_layout(True)
	__plt__.show()

################################################################
################################################################