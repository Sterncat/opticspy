from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__

# Function: trace rays
# input a list of ray 
# output [ray position and direction] on next surface

def trace(ray_list,surface1,surface2):
	ray_num = len(ray_list)
	Pos_new_list = []
	KLM_new_list = []
	for ray in ray_list:
		Pos = ray.Pos
		KLM = ray.KLM
		c1 = surface1.curvature
		c2 = surface2.curvature
		n1 = surface1.index
		n2 = surface2.index
		tn1 = surface1.thickness
		tn2 = surface2.thickness
		xyz = __np__.asarray([Pos[0],Pos[1],Pos[2]-tn1])
		delta,cosI = pos(xyz,KLM,c2)
		Pos_new = xyz + delta*KLM
		Pos_new_list.append(Pos_new)
		# calculate new ray direction
		# if curvature == 0, it is a stop, object or image plane
		# don't need to calculate the new ray direction
		if c2 == 0:
			KLM_new = KLM
		else:
			sigma = __np__.sqrt(n2**2-n1**2*(1-cosI**2)) - n1*cosI
			Kp = (n1*KLM[0] - c2*sigma*Pos_new[0])/n2
			Lp = (n1*KLM[1] - c2*sigma*Pos_new[1])/n2
			Mp = (n1*KLM[2] - c2*sigma*Pos_new[2] + sigma)/n2
			KLM_new = __np__.asarray([Kp,Lp,Mp])
		KLM_new_list.append(KLM_new)

	return Pos_new_list, KLM_new_list


def pos(Pos,KLM,curvature):
	c = curvature
	x0 = Pos[0]
	y0 = Pos[1]
	z0 = Pos[2]
	K = KLM[0]
	L = KLM[1]
	M = KLM[2]
	E = c*(x0**2+y0**2+z0**2)-2*z0
	G = M - c*(K*x0+L*y0+M*z0)
	delta = E/(G+__np__.sqrt(G**2-c*E))
	cosI = __np__.sqrt(G**2-c*E)
	return delta, cosI	