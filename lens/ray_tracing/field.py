from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__

# Ray Class

class Ray(object):
	def __init__(self,Pos,KLM):
		self.Pos = __np__.asarray(Pos)
		self.KLM = __np__.asarray(KLM)
	def list(self):
		print "Ray Position :",self.Pos
		print "Ray Direction:",self.KLM

class Field(object):
	def __init__(self,Raylist):
		self.ray_list = []
		for i in Raylist:
			self.ray_list.append(Ray(i[0],i[1]))

def add_field_YAN(Lens,angle):
	'''
	Add field by object angle
	self.EPD.diameter: Entrance pupil diameter
	angle: Object angle 
	'''
	print 'add field'
	diameter = Lens.EPD_diameter
	l1 = __np__.linspace(-diameter,diameter,15)
	Pos = []
	for i in l1:
		for j in l1:
			if i**2+j**2<diameter**2:
				Pos.append([i,j,0])
	KLM = []
	l = __np__.sin(angle/180*__np__.pi)
	m = __np__.cos(angle/180*__np__.pi)
	for i in Pos:
		KLM.append([0,l,m])

	raylist = []

	for pos,klm in zip(Pos,KLM):
		raylist.append([pos,klm])

	New_Field = Field(raylist)
	Lens.field_list.append(New_Field)








	