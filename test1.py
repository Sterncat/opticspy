import numpy
import matplotlib.pyplot as plt
import zernike

def makecircle(a, r, PR):
	max = a.max()
	size = numpy.sqrt(a.size)
	for i in range(int(size)):
		for j in range(int(size)):
			if numpy.sqrt(r[i]**2+r[j]**2) > PR:
				a[i,j] = max

def twyman_green_zernike(Z0=0, Z1=0, Z2=0, Z3=0, Z4=0, Z5=0, Z6=0, Z7=0, \
						Z8=0, Z9=0, Z10=0, Z11=0, Z12=0, Z13=0, Z14=0, \
						Z15=0, Z16=0, Z17=0, Z18=0, Z19=0, Z20=0, Z21=0, \
						Z22=0, Z23=0, Z24=0, Z25=0, Z26=0, Z27=0, Z28=0, \
						Z29=0, Z30=0, Z31=0, Z32=0, Z33=0, Z34=0, Z35=0, \
						lambda_1 = 632, PR = 1):
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
	coefficients = [A*2,B*2,C*2,D*2,E*2,F*2,G*2]
	r = numpy.linspace(-PR, PR, 400)
	x, y = numpy.meshgrid(r,r) 
	rr = numpy.sqrt(x**2 + y**2)
	def wavenumber(n):
	     return n*lambda_1*2/PR
	[A,B,C,D,E,F,G] =  map(wavenumber, [A,B,C,D,E,F,G])
	OPD = 	zernike.zernike(x,y,Z5=3)
	ph = 2 * numpy.pi / lambda_1 * OPD

	I1 = 1
	I2 = 1
	Ixy = I1 + I2 + 2 * numpy.sqrt(I1*I2) * numpy.cos(ph)
	makecircle(Ixy, r, PR) 
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
				label = label + str(i/2) + r'$\lambda$' + ' ' + labellist[count] + '\n'
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

################################################################
################################################################