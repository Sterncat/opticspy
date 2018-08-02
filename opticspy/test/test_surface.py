import numpy as __np__
from numpy import sqrt as __sqrt__
from numpy import cos as __cos__
from numpy import sin as __sin__
import matplotlib.pyplot as __plt__
from matplotlib import cm as __cm__
from matplotlib.ticker import LinearLocator as __LinearLocator__
from matplotlib.ticker import FormatStrFormatter as __FormatStrFormatter__
#generate test surface figure
def spherical_surf(l1):
	R = 1.02
	l1 = l1  #surface matrix length
	theta = __np__.linspace(0, 2*__np__.pi, l1)
	rho = __np__.linspace(0, 1, l1)
	[u,r] = __np__.meshgrid(theta,rho)
	X = r*__cos__(u)
	Y = r*__sin__(u)
	Z = __sqrt__(R**2-r**2)-__sqrt__(R**2-1)
	v_1 = max(abs(Z.max()),abs(Z.min()))

	noise = (__np__.random.rand(len(Z),len(Z))*2-1)*0.05*v_1
	Z = Z+noise
	fig = __plt__.figure(figsize=(12, 8), dpi=80)
	ax = fig.gca(projection='3d')
	surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=__cm__.RdYlGn,\
								linewidth=0, antialiased=False, alpha = 0.6)
	v = max(abs(Z.max()),abs(Z.min()))
	ax.set_zlim(-1, 2)
	ax.zaxis.set_major_locator(__LinearLocator__(10))
	ax.zaxis.set_major_formatter(__FormatStrFormatter__('%.02f'))
	cset = ax.contourf(X, Y, Z, zdir='z', offset=-1, cmap=__cm__.RdYlGn)
	fig.colorbar(surf, shrink=1, aspect=30)
	__plt__.title('Test Surface: Spherical surface with some noise',fontsize=16)
	__plt__.show()

	#Generate test surface matrix from a detector
	x = __np__.linspace(-1, 1, l1)
	y = __np__.linspace(-1, 1, l1)
	[X,Y] = __np__.meshgrid(x,y)
	Z = __sqrt__(R**2-(X**2+Y**2))-__sqrt__(R**2-1)+noise
	for i in range(len(Z)):
		for j in range(len(Z)):
			if x[i]**2+y[j]**2>1:
				Z[i][j]=0
	return Z