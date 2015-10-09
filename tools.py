import numpy as __np__
import matplotlib.pyplot as __plt__
from matplotlib import cm as __cm__

def __apershow__(obj, extent):
	if extent != 0:
		obj = -abs(obj)
		__plt__.imshow(obj, extent = [-extent/2,extent/2,-extent/2,extent/2])
		__plt__.set_cmap('Greys')
		__plt__.show()
	else:
		obj = -abs(obj)
		__plt__.imshow(obj)
		__plt__.set_cmap('Greys')
		__plt__.show()

def makecircle(a, r, PR):
	max = a.max()
	size = __np__.sqrt(a.size)
	for i in range(int(size)):
		for j in range(int(size)):
			if __np__.sqrt(r[i]**2+r[j]**2) > PR:
				a[i,j] = max
def makecircle_boundary(a,r,PR,value):
	size = __np__.sqrt(a.size)
	for i in range(int(size)):
		for j in range(int(size)):
			if __np__.sqrt(r[i]**2+r[j]**2) > PR:
				a[i,j] = value

def circle_aperture(n):
	aperture = __np__.zeros([n,n])
	for i in range(n):
		for j in range(n):
			r = __np__.sqrt((i-n/2)**2+(j-n/2)**2)
			if r < n/2:
				aperture[i,j] = 1
	return aperture

def peak2valley(Z):
	return Z.max()-Z.min()

def rms(Z):
	rms = __np__.sqrt(__np__.mean(__np__.square(Z)))
	return rms

	
def zernikeprint(Z):
	"""
	Format output the Zernike Polynomials
	Used in opticspy.zernike.fitting
	"""
	Z.insert(0,0)
	print "                            Zernike Polynomials List                              "
	print "----------------------------------------------------------------------------------"
	print "|   Z1  |   Z2  |   Z3  |   Z4  |   Z5  |   Z6  |   Z7  |   Z8  |   Z9  |  Z10  |"
	print "----------------------------------------------------------------------------------"
	print "|{0:^7.3f}|{1:^7.3f}|{2:^7.3f}|{3:^7.3f}|{4:^7.3f}|{5:^7.3f}|{6:^7.3f}|{7:^7.3f}|{8:^7.3f}|{9:^7.3f}|".format\
			(Z[1],Z[2],Z[3],Z[4],Z[5],Z[6],Z[7],Z[8],Z[9],Z[10])
	print "----------------------------------------------------------------------------------"
	print "|  Z11  |  Z12  |  Z13  |  Z14  |  Z15  |  Z16  |  Z17  |  Z18  |  Z19  |  Z20  |"
	print "----------------------------------------------------------------------------------"
	print "|{0:^7.3f}|{1:^7.3f}|{2:^7.3f}|{3:^7.3f}|{4:^7.3f}|{5:^7.3f}|{6:^7.3f}|{7:^7.3f}|{8:^7.3f}|{9:^7.3f}|".format\
			(Z[11],Z[12],Z[13],Z[14],Z[15],Z[16],Z[17],Z[18],Z[19],Z[20])
	print "----------------------------------------------------------------------------------"
	print "|  Z21  |  Z22  |  Z23  |  Z24  |  Z25  |  Z26  |  Z27  |  Z28  |  Z29  |  Z30  |"
	print "----------------------------------------------------------------------------------"
	print "|{0:^7.3f}|{1:^7.3f}|{2:^7.3f}|{3:^7.3f}|{4:^7.3f}|{5:^7.3f}|{6:^7.3f}|{7:^7.3f}|{8:^7.3f}|{9:^7.3f}|".format\
			(Z[21],Z[22],Z[23],Z[24],Z[25],Z[26],Z[27],Z[28],Z[29],Z[30])
	print "----------------------------------------------------------------------------------"
	print "|  Z31  |  Z32  |  Z33  |  Z34  |  Z35  |  Z36  |  Z37  |                       |"
	print "----------------------------------------------------------------------------------"
	print "|{0:^7.3f}|{1:^7.3f}|{2:^7.3f}|{3:^7.3f}|{4:^7.3f}|{5:^7.3f}|{6:^7.3f}|                       |".format\
			(Z[31],Z[32],Z[33],Z[34],Z[35],Z[36],Z[37])
	print "----------------------------------------------------------------------------------"


def phase_shift_figure(I,PR,type):
	"""
	Draw PSI Interferograms, several types.
	"""
	if type == "4-step":
		f, axarr = __plt__.subplots(2, 2, figsize=(9, 9), dpi=80)
		axarr[0, 0].imshow(-I[0], extent=[-PR,PR,-PR,PR],cmap=__cm__.Greys)
		axarr[0, 0].set_title(r'$Phase\ shift: 0$',fontsize=16)
		axarr[0, 1].imshow(-I[1], extent=[-PR,PR,-PR,PR],cmap=__cm__.Greys)
		axarr[0, 1].set_title(r'$Phase\ shift: 1/2\pi$',fontsize=16)
		axarr[1, 0].imshow(-I[2], extent=[-PR,PR,-PR,PR],cmap=__cm__.Greys)
		axarr[1, 0].set_title(r'$Phase\ shift: \pi$',fontsize=16)
		axarr[1, 1].imshow(-I[3], extent=[-PR,PR,-PR,PR],cmap=__cm__.Greys)
		axarr[1, 1].set_title(r'$Phase\ shift: 3/2\pi$',fontsize=16)
		__plt__.suptitle('4-step Phase Shift Interferograms',fontsize=16)
		__plt__.show()
	else:
		print "No this type of figure"












