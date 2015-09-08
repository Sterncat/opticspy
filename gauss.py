import numpy as __np__
import matplotlib.pyplot as __plt__
from mpl_toolkits.mplot3d import Axes3D as __Axes3D__
from matplotlib import cm as __cm__
def gausscal(z = 1,w0 = 0.1 ,lambda1 = 0.633):
	# Axial Distance, z (mm)
	# Beam Waist, w0 (mm)
	# Wavelength, lambda (um)
	theta = lambda1/__np__.pi/w0 # Half Angle Divergence, theta (mrad)
	z0 = w0/theta*1000 # Rayleigh Range, z0 (mm)
	wz = w0*__np__.sqrt(1+(z/z0)**2) # Half Beam Diameter, w(z) (mm)
	Rz = z + z0**2/z# Radius of Curvature, R(z) (mm)
	wR =  __np__.sqrt(2)*w0# Rayleigh Half Diameter, wz(b/2)
	list1 = [z,w0,lambda1,wz,Rz,z0,wR,theta]
	list3 = []
	for i in list1:
		if i>100000:
			list3.append("Inf")
		else:
			list3.append(str(round(i,3)))
	list2 = [
	"Axial Distance, z (mm)",	
	"Beam Waist, w0 (mm)",	
	"Wavelength, lambda (um)",	
	"Half Beam Diameter, w(z) (mm)",
	"Radius of Curvature, R(z) (mm)",
	"Rayleigh Range, z0 (mm)",
	"Rayleigh Half Diameter, w0 (mm)",
	"Half Angle Divergence, theta (mrad)"]	
	print"               Gaussian Beams Calculator"
	print"--------------------------------------------------------"
	for i in range(8):
		print "| {0:>35s} |  {1:<6s}".format(list2[i],list3[i])
	print"--------------------------------------------------------"
	return list1

def gaussbeam():
	x1 = __np__.linspace(-4,4,100)
	y1 = __np__.linspace(-4,4,100)
	[x,y] = __np__.meshgrid(x1,y1)
	w = 1
	P = 5
	I = 2*P/__np__.pi/w**2*__np__.exp(-2*(x**2+y**2)/w**2)
	fig = __plt__.figure(figsize=(12, 8), dpi=80)
	ax = fig.gca(projection='3d')
	surf = ax.plot_surface(x, y, I, rstride=1, cstride=1, cmap=__cm__.RdYlGn,
		        linewidth=0, antialiased=False, alpha = 0.6)
	__plt__.show()

	