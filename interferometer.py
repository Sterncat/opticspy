import numpy
import matplotlib.pyplot as plt

def makecircle(a, r, PR):
	max = a.max()
	size = numpy.sqrt(a.size)
	for i in range(int(size)):
		for j in range(int(size)):
			if numpy.sqrt(r[i]**2+r[j]**2) > PR:
				a[i,j] = max

def twyman_green(A, B, C, D, E, F, G, lambda_1 = 632, PR = 1):
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


def lateral_shear(A, B, C, D, E, S, lambda_1 = 632, PR = 1):
	"""
	Genertate Lateral_Shear Interferogram
	=============================================
	
	input
	Lateral_Shear(A, B, C, D, E, S, lambda_1 = 632, PR = 1):
	----------------------------------------------
	
	coefficients in wavenumber(ex. D=8 means 8 max error 
				in defocus aberration)

	A: Primary spherical aberration
	B: Coma
	C: Astigmatism
	D: Defocus
	E: x-Tilt
	S: Shear distance(positive)
	lambda_1: wavelength in nanometer, default = 632nm
	PR: pupil radius, default = 1

	output
	----------------------------------------------
	Lateral Shear interferogram of aberration
	"""
	lambda_1 = lambda_1*(10**-9)
	r = numpy.linspace(-PR, PR, 400)
	#r1 = numpy.linspace(-PR-S/2,PR+S/2)
	x, y = numpy.meshgrid(r,r) 
	rr = numpy.sqrt(x**2 + y**2)
	coefficients = [A*2,B*2,C*2,D*2,E*2]
	def wavenumber(n):
	     return n*lambda_1*2/PR
	[A,B,C,D,E] =  map(wavenumber, [A,B,C,D,E])
	OPD = 	4 * A * (x**2 + y**2) * x * S + \
			2 * B * x * y * S  + \
			C * x * S + \
			2 * D * x * S + \
	  		E * y
	ph = 2 * numpy.pi / lambda_1 * OPD

	I1 = 1
	I2 = 1
	Ixy = -(I1 + I2 + 2 * numpy.sqrt(I1 * I2) * numpy.cos(ph))

	def doublecircle(a, PR, S):
		x = int(400+200*S/PR)
		y = 400
		rec = numpy.zeros((y,x))
		for i in range(400):
			for j in range(400):
				rec[j, i+100*S/PR] = a[j, i]

		x1 = numpy.linspace(-PR-S/2, PR+S/2, x)
		y1 = numpy.linspace(-PR, PR, y)
		max = a.max()
		min = a.min()
		for i in range(x):
			for j in range(y):
				a1 = (x1[i] + S/2)**2 + (y1[j])**2
				a2 = (x1[i] - S/2)**2 + (y1[j])**2
				if a1 > PR**2 and a2 > PR**2:
					rec[j,i] = max
				elif (a1 > PR**2 and a2 < PR**2) or (a1 < PR**2 and a2 >PR**2):
					rec[j,i] = min*2/10
		return rec
	Ixy_new = doublecircle(Ixy, PR, S) 
	fig = plt.figure(1)
	plt.imshow(Ixy_new, extent=[-PR-S/2,PR+S/2,-PR,PR])
	plt.set_cmap('Greys')

	label = ''
	def	labelgenerate(b):
		label = 'Shaer Interferogram with ' + str(S) +' shearing in x' + '\n\n'
		count = 0
		count_1 = 0
		labellist = ['A: Primary spherical aberration',
		'B: Coma',
		'C: Astigmatism',
		'D: Defocus',
		'E: x-Tilt']
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
	plt.title('Lateral Shear Interferogram',fontsize=15)
	fig.set_tight_layout(True)
	plt.show()



