from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
import zernike as __zernike__
import tools as __tools__
from phaseunwrap import unwrap2D as __unwrap2D__
from matplotlib import cm as __cm__



def hartmann(coefficients, r, R):
	"""
	Generate Hartmann spotdiagram
	use circle hartmann plate
	coefficients: zernike coefficients
	r: distance from the pupil of the wavefront
	R: radius of mirror under test 
	"""
	coefficients = coefficients.__coefficients__
	x_list = []
	y_list = []
	Ax_list = []
	Ay_list = []
	x = y = __np__.linspace(-R, R, 20)
	for i in x:
		for j in y:
			if i**2 + j**2 < R**2:
				x_list.append(i)
				y_list.append(j)
				W0 = __zernike__.__zernikecartesian__(coefficients,i,j)
				Wx = __zernike__.__zernikecartesian__(coefficients,1.01*i,j)
				Wy = __zernike__.__zernikecartesian__(coefficients,i,1.01*j)
				TAx = -(Wx-W0)/(0.01*i)*r
				TAy = -(Wy-W0)/(0.01*j)*r
				Ax_list.append(TAx)
				Ay_list.append(TAy)
	# fig = __plt__.figure(1)
	# __plt__.plot(x_list,y_list,'*')
	# __plt__.show()
	fig = __plt__.figure(2,figsize=(6, 6))
	ax = fig.gca()
	ax.set_axis_bgcolor('black')
	__plt__.title('Hartmann Spotdiagram',fontsize=18)
	__plt__.plot(Ax_list,Ay_list,'wo')
	__plt__.show()
	
