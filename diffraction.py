from core import diff_core as DC
#__all__ = ['apershow','rec','circle']
import show

#def apershow(aper_fft, clipfactor):
#
#	aper_fft = abs(aper_fft)
#	gamax=aper_fft.max()
#	gamin=aper_fft.min()
#	print gamax
#	print gamin
##	scale=0.25*255*clipfactor/gamax
##	ga=min(scale*aper_fft,255);
#	DC.plt.imshow(aper_fft,vmax=gamax, vmin=gamin)
#	DC.plt.show()
	
def rec(background_size, rec_height, rec_width, row_start, col_start, clipfactor):
	"""
	Compute the rectangle aperture's diffraction pattern.
	
	Example
	-----------
	diffraction.rect(200,20,20,80,80,1)
	
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
	aper = DC.np.ones(matrix_1)
	aper1 = DC.np.zeros([n,n])
	aper1[(rowstart-1):(rowstart-1+height),(colstart-1):(colstart-1+width)] = aper
#	print "aperture_matrix:",aper1
	aperfft = DC.np.fft.fftshift(DC.np.fft.fft2(aper1))
	show.apershow(aperfft,1)
	
	
	

def circle(background_size, radius, clipfactor):
	"""
	Compute the cirlce aperture's diffraction pattern.
	
	Example
	-----------
	diffraction.circle(200,[50,50],20,1)
	
 	Parameters
	-----------
	background_size: int
				Square background
	center: int
				aperture center
	radius: int
				aperture radius
				
	returns
	-----------
	out: aperture's matrix and figure of diffraction pattern
	"""

	n = background_size
	radius = radius
	clipfactor = clipfactor
	aper1 = DC.np.zeros([n,n])
	for i in range(n):
		for j in range(n):
			r = DC.sqrt((i-background_size/2)**2+(j-background_size/2)**2)
			if r < radius:
				aper1[i,j] = 1
#	print "aperture_matrix:",aper1
	aperfft = DC.np.fft.fftshift(DC.np.fft.fft2(aper1))
	show.apershow(aperfft,1)
