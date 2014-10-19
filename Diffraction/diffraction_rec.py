def diff_rec(background_size, rec_height, rec_width, row_start, col_start, clipfactor):
	import numpy as np
	import matplotlib.pyplot as plt
	import matplotlib.mlab as mlab
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
