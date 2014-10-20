import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

def apershow(aper_fft, clipfactor):

	aper_fft = abs(aper_fft)
	gamax=aper_fft.max()
	gamin=aper_fft.min()
	print gamax
	print gamin
#	scale=0.25*255*clipfactor/gamax
#	ga=min(scale*aper_fft,255);
	plt.imshow(aper_fft,vmax=gamax, vmin=gamin)
	plt.show()
	
def rec(background_size, rec_height, rec_width, row_start, col_start, clipfactor):
	"""
	Compute the rectangle aperture's diffraction pattern.
	
 	Parameters
	-----------
	background_size: int
				Square background
	rec_height: int
				aperture height
	rec_width: int
				aperture width
	row_start: int
				aperture x position
	col_start: int
				aperture y position
				
	returns
	-----------
	out: aperture's matrix and figure of diffraction pattern
	"""
	n = background_size
	height = rec_height
	width = rec_width
	rowstart = row_start
	colstart = col_start
	clipfactor = clipfactor
	matrix_1 = [height,width]
	aper = np.ones(matrix_1)
	aper1 = np.zeros([n,n])
	aper1[(rowstart-1):(rowstart-1+height),(colstart-1):(colstart-1+width)] = aper
	print "aperture_matrix:",aper1
	aperfft = np.fft.fftshift(np.fft.fft2(aper1))
	apershow(aperfft,1)
	
	
	

def circle(background_size, center, radius, clipfactor):
	n = background_size
	xcenter = center[0]+n/2
	ycenter = center[1]+n/2
	radius = radius
	clipfactor = clipfactor
	print n, xcenter, ycenter, radius, clipfactor
#	matrix_1 = [height,width]
#	aper = np.ones(matrix_1)
	aper1 = np.zeros([n,n])
	for i in range(n):
		for j in range(n):
			r = math.sqrt((i-xcenter)**2+(j-ycenter)**2)
			if r < radius:
				aper1[i,j] = 1
	print "aperture_matrix:\n",aper1
	aperfft = np.fft.fftshift(np.fft.fft2(aper1))
	apershow(aperfft,1)
