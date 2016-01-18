import numpy as __np__
import matplotlib.pyplot as __plt__
import tools as __tools__

def twyman_green(A=0, B=0, C=0, D=0, E=0, F=0, G=0, lambda_1 = 632, PR = 1):
	"""
	Genertate Twyman_Green Interferogram based on Seidel aberration
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
	lambda_1 = lambda_1*(1e-9)
	coefficients = [A,B,C,D,E,F,G]
	r = __np__.linspace(-PR, PR, 400)
	x, y = __np__.meshgrid(r,r) 
	rr = __np__.sqrt(x**2 + y**2)
	wavemap = lambda n: n*lambda_1*2/PR
	[A,B,C,D,E,F,G] =  map(wavemap, [A,B,C,D,E,F,G])
	OPD = 	A + \
			B * x + \
			C * y + \
			D * (x**2 + y**2) + \
	  		E * (x**2 + 3 * y**2) + \
	  		F * y * (x**2 + y**2) + \
	  		G * (x**2 + y**2)**2
	ph = 2 * __np__.pi/lambda_1 * OPD
	I1 = 1
	I2 = 1
	Ixy = I1 + I2 + 2 * __np__.sqrt(I1*I2) * __np__.cos(ph)
	__tools__.makecircle(Ixy, r, PR) 
#======================================================
	fig = __plt__.figure(figsize=(9, 6), dpi=80)
	__plt__.imshow(-Ixy, extent=[-PR,PR,-PR,PR])
	__plt__.set_cmap('Greys')

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
	__plt__.xlabel(label,fontsize=16)
	__plt__.title('Twyman Green Interferogram',fontsize=16)
	fig.set_tight_layout(True)
	__plt__.show()

################################################################
################################################################


def lateral_shear(A=0, B=0, C=0, D=0, E=0, S=0.1, lambda_1 = 632, PR = 1):
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
	r = __np__.linspace(-PR, PR, 400)
	#r1 = __np__.linspace(-PR-S/2,PR+S/2)
	x, y = __np__.meshgrid(r,r) 
	rr = __np__.sqrt(x**2 + y**2)
	coefficients = [A*2,B*2,C*2,D*2,E*2]
	def wavenumber(n):
	     return n*lambda_1*2/PR
	[A,B,C,D,E] =  map(wavenumber, [A,B,C,D,E])
	OPD = 	4 * A * (x**2 + y**2) * x * S + \
			2 * B * x * y * S  + \
			C * x * S + \
			2 * D * x * S + \
	  		E * y
	ph = 2 * __np__.pi / lambda_1 * OPD

	I1 = 1
	I2 = 1
	Ixy = -(I1 + I2 + 2 * __np__.sqrt(I1 * I2) * __np__.cos(ph))

	def doublecircle(a, PR, S):
		x = int(400+200*S/PR)
		y = 400
		rec = __np__.zeros((y,x))
		for i in range(400):
			for j in range(400):
				rec[j, i+100*S/PR] = a[j, i]

		x1 = __np__.linspace(-PR-S/2, PR+S/2, x)
		y1 = __np__.linspace(-PR, PR, y)
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
	fig = __plt__.figure(figsize=(9, 6), dpi=80)
	__plt__.imshow(Ixy_new, extent=[-PR-S/2,PR+S/2,-PR,PR])
	__plt__.set_cmap('Greys')

	label = ''
	def	labelgenerate(b):
		label = 'Shear Interferogram with ' + str(S) +' shearing in x' + '\n\n'
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

	__plt__.xlabel(label,fontsize=16)
	__plt__.title('Lateral Shear Interferogram',fontsize=16)
	fig.set_tight_layout(True)
	__plt__.show()



