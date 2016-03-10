import numpy as __np__
import matplotlib.pyplot as __plt__
from matplotlib import cm as __cm__
from mplot3d import Axes3D as __Axes3D__
def gausscal(z = 1,w0 = 0.1 ,lambda1 = 0.633):
	"""
	Gauss beam Calculator
	==========================================
	input
	------------------------------------------
	# z: Axial Distance(mm)
	# w0: Beam Waist(mm)
	# lambda1: Wavelength(um)
	"""
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
	"Rayleigh Range, z0 (mm)",# [1]
	"Rayleigh Half Diameter, w0 (mm)",
	"Half Angle Divergence, theta (mrad)"]	
	print"               Gaussian Beams Calculator"
	print"--------------------------------------------------------"
	for i in range(8):
		print "| {0:>35s} |  {1:<6s} ".format(list2[i],list3[i])
	print"--------------------------------------------------------"
	return list1
	#[1] In optics and especially laser science, the Rayleigh length or Rayleigh 
	# range is the distance along the propagation direction of a beam from the 
	# waist to the place where the area of the cross section is doubled.
def gaussbeam(w0 = 1,P = 5,z0 = 5, z = 10):
	"""
	Generate a gaussbeam
	========================================
	input
	----------------------------------------
	w0 Beam Waist
	P total power
    z0 Rayleigh Range
    z Axial Distance

    output
    ----------------------------------------
    gaussbeam matrix

    """
	x1 = __np__.linspace(-4,4,100)
	y1 = __np__.linspace(-4,4,100)
	[x,y] = __np__.meshgrid(x1,y1)
	wz = w0*__np__.sqrt(1+(z/z0)**2)
	I = 2*P/__np__.pi/(wz**2)*__np__.exp(-2*(x**2+y**2)/(wz**2))
	fig = __plt__.figure(figsize=(12, 8), dpi=80)
	ax = fig.gca(projection='3d')
	surf = ax.plot_surface(x, y, I, rstride=1, cstride=1, cmap=__cm__.RdYlGn,
		        linewidth=0, antialiased=False, alpha = 0.6)
	__plt__.title('Gaussian Beam Intensity Distribution',fontsize=18)
	label_1 = "Beam Waist = " + str(w0) + "\n" +\
			  "Total Power = " + str(P) + "\n" +\
			  "Rayleigh Range = " + str(z0) + "\n" +\
			  "Axial Distance = " + str(z)	
	ax.text2D(0.02, 0.01, label_1, transform=ax.transAxes,fontsize=14)
	__plt__.show()
	return I
