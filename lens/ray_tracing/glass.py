from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
import os

# glass related functions

def glass2indexlist(self,glassname):
	"""
	convert glass to index list related to wavelength
	glassname: str
	"""
	print 'glass',glassname
	wavelength_num = len(self.wavelength_list)
	if glassname == 'air' or glassname == 'AIR':
		print 'AIR'
		return [1]*wavelength_num
	else:
		print '----------------------------'
		n = glassname.find('_')
		glass_catalog_name = glassname[n+1:]
		glass_name = glassname[:n]
		print glass_catalog_name
		dir = 'glass/' + glass_catalog_name+'/'+glassname
		print dir
		e = os.path.exists(dir)
		if e == False:
			print 'No This Kind Of Glass'
		else:
			wave_list = []
			index_list = []
			lens_index_list = []
			file = open(dir)
			while 1:
				line = file.readline()
				if not line:
					break
				a = line.split()
				print a
				wave_list.append(float(a[0]))
				index_list.append(float(a[1]))
			file.close()
			print wave_list
			print index_list
			for wavelength in self.wavelength_list:
				index = find_closest_wavelength(wavelength,wave_list,index_list)
				lens_index_list.append(index)
			print 'Lens wavelength vs index'
			print 'wavelength-----index---'
			for wavelength,index in zip(self.wavelength_list,lens_index_list):
				print "| {0:<8s} |  {1:<8s} |".\
				format(str(wavelength),str(index))
			print '-----------------------'
			return lens_index_list

def find_closest_wavelength(wavelength,wave_list,index_list):
	n = 0
	print wavelength
	for i in wave_list:
		if wavelength == i:
			return index_list[n]
		elif wavelength < i:
			return (index_list[n]+index_list[n])/2
		else:
			n = n + 1










	