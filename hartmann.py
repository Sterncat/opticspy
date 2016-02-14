from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
import zernike as __zernike__
import tools as __tools__
from phaseunwrap import unwrap2D as __unwrap2D__

from mplot3d import Axes3D as __Axes3D__
from matplotlib import cm as __cm__


def hartmann(coefficients, r, R):
	"""
	Generate Hartmann spotdiagram
	use circle hartmann plate
	coefficients: zernike coefficients
	r: distance from the pupil of the wavefront to detect plate
	R: radius of mirror under test
	"""
	coefficients = coefficients.__coefficients__
	x_list = []
	y_list = []
	Ax_list = []
	Ay_list = []
	s = 40
	x = y = __np__.linspace(-R, R, s)
	M = []
	for i in x:
		tmp = []
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
				tmp.append([1,[i,j],[TAx,TAy]])
			else:
				tmp.append([0,[i,j],[0,0]])
		M.append(tmp)
	fig = __plt__.figure(1,figsize=(6, 6))
	ax = fig.gca()
	ax.set_axis_bgcolor('black')
	__plt__.title('Hartmann Spotdiagram',fontsize=18)
	__plt__.plot(Ax_list,Ay_list,'wo')
	__plt__.show()

	return M,r


def hartmann_rebuild(M,r):
	s = len(M)
	w = __np__.zeros([s,s])
	d = 2
	for n in range(s):
		label = 0
		for m in range(s):
			if M[n][m][0] == 0:
				pass
			elif (M[n][m][0] != 0 and label == 0):
				w[n,m] = 0
				label = 1
			elif (M[n][m][0] != 0 and label == 1):
				w[n,m] = w[n][m-1] + d/2/r*(M[n][m-1][2][0] + M[n][m][2][0])
			else:
				print 'wrong'
	fig = __plt__.figure(2,figsize=(6, 6))
	__plt__.imshow(w)
	__plt__.show()
	# x = __np__.linspace(-1,1,s)
	# [X,Y] = __np__.meshgrid(x,x)
	# fig = __plt__.figure(figsize=(8, 8), dpi=80)
	# ax = fig.gca(projection='3d')
	# surf = ax.plot_surface(w, rstride=1, cstride=1, cmap=__cm__.RdYlGn,
	#         linewidth=0, antialiased=False, alpha = 0.6)
	# __plt__.show()

	return w


#Depth first search algorithm, use to find wavefrontase map(where)
def DFS(M,wavefront1,m,n,s):
	stack = []
	stack.append([m,n])
	M[m,n] = 2
	wavefront = __np__.zeros([s,s])

	while (len(stack) != 0):
		[m,n] = stack[-1]
		if m + 1 < s and n < s and M[m+1,n] == 1 and M[m+1,n] != 0 and M[m+1,n] != 2:
			m = m + 1
			M[m,n] = 2
			stack.append([m,n])
			
			wavefront[m,n] = wavefront[m-1,n] + v(wavefront1[m,n] - wavefront1[m-1,n])
			
		elif m - 1 > 0 and n < s and M[m-1,n] == 1 and M[m-1,n] != 0 and M[m-1,n] != 2:
			m = m - 1
			M[m,n] = 2
			stack.append([m,n])
			
			wavefront[m,n] = wavefront[m+1,n] + v(wavefront1[m,n] - wavefront1[m+1,n])
			
		elif m < s and n + 1 < s and M[m,n+1] == 1 and M[m,n+1] != 0 and M[m,n+1] != 2: 
			n = n + 1
			M[m,n] = 2
			stack.append([m,n])
			
			wavefront[m,n] = wavefront[m,n-1] + v(wavefront1[m,n] - wavefront1[m,n-1])
			
		elif m < s and n - 1 > 0 and M[m,n-1] == 1 and M[m,n-1] != 0 and M[m,n-1] != 2: 
			n = n - 1
			M[m,n] = 2
			stack.append([m,n])
			
			wavefront[m,n] = wavefront[m,n+1] + v(wavefront1[m,n] - wavefront1[m,n+1])
			
		else:
			stack.pop()
	return wavefront


	
