import numpy as __np__
import matplotlib.pyplot as __plt__

def __apershow__(obj):
	obj = -abs(obj)
	__plt__.imshow(obj)
	__plt__.set_cmap('Greys')
	__plt__.show()
def fresnel(aperture,z = 2,lambda1 = 660*10**(-9)):
	aperturelist = ['rectangle','doublerectangle','frame','doublecircle','ring']
	if aperture.__type__ == 'circle':
		n = aperture.__background__
		d = aperture.__d__
		D = aperture.__D__
		scale = aperture.__scale__
		Nf = D**2/(4*lambda1*z);  #Fresnel number. Smaller is better for single-DFT Fresnel
		print "Fresnel number = ", Nf
	elif aperture.__type__ in aperturelist:
		print aperture.__type__
		n = aperture.__background__
		scale = aperture.__scale__
	else:
		print "No this kind aperture for fresnel diffraction"

	x1 = __np__.linspace(-n/2+1,n/2,n)
	[x,y] = __np__.meshgrid(x1,x1)
	# Single-DFT
	e1 = __np__.exp(1j*2*__np__.pi/lambda1*(x**2+y**2)/2/z*((scale)**2))
	diffraction = __np__.fft.fftshift(__np__.fft.fft2(aperture.__aper__*e1))
	__apershow__(diffraction)
	return diffraction

def fraunhofer(aperture, z = 2, lambda1 = 660*10**(-9)):
	"""
	Fraunhofer diffraction
	"""
	diffraction = 1j*__np__.exp(1j*2*__np__.pi/lambda1*z)/lambda1/z*__np__.fft.fftshift(__np__.fft.fft2(aperture.__aper__))
	__apershow__(diffraction)
	return 0