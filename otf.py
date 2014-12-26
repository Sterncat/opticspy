from core import diff_core as DC
import show

#test

def circle(background_size, radius):
	n = background_size
	radius = radius
	aper1 = DC.np.zeros([n,n])
	for i in range(n):
		for j in range(n):
			r = DC.sqrt((i-background_size/2)**2+(j-background_size/2)**2)
			if r < radius:
				aper1[i,j] = 1
	aperfft = DC.np.fft.fftshift(DC.np.fft.fft2(aper1))**2
	aper_OTF = DC.np.fft.fftshift(DC.np.fft.fft2(aperfft))
	show.apershow(aper_OTF,1)
