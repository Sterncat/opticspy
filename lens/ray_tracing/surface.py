from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__

# Ray Class

class Surface(object):
	def __init__(self,number,radius,thickness,index,STO):
		self.number = number
		self.radius = radius
		self.index = index
		self.thickness = thickness
		self.STO = STO
	def list(self):
		print self.radius,self.thickness,self.index


def add(self,number,radius,thickness,index,STO):
	"""
	add a surface instance to a Lens Class
	input: a Lens Class
	"""
	print number,radius,thickness,index,STO
	New_Surface = Surface(number=number,radius=radius,thickness=thickness,index=index,STO=STO)
	self.surface_list.append(New_Surface)
	print self.surface_list
# def update(number,key,value):
# 	if key = 'STO':

# 	else:
# 		Lens_name.surfacelist[number].key = new_value

# def delete(number):
# 	print 'delete surface x'























