import numpy
import matplotlib.pyplot as plt
def Twyman_Green(A, B, C, D, E, F, G, lambda_1 = 632, PR = 1):
	"""
	Genertate Twyman_Green Interferogram
	=============================================
	
	input
	----------------------------------------------
	
	coefficients in wavenumber(ex. D=8 means 8 max error 
				in defocus aberration)

	A: Constant(piston)term
	B: Tilt about the y axis
	C: Tilt about the x axis
	D: Reference sphere change, also called defocus
	E: Sagittal astigmatism along the y axis
	F: Sagittal coma along the y axis
	G: Primary spherical aberration
	lambda_1: wavelength in nanometer, default = 632nm
	PR: pupil radius, default = 1

	output
	----------------------------------------------
	Interferogram of aberration
	"""
	lambda_1 = lambda_1*(10**-9)
	coefficients = [A,B,C,D,E,F,G]
	r = numpy.linspace(-PR, PR, 400)
	x, y = numpy.meshgrid(r,r) 
	rr = numpy.sqrt(x**2 + y**2)
	def wavenumber(n):
	     return n*lambda_1
	[A,B,C,D,E,F,G] =  map(wavenumber, [A,B,C,D,E,F,G])
	OPD = 	A + \
			B * x + \
			C * y + \
			D * (x**2 + y**2) + \
	  		E * (x**2 + 3 * y**2) + \
	  		F * y * (x**2 + y**2) + \
	  		G * (x**2 + y**2)**2

	ph = 2 * numpy.pi / lambda_1 * OPD

	I1 = 1
	I2 = 1
	Ixy = I1 + I2 + 2 * numpy.sqrt(I1*I2) * numpy.cos(ph)
	def makecircle(a):
		max = a.max()
		size = numpy.sqrt(a.size)
		for i in range(int(size)):
			for j in range(int(size)):
				if numpy.sqrt(r[i]**2+r[j]**2) > PR:
					a[i,j] = max
	makecircle(Ixy) 
#======================================================
	fig = plt.figure(1)
	plt.imshow(Ixy, extent=[-PR,PR,-PR,PR])
	plt.set_cmap('Greys')

	label = ''
	def	labelgenerate(b):
		label = 'Interferogram with '
		count = 0
		count_1 = 0
		labellist = ['A: piston',
		'B: Tilt about the y axis',
		'C: Tilt about the x axis',
		'D: Defocus',
		'E: Sagittal astigmatism along the y axis',
		'F: Sagittal coma along the y axis',
		'G: Primary spherical aberration']
		for i in b:
			if i != 0:
				label = label + str(i) + r'$\lambda$' + ' ' + labellist[count] + '\n'
			else:
				count_1 = count_1 + 1
			count = count + 1
		if count_1 == len(b):
			label = label + ' ' + 'no aberration'
		return label
	label = labelgenerate(coefficients)
	plt.xlabel(label,fontsize=15)
	plt.title('Twyman Green Interferogram',fontsize=15)
	fig.set_tight_layout(True)
	plt.show()