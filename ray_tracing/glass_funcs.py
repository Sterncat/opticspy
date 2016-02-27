from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
import os
from glass_function.refractiveIndex import *


# glass related functions
# use polyanskiy's refractiveindex database(http://refractiveindex.info/) 
# polyanskiy's github: https://github.com/polyanskiy
# https://github.com/polyanskiy/refractiveindex.info-database
# Also use Pavel Dmitriev's script for return refractiveindex from database
# https://github.com/kitchenknif/PyTMM


def glass2indexlist(wavelength_list,glassname):
	
	lens_index_list = []
	wavelength_num = len(wavelength_list)
	if glassname == 'air' or glassname == 'AIR':
		lens_index_list = [1]*wavelength_num
		return lens_index_list
	else:
		n = glassname.find('_')
		glass_catalog_name = glassname[n+1:]
		glass_name = glassname[:n]
		catalog = RefractiveIndex()
		for w in wavelength_list:
			mat = catalog.getMaterial('glass', glass_catalog_name, glass_name)
			n = mat.getRefractiveIndex(w)
			lens_index_list.append(round(n,6))
	return lens_index_list

	
def output(wavelength_list,lens_index_list):
	print 'Lens wavelength vs index'
	print 'wavelength-----index---'
	for wavelength,index in zip(wavelength_list,lens_index_list):
		print "| {0:<8s} |  {1:<8s} |".\
		format(str(wavelength),str(index))
	print '-----------------------'
	return 0

#=============================================================
# Old glass check functions
#
# def glass2indexlist(wavelength_list,glassname):
# 	"""
# 	convert glass to index list related to wavelength
# 	glassname: str
# 	"""
# 	#print 'glass',glassname
# 	wavelength_num = len(wavelength_list)
# 	if glassname == 'air' or glassname == 'AIR':
# 		lens_index_list = [1]*wavelength_num
# 		#output(wavelength_list,lens_index_list)
# 		return lens_index_list
# 	else:
# 		n = glassname.find('_')
# 		glass_catalog_name = glassname[n+1:]
# 		glass_name = glassname[:n]
# 		dir = 'opticspy/ray_tracing/glass/' + glass_catalog_name+'/'+glassname
# 		e = os.path.exists(dir)

# 		if e == False:
# 			print 'No This Kind Of Glass'
# 			return None
# 		else:
# 			wave_list = []
# 			index_list = []
# 			lens_index_list = []
# 			file = open(dir)
# 			while 1:
# 				line = file.readline()
# 				if not line:
# 					break
# 				a = line.split()
# 				wave_list.append(float(a[0]))
# 				index_list.append(float(a[1]))
# 			file.close()
# 			for wavelength in wavelength_list:
# 				index = find_closest_wavelength(wavelength,wave_list,index_list)
# 				lens_index_list.append(index)
# 			#output(wavelength_list,lens_index_list)
# 			return lens_index_list

# def find_closest_wavelength(wavelength,wave_list,index_list):
# 	n = 0
# 	for i in wave_list:
# 		if wavelength == i:
# 			return index_list[n]
# 		elif wavelength < i:
# 			return (index_list[n]+index_list[n])/2
# 		else:
# 			n = n + 1

