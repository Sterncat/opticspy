from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__

# Ray Class

def spotdiagram(Lens):
	'''
	Show spotdiagram of image plane for different field
	input: Lens Class
	'''
	fig = __plt__.figure()
	for ray_list in Lens.image_plane_ray_list: 
		x = []
		y = []
		z = []
		for ray in ray_list:
			x.append(ray.Pos[0])
			y.append(ray.Pos[1])
			z.append(ray.Pos[2])
		__plt__.plot(x,y,'b*')
	__plt__.show()
	return 0
