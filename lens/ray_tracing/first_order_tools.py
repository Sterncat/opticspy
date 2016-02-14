# first order tools, find EPD, calculate system power, etc
from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__

def T(t,n):
	'''
	T matrix generate
	'''
	return __np__.array([[1,t/n],[0,1]])

def R(c,n_left,n_right):
	'''
	R matrix generate
	'''
	return __np__.array([[1,0],[-c*(n_right-n_left),1]])

def ABCD(matrix_list):
	'''
	ABCD matrix calculator
	input: a matrix list
	output: ABCD matrix
	'''
	M = matrix_list.pop()
	while matrix_list:
		M = __np__.dot(M,matrix_list.pop())
	return M[0,0],M[0,1],M[1,0],M[1,1]




def list(Lens):
	'''
	List first order information of a lens system
	input: Lens Class
	output: print information
			refresh Lens first order information
	'''

	return 0


# input should be Lens class and surface number(s1..5)
def EFL(Lens,start_surface=0,end_surface=0):
	print '------------calculating EFL---------------'

	s = Lens.surface_list
	if start_surface == 0:
		start = 1
		end = len(Lens.surface_list)
	else:
		start = start_surface
		end = end_surface
	print 'start surface:',start
	print 'end surface:',end
	R_matrix = []
	T_matrix = []
	RT_matrix = []
	for i in range(start,end-1):
		print 'i:',i
		print 'surface_num',s[i].number
		c = 1/s[i].radius
		# now use central wavelength as reference
		n_left = s[i-1].indexlist[int(len(s[i-1].indexlist)/2)]
		n_right = s[i].indexlist[int(len(s[i].indexlist)/2)]
		t = s[i].thickness
		R1 = R(c,n_left,n_right)
		T1 = T(t,n_right)
		RT_matrix.append(R1)
		if i != end:
			RT_matrix.append(T1)
		else:
			pass
	print RT_matrix
	A,B,C,D = ABCD(RT_matrix)
	print 'Front Focal Point F:',D/C
	print 'Rear Focal Point F\':',-A/C
	print 'Front Principal Point P:', (D-1)/C
	print 'Rear Principal Point P\':',(1-A)/C
	print 'Front Nodal Point N:',(D-1)/C
	print 'Rear Nodal Point N\':',(1-A)/C
	print 'Front Focal Length f:',-1/C
	print 'Rear Focal Length f\':',-1/C
	return 0

def BFL():
	return 0

def FFL():
	return 0

def OAL():
	return 0

def image_height():
	return 0

def EP():
# Entrance pupil's position and diameter
	return 0

def EX():
# Exit pupil's position and diameter
	return 0