# calculation tools
from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__

# spot diagram rms calculator

def rms(xy_list):
	x = xy_list[0]-__np__.mean(xy_list[0])
	y = xy_list[1]-__np__.mean(xy_list[1])
	rms = __np__.sqrt(sum(x**2+y**2)/len(xy_list))
	return rms