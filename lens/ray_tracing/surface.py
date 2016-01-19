from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
import glass_funcs

# Ray Class

class Surface(object):
	'''
	Surface Class
	'''
	def __init__(self,wavelength_list,number,radius,thickness,glass,STO):
		self.wavelength_list = wavelength_list
		self.number = number
		self.radius = radius
		self.glass = glass
		self.indexlist = glass_funcs.glass2indexlist(wavelength_list,glass)
		self.thickness = thickness
		self.STO = STO
	def list(self):
		print self.radius,self.thickness,self.index


def add(self,number,radius,thickness,glass,STO):
	"""
	add a surface instance to a Lens Class
	input: a Lens Class
	"""
	print '-----------------------Add surface:--------------------------'
	print '-------------------------------------------------------------'
	print "| {0:<5s} |  {1:<10s} |  {2:<11s} |  {3:<10s} |  {4:<5s} |".\
				format('Num','Radius','Thickness','Glass','STO')
	print '-------------------------------------------------------------'
	print "| {0:<5s} |  {1:<10s} |  {2:<11s} |  {3:<10s} |  {4:<5s} |".\
				format(str(number),str(radius),str(thickness),glass,str(STO))
	print '-------------------------------------------------------------'
	New_Surface = Surface(wavelength_list = self.wavelength_list,number=number,radius=radius,thickness=thickness,glass=glass,STO=STO)
	self.surface_list.append(New_Surface)

# def update(number,key,value):
# 	if key = 'STO':

# 	else:
# 		Lens_name.surfacelist[number].key = new_value

# def delete(number):
# 	print 'delete surface x'



def list_index(self):
	print self.indexlist




