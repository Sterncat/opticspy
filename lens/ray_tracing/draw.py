from __future__ import division as __division__
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
# All lens drawing and ray drawing functions

def draw_surface(r,x0,d):
	verts_1 = []
	verts_2 = []
	codes = []
	for y in np.linspace(0,d/2,10):
		if r > 0:
			x = -np.sqrt(r**2-y**2) + r
		else:
			x = np.sqrt(r**2-y**2) + r
		verts_1.append([x+x0,y])
		verts_2.append([x+x0,-y])
		
	verts = verts_1[::-1] + verts_2[1:]
	codes.append(Path.MOVETO)
	for j in range(len(verts)-1):
		codes.append(Path.LINETO)
	return verts,codes,[verts[0],verts[-1]]

def draw_system(Lens):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	surface_list = Lens.surface_list
	m = len(surface_list)
	thinkness_list = []
	start_end_list = []
	verts_list = []
	codes_list = []
	for num in range(m):
		r = surface_list[num].radius
		glass = surface_list[num].glass
		t = surface_list[num].thickness
		thinkness_list.append(t)
		d = surface_list[num].__diameter__
		# if surface is stop, don't draw
		if surface_list[num].STO == 1:
			pass
		else:
			if num == 0:
				x0 = 0 - thinkness_list[0]
			else:
				x0 = sum(thinkness_list[0:-1]) - thinkness_list[0]
				print x0
			verts,codes,start_end = draw_surface(r,x0,d)
			start_end_list.append(start_end)
			verts_list.append(verts)
			codes_list.append(codes)

			# start drawing surface
			print 'draw surface:',num+1
			path = Path(verts, codes)
			patch = patches.PathPatch(path, facecolor='white', lw=1)
			ax.add_patch(patch)
			# start drawing edge
			if num == 0:
				pass
			elif surface_list[num-1].glass != ('air' or 'AIR'):
				print 'drawing edge:',num,'---',num+1
				verts1 = [start_end_list[num-1][0],start_end_list[num][0]]
				print verts1
				verts2 = [start_end_list[num-1][1],start_end_list[num][1]]
				print verts2
				codes = [Path.MOVETO,Path.LINETO]
				path = Path(verts1,codes)
				patch = patches.PathPatch(path, facecolor='white', lw=1)
				ax.add_patch(patch)
				path = Path(verts2,codes)
				patch = patches.PathPatch(path, facecolor='white', lw=1)	
				ax.add_patch(patch)
			else:
				pass

	ax.set_xlim(-0.5*sum(thinkness_list),1.5*sum(thinkness_list))
	ax.set_ylim(-d/2*3,d/2*3)
	plt.show()