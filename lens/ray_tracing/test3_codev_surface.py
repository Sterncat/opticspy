from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
from mpl_toolkits.mplot3d import Axes3D
import codev,surface
a = codev.readseq("triplet.seq")
Surface_list = []
m = 0

for i in a['Surface']:
	print i
	if i[0] == 'SO':
		pass
	elif i[0] == 'SI':
		pass
	else:
		m = m + 1
		number = m
		radius = i[1]
		thickness = i[2]
		if i[3] == '':
			index = 0
		else:
			index = 1.5
		STO = False
		if len(i) == 5:
			STO = True
		s = surface.Surface(number = number,
								radius = radius,
								thickness = i[2], 
								index = index,
								STO = STO)
		Surface_list.append(s)

for j in range(len(Surface_list)):
	print Surface_list[j].number,' ',Surface_list[j].radius,' ',Surface_list[j].thickness,Surface_list[j].STO
	
	
	
	
	
	
	
	
	
	
	
	
	
	