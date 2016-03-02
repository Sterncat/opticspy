# first order tools, find EPD, calculate system power, etc
from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__


def start_end(Lens,start_surface,end_surface):
	'''
	return start end surface index
	'''
	if start_surface == 0:
		start = 2
		end = len(Lens.surface_list) - 1
	else:
		start = start_surface
		end = end_surface
	print 'start surface:',start
	print 'end surface:',end
	return start,end


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

def ABCD_start_end(Lens,start_surface=0,end_surface=0):
	'''
	matrix calculation
	------------------------------------
	input: Lens Class,start_surface,end_surface
	output: ABCD matrix
	'''
	s = Lens.surface_list
	start,end = start_end(Lens,start_surface,end_surface)
	R_matrix = []
	T_matrix = []
	RT_matrix = []
	for i in range(start,end+1):
		i = i - 1
		# print 'i:',i
		# print 'surface_num',s[i].number
		c = 1/s[i].radius
		# now use central wavelength as reference
		n_left = s[i-1].indexlist[int(len(s[i-1].indexlist)/2)]
		n_right = s[i].indexlist[int(len(s[i].indexlist)/2)]
		t = s[i].thickness
		R1 = R(c,n_left,n_right)
		T1 = T(t,n_right)
		# print R1
		# print T1
		RT_matrix.append(R1)
		if i+1 != end:
			RT_matrix.append(T1)
	# print '--------------------------------'
	# for i in RT_matrix:
	# 	print i
	# print '--------------------------------'
	A,B,C,D = ABCD(RT_matrix)
	return A,B,C,D


def list(Lens):
	'''
	List first order information of a lens system
	input: Lens Class
	output: print information
			refresh Lens first order information
	'''
	return 0


# input should be Lens class and surface number(s1..5)
def EFL(Lens,start_surface,end_surface):
	print '------------Calculating EFL---------------'
	A,B,C,D = ABCD_start_end(Lens,start_surface,end_surface)
	EFL = -1/C
	print 'Rear Focal Length f\':',-1/C
	return EFL

def BFL(Lens):
	print '------------Calculating BFL---------------'
	BFL = Lens.surface_list[-2].thickness
	print 'Back focal length:',BFL
	return BFL

def FFL():
	return 0

def OAL(Lens,start_surface,end_surface):
	print '------------Calculating OAL---------------'
	s = Lens.surface_list
	start,end = start_end(Lens,start_surface,end_surface)
	OAL = 0
	for i in range(start,end):
		OAL = OAL + s[i-1].thickness
	print 'Overall length:',OAL
	return OAL

def image_position(Lens):
	'''
	Calculate paraxial image position
	'''
	print '------------Calculating image position---------------'
	s = Lens.surface_list
	z = Lens.object_position  # object distance
	print 'object distance',z
	A,B,C,D = ABCD_start_end(Lens,start_surface=0,end_surface=0)
	f = -1/C
	fp = -1/C
	Fp = -A/C
	zp = f*fp/z
	image_position = Fp + zp
	print 'image position:',image_position
	return image_position

def EP(Lens):
	# Entrance pupil's position and diameter
	print '---------Calculating Entrance Pupil Position-----------'
	s = Lens.surface_list
	
	for surface in s:
		if surface.STO == True:
			n = surface.number
			print 'STOP Surface',n
			if n == 2:
				EP = 0
				return EP
			else:
				t_stop = s[n-2].thickness
				print 'STOP thickness',t_stop
				start_surface = 2
				end_surface = n - 1
		else:
			pass
	A,B,C,D = ABCD_start_end(Lens,start_surface,end_surface)
	phi = -C
	P = (D-1)/C
	Pp = (1-A)/C
	lp = t_stop-Pp
	l = 1/(1/lp - phi)
	EP = l + P
	print 'entrance pupil position EP:',EP
	return EP

def EX(Lens):
	# Exit pupil's position and diameter
	print '---------Calculating Exit Pupil Position-----------'
	s = Lens.surface_list
	for surface in s:
		if surface.STO == True:
			n = surface.number
			print 'STOP Surface',n
			if n == len(s)-1:
				EX = 0   # if stop at last, EX = 0, code V do this
				return EX
			else:
				t_stop = s[n-1].thickness
				print 'STOP thickness',t_stop
				start_surface = n + 1
				end_surface = len(s) - 1
		else:
			pass
	A,B,C,D = ABCD_start_end(Lens,start_surface,end_surface)
	phi = -C
	P = (D-1)/C
	Pp = (1-A)/C
	l = -(t_stop+P)
	lp = 1/(1/l + phi)
	EX = lp + Pp
	print 'exit pupil position EX:',EX
	return EX

## note for future work: for system no in air, need to change part of program,
## For example, 'Rear Focal Length f\':',-1/C ----> -np/C, etc



