import numpy as __np__
from numpy import sqrt as __sqrt__
from numpy import cos as __cos__
from numpy import sin as __sin__
import matplotlib.pyplot as __plt__
from matplotlib import cm as __cm__
from matplotlib.ticker import LinearLocator as __LinearLocator__
from matplotlib.ticker import FormatStrFormatter as __FormatStrFormatter__
#generate test surface figure
def makecircle(a, r, PR):
	max = a.max()
	size = __np__.sqrt(a.size)
	for i in range(int(size)):
		for j in range(int(size)):
			if __np__.sqrt(r[i]**2+r[j]**2) > PR:
				a[i,j] = max

def testsurface2():

	lambda_1 = 632*(10**-9)
	PR = 1
	r = __np__.linspace(-PR, PR, 200)
	x, y = __np__.meshgrid(r,r) 
	r1 = __np__.sqrt(x**2 + y**2)
	Z4 = 1
	Z5 = 0.6
	ZX  =  Z4  * __np__.sqrt(3)*(2*r1**2-1) + Z5*2*__np__.sqrt(6)*x*y
	OPD = 	ZX*2/PR
	ph = 2 * __np__.pi * OPD
	Ia = 1
	Ib = 1
	Ixy = Ia + Ib + 2 * __np__.sqrt(Ia*Ib) * __np__.cos(ph)
	makecircle(Ixy, r, PR)
	fig = __plt__.figure(figsize=(9, 6), dpi=80)
	__plt__.imshow(-Ixy, extent=[-PR,PR,-PR,PR])
	__plt__.set_cmap('Greys')
	__plt__.show()

	I1 = Ia + Ib + 2 * __np__.sqrt(Ia*Ib) * __np__.cos(ph)
	I2 = Ia + Ib + 2 * __np__.sqrt(Ia*Ib) * __np__.cos(ph+45.0/180*__np__.pi)
	I3 = Ia + Ib + 2 * __np__.sqrt(Ia*Ib) * __np__.cos(ph+90.0/180*__np__.pi)
	I4 = Ia + Ib + 2 * __np__.sqrt(Ia*Ib) * __np__.cos(ph+135.0/180*__np__.pi)

	Ilist = [I1,I2,I3,I4]

	for i in range(4):
		makecircle(Ilist[i], r, PR)
		fig = __plt__.figure(figsize=(9, 6), dpi=80)
		__plt__.imshow(-Ilist[i], extent=[-PR,PR,-PR,PR])
		__plt__.set_cmap('Greys')
		__plt__.show()

	ph1 = __np__.arctan((I4-I2)/(I1-I3))

	Ixy1 = Ia + Ib + 2 * __np__.sqrt(Ia*Ib) * __np__.cos(ph1)
	fig = __plt__.figure(figsize=(9, 6), dpi=80)
	__plt__.imshow(-Ixy, extent=[-PR,PR,-PR,PR])
	__plt__.set_cmap('Greys')
	__plt__.show()

	OPD = ph*PR/2
	Z = OPD
	fig = __plt__.figure(figsize=(6, 6), dpi=80)
	#ax = fig.gca(projection='3d')
	#surf = ax.plot_surface(x, y, Z, rstride=1, cstride=1, cmap=__cm__.RdYlGn,linewidth=0, antialiased=False, alpha = 0.6)
	im = __plt__.pcolormesh(x, y, Z, cmap=__cm__.RdYlGn)
	__plt__.colorbar()
	__plt__.show()

	for i in range(len(Z)):
		for j in range(len(Z)):
			if r[i]**2+r[j]**2>1:
				Z[i][j]=0
	fig = __plt__.figure(figsize=(6, 6), dpi=80)
	im = __plt__.pcolormesh(x, y, Z, cmap=__cm__.RdYlGn)
	__plt__.colorbar()
	__plt__.show()

	return Z