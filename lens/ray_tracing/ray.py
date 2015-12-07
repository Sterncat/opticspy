from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__

# Ray Class

class Ray(object):
	Pos = []
	KLM = []
	def __init__(self,Pos = Pos, KLM = KLM):
		self.Pos = __np__.asarray(Pos)
		self.KLM = __np__.asarray(KLM)
	def list(self):
		print "Ray Position :",self.Pos
		print "Ray Direction:",self.KLM


	