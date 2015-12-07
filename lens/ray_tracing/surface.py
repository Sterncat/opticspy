from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__

# Ray Class

class Surface(object):
	def __init__(self,curvature = 1/1000000,thickness = 0, index = 0.000001):
		self.curvature = curvature
		self.index = index
		self.thickness = thickness
	def list(self):
		print self.curvature,self.thickness,self.index


	