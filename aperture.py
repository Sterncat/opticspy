import numpy as __np__
import matplotlib.pyplot as __plt__
import diffraction as __diffraction__

def __apershow__(obj):
	obj = -abs(obj)
	__plt__.imshow(obj)
	__plt__.set_cmap('Greys')
	__plt__.show()


class Aperture():
	def __init__(self, background):
		self.background = background

	def show(self):

		"""
		Show aperture figure

		Output
		------------------------------------
		Aperture figure

		"""

		print "---------show aperture--------"
		__apershow__(self.__aper__)

	def diffraction(self):
		"""
		Compute the cirlce aperture's diffraction pattern.

		Output
		------------------------------------
		Diffraction pattern figure

		"""
		print "---------diffraction----------"
		aperfft = __np__.fft.fftshift(__np__.fft.fft2(self.__aper__))
		__apershow__(aperfft)

	def otf(self):
		"""
		Compute an aperture's otf
		"""
		print "-------------OTF---------------"
		aperfft = __np__.fft.fftshift(__np__.fft.fft2(self.__aper__))**2
		aper_OTF = __np__.fft.fftshift(__np__.fft.fft2(aperfft))
		__apershow__(aper_OTF)


class Circle(Aperture):
	"""
	Build a circle aperture example

	Example
	------------------------------------
	aperture = opticspy.aper.Circle(200,50)
	
 	Parameters
	------------------------------------
	background: int
				Square background

	d: int
				aperture pixel diameter
	D: int
				aperture real diameter

	"""
	def __init__(self, background=500, d=250, D=0.05):
		self.__background__ = background
		self.__d__ = d
		self.__D__ = D
		self.__scale__ = D/d
		n = background
		radius = d/2
		Aperture.__aper__ = __np__.zeros([n,n])
		for i in range(n):
			for j in range(n):
				r = __np__.sqrt((i-n/2)**2+(j-n/2)**2)
				if r < radius:
					Aperture.__aper__[i,j] = 1

class Rectangle(Aperture):
	def __init__(self, background, height, width):
		"""
		Build a  rectangle aperture example
		
		Example
		-----------
		aperture = opticspy.aper.Rectangle(200,20,40)
		
	 	Parameters
		-----------
		background: int
					Square background
		height: int
					aperture height
		width: int
					aperture width
		"""
		#self.background = background
		#self.height = height
		#self.width = width
		n = background
		matrix_1 = [height,width]
		aper1 = __np__.ones(matrix_1)
		Aperture.aper = __np__.zeros([n,n])
		Aperture.aper[(n/2-height/2):(n/2+height/2),(n/2-width/2):(n/2+width/2)] = aper1






