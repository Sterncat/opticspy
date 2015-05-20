import numpy as __np__
def makecircle(a, r, PR):
	max = a.max()
	size = __np__.sqrt(a.size)
	for i in range(int(size)):
		for j in range(int(size)):
			if __np__.sqrt(r[i]**2+r[j]**2) > PR:
				a[i,j] = max

def peak2valley(Z):
	return Z.max()-Z.min()

def rms(Z):
	rms = __np__.sqrt(__np__.mean(__np__.square(Z)))
	return rms
