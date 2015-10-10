import numpy as __np__
import matplotlib.pyplot as __plt__
import diffraction as __diffraction__
import tools as __tools__

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
		extent = self.__scale__ * self.__background__
		__tools__.__apershow__(self.__aper__, extent)

	def fresnel(self,z = 2,lambda1 = 660*10**(-9)):
		"""
		Compute the fresnel diffraction pattern.

		Output
		------------------------------------
		Diffraction pattern figure

		"""
		print "---------Fresnel Diffraction----------"
		__diffraction__.fresnel(self,z,lambda1)
		return 0
	def fraunhofer(self,z = 2,lambda1 = 660*10**(-9)):
		"""
		Compute the frauhofer diffraction pattern.

		Output
		------------------------------------
		Diffraction pattern figure

		"""
		print "---------Fraunhofer Diffraction----------"
		__diffraction__.fraunhofer(self,z,lambda1)
		return 0

	def otf(self):
		"""
		Compute an aperture's otf
		"""
		print "-------------OTF---------------"
		aperfft = __np__.fft.fftshift(__np__.fft.fft2(self.__aper__))**2
		aper_OTF = __np__.fft.fftshift(__np__.fft.fft2(aperfft))
		__tools__.__apershow__(aper_OTF,extent = 0)
		return 0


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
	def __init__(self, background=500, d=200, D = 0.01, scale = 0.01/200):
		self.__type__ = 'circle'
		self.__background__ = n = background
		self.__d__ = d
		self.__D__ = d*scale
		self.__scale__ = scale
		radius = d/2
		self.__aper__ = __np__.zeros([n,n])
		aper1 = __tools__.circle_aperture(d)
		self.__aper__[(n/2-d/2):(n/2-d/2+d),(n/2-d/2):(n/2-d/2+d)] = aper1

class DoubleCircle(Aperture):
	def __init__(self, background=500, d=50, D=0.01, separation = 100, scale=0.01/200):
		self.__type__ = 'doublecircle'
		self.__background__ = n = background
		self.__d__ = DoubleRectangle
		self.__D__ = D
		self.__scale__ = scale
		self.__separation__ = s = separation
		radius = d/2
		self.__aper__ = __np__.zeros([n,n])

		aper1 = __tools__.circle_aperture(d)
		self.__aper__[(n/2-d/2):(n/2-d/2+d),(n/2-s/2-d/2):(n/2-s/2+d/2)] = aper1
		self.__aper__[(n/2-d/2):(n/2-d/2+d),(n/2+s/2-d/2):(n/2+s/2+d/2)] = aper1

class Ring(Aperture):
	def __init__(self, background=500, outside=200, inside=100, scale=0.01/200):
		self.__type__ = 'ring'
		self.__background__ = n = background
		self.__outside__ = outside
		self.__inside__ = inside
		self.__scale__ = scale
		self.__aper__ = __np__.zeros([n,n])

		aper1 = __tools__.circle_aperture(inside)
		aper2 = __tools__.circle_aperture(outside)

		aper2[(outside/2-inside/2):(outside/2-inside/2+inside),(outside/2-inside/2):(outside/2-inside/2+inside)] = -1*(aper1-1)
		self.__aper__[(n/2-outside/2):(n/2-outside/2+outside),(n/2-outside/2):(n/2-outside/2+outside)] = aper2

class Rectangle(Aperture):
	def __init__(self, background=500, height=200, width=200, scale=0.01/200):
		"""
		Build a rectangle aperture instance
		
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
		self.__type__ = 'rectangle'
		n = self.__background__ = background
		self.__height__ = height
		self.__width__ = width
		self.__scale__ = scale
		#matrix_1 = [height,width]
		aper1 = __np__.ones([height,width])
		self.__aper__ = __np__.zeros([n,n])
		self.__aper__[(n/2-height/2):(n/2-height/2+height),(n/2-width/2):(n/2-width/2+width)] = aper1

class DoubleRectangle(Aperture):
	def __init__(self, background=500, height=50, width=2, separation=4, scale=0.01/200):
		"""
		Build a DoubleRectangle aperture instance, could use as a doubleslit aperture
		"""
		self.__type__ = "doublerectangle"
		n = self.__background__ = background
		self.__height__ = height
		self.__width__ = width
		self.__separation__ = separation
		self.__scale__ = scale
		self.__aper__ = __np__.zeros([n,n])
		aper1 = __np__.ones([height,width])
		self.__aper__[(n/2-height/2):(n/2-height/2+height),(n/2-width/2-separation/2):(n/2-width/2+width-separation/2)] = aper1
		self.__aper__[(n/2-height/2):(n/2-height/2+height),(n/2-width/2+separation/2):(n/2-width/2+width+separation/2)] = aper1

class Frame(Aperture):
	def __init__(self, background=500, outside=200, inside=100, scale=0.01/200):
		self.__type__ = "frame"
		n = self.__background__ = background
		self.__outside__ = outside
		self.__inside__ = inside
		self.__scale__ = scale
		self.__aper__ = __np__.zeros([n,n])
		aper1 = __np__.ones([outside,outside])
		aper2 = __np__.zeros([inside,inside])
		self.__aper__[(n/2-outside/2):(n/2-outside/2+outside),(n/2-outside/2):(n/2-outside/2+outside)] = aper1
		self.__aper__[(n/2-inside/2):(n/2-inside/2+inside),(n/2-inside/2):(n/2-inside/2+inside)] = aper2