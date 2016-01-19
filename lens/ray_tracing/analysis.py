from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__

# Ray Class

def spotdiagram(Lens):
	'''
	Show spotdiagram of image plane for different field
	input: Lens Class
	'''

	sign_list = ['b*','go','rs','cD','m+','yx','k1','ws']


	fig = __plt__.figure(figsize=(5, 9), dpi=80)
	field_num = len(Lens.field_list)
	wave_num = len(Lens.wavelength_list)
	n = field_num
	
	for field_list in Lens.image_plane_ray_list:
		m = -1
		__plt__.subplot(field_num, 1, n)
		for ray_list in field_list:
			m = m + 1
			x = []
			y = []
			z = []
			for ray in ray_list:
				x.append(ray.Pos[0])
				y.append(ray.Pos[1])
				z.append(ray.Pos[2])
			__plt__.plot(x,y,sign_list[m])
			__plt__.axis('equal')
		n = n - 1
	__plt__.show()
	return 0
