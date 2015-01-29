import numpy as np
from math import sqrt
import pltshow
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
		#print self.aper
		pltshow.apershow(self.aper)

	def diffraction(self):
		"""
		Compute the cirlce aperture's diffraction pattern.

		Output
		------------------------------------
		Diffraction pattern figure

		"""
		print "---------diffraction----------"
		aperfft = np.fft.fftshift(np.fft.fft2(self.aper))
		pltshow.apershow(aperfft)

	def otf(self):
		"""
		Compute an aperture's otf
		"""
		print "-------------OTF---------------"
		aperfft = np.fft.fftshift(np.fft.fft2(self.aper))**2
		aper_OTF = np.fft.fftshift(np.fft.fft2(aperfft))
		pltshow.apershow(aper_OTF)


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

	radius: int
				aperture radius

	"""
	def __init__(self, background, radius):
		#self.background = background
		#self.radius = radius

		n = background
		Aperture.aper = np.zeros([n,n])
		for i in range(n):
			for j in range(n):
				r = sqrt((i-n/2)**2+(j-n/2)**2)
				if r < radius:
					Aperture.aper[i,j] = 1

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
		aper1 = np.ones(matrix_1)
		Aperture.aper = np.zeros([n,n])
		Aperture.aper[(n/2-height/2):(n/2+height/2),(n/2-width/2):(n/2+width/2)] = aper1






