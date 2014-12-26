from core import diff_core as DC
#__all__ = ['apershow','rec','circle']

def apershow(obj, clipfactor):

	obj = abs(obj)
	gamax=obj.max()
	gamin=obj.min()
	print gamax
	print gamin
#	scale=0.25*255*clipfactor/gamax
#	ga=min(scale*aper_fft,255);
	DC.plt.imshow(obj,vmax=gamax, vmin=gamin)
	DC.plt.show()
	

