# calculation tools
from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__

# spot diagram rms calculator

def rms(ray_list):
	x2 = []
	y2 = []
	for ray in ray_list:
		x2.append(ray.Pos[0])
		y2.append(ray.Pos[1])
	x2 = __np__.asarray(x2)
	y2 = __np__.asarray(y2)
	rms = __np__.sqrt(sum(x2**2+y2**2)/len(ray_list))
	return rms 


	