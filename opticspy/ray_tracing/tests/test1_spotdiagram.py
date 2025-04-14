from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
from mpl_toolkits.mplot3d import Axes3D
import field
import traceray
import surface
import cal_tools
# test ray.py and traceray.py
		

# define rays
l1 = __np__.linspace(-5,5,10)
Pos1 = []
for i in l1:
	for j in l1:
		if i**2+j**2<25:
			Pos1.append([i,j,0])
KLM = []
for i in Pos1:
	KLM.append([0,0,1])

# define surface
surface1 = surface.Surface(number=1,radius = 10000000, thickness = 10, index = 1,STO=0) #object
surface2 = surface.Surface(number=2,radius = 20, thickness = 40, index = 2,STO=0)  #surface i
surface3 = surface.Surface(number=3,radius = 10000000, thickness = 0, index = 1,STO=0) #image

raylist1 = []
raylist2 = []

for pos,klm in zip(Pos1,KLM):
		ray1 = field.Field(Pos = pos, KLM = klm) 
		raylist1.append(ray1)
		
Pos_new_list,KLM_new_list = traceray.trace(raylist1,surface1,surface2)


x = []
y = []
z = []
for i in Pos_new_list:
	x.append(i[0])
	y.append(i[1])
	z.append(i[2])
	
fig = __plt__.figure()
ax = Axes3D(fig)
ax.scatter(x, z, y)
ax.set_xlim3d(-6, 6)
ax.set_ylim3d(-6, 6)
ax.set_zlim3d(-6, 6)
__plt__.show()


for pos,klm in zip(Pos_new_list,KLM_new_list):
		ray2 = field.Field(Pos = pos, KLM = klm) 
		raylist2.append(ray2)


Pos_new_list1,KLM_new_list1 = traceray.trace(raylist2, surface2, surface3)

x2 = []
y2 = []
z2 = []
for i in Pos_new_list1:
	x2.append(i[0])
	y2.append(i[1])
	z2.append(i[2])

fig = __plt__.figure()
__plt__.plot(x2,y2,'b*')
__plt__.show()



rms = cal_tools.rms(Pos_new_list1)
print rms



	