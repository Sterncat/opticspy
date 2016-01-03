# calculation tools
from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__

# spot diagram rms calculator

def rms(position_list):
	x2 = []
	y2 = []
	for i in position_list:
		x2.append(i[0])
		y2.append(i[1])
	x2 = __np__.asarray(x2)
	y2 = __np__.asarray(y2)
	rms = __np__.sqrt(sum(x2**2+y2**2)/len(position_list))
	return rms 


	