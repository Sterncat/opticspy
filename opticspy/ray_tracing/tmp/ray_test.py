from __future__ import division as __division__
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cal_tools

#1st surface object
l1 = np.linspace(-5,5,30)
Pn1 = [];
for i in l1:
	for j in l1:
		if i**2+j**2<25:
			Pn1.append([i,j,0])
#plt.plot(p0,p1,'b*')
#plt.show()
KLM = []
for i in Pn1:
	KLM.append([0,0,1])
#second surface
tn1 = 10
c = 1/20
def pos(xyz,c,KLM):
	x0 = xyz[0]
	y0 = xyz[1]
	z0 = xyz[2]
	K = KLM[0]
	L = KLM[1]
	M = KLM[2]
	E = c*(x0**2+y0**2+z0**2)-2*z0
	G = M - c*(K*x0+L*y0+M*z0)
	delta = E/(G+np.sqrt(G**2-c*E))
	cosI = np.sqrt(G**2-c*E)
	return delta, cosI

xyz_list = []
cosI = []
x = []
y = []
z = []
for p,q in zip(Pn1,KLM):
	xyz = np.asarray([p[0],p[1],p[2]-tn1])
	delta,cosI_tmp = pos(xyz,c,q)
	cosI.append(cosI_tmp)
	q = np.asarray(q)
	xyz_tmp = xyz + delta*q
	xyz_list.append(xyz_tmp)
	x.append(xyz_tmp[0])
	y.append(xyz_tmp[1])
	z.append(xyz_tmp[2])
	
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, z, y)
ax.set_xlim3d(-6, 6)
ax.set_ylim3d(-6, 6)
ax.set_zlim3d(-6, 6)
plt.show()

npp = 2
n = 1
KLM1 = []

for i,j,k in zip(xyz_list,KLM,cosI):
	sigma = np.sqrt(npp**2-n**2*(1-k**2)) - n*k
	Kp = (n*j[0] - c*sigma*i[0])/npp
	Lp = (n*j[1] - c*sigma*i[1])/npp
	Mp = (n*j[2] - c*sigma*i[2] + sigma)/npp
	KLM1.append([Kp,Lp,Mp]) 

#print KLM1	



tn2 = 40
c2 = 1/10000
xyz_list2 = []
cosI2 = []
x2 = []
y2 = []
z2 = []

for p,q in zip(xyz_list,KLM1):
	xyz = np.asarray([p[0],p[1],p[2]-tn2])
	delta,cosI_tmp = pos(xyz,c2,q)
	cosI2.append(cosI_tmp)
	q = np.asarray(q)
	xyz_tmp = xyz + delta*q
	xyz_list2.append(xyz_tmp)
	x2.append(xyz_tmp[0])
	y2.append(xyz_tmp[1])
	z2.append(xyz_tmp[2])
	
#print xyz_list2
fig = plt.figure()
plt.plot(x2,y2,'b*')
plt.show()

rms = cal_tools.rms()
print 'rms = ',rms


