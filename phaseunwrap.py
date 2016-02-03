import numpy as __np__
from unwrap import unwrap as __unwrap__

v = lambda x: __np__.arctan2(__np__.sin(x), __np__.cos(x))
wrap_diff = lambda x: v(__np__.diff(x)) 

#Depth first search algorithm, use to find phase map(where)
def DFS(M,ph1,m,n,s):
	stack = []
	stack.append([m,n])
	M[m,n] = 2
	ph = __np__.zeros([s,s])

	while (len(stack) != 0):
		[m,n] = stack[-1]
		if m + 1 < s and n < s and M[m+1,n] == 1 and M[m+1,n] != 0 and M[m+1,n] != 2:
			m = m + 1
			M[m,n] = 2
			stack.append([m,n])
			#print m,n
			
			ph[m,n] = ph[m-1,n] + v(ph1[m,n] - ph1[m-1,n])
			
		elif m - 1 > 0 and n < s and M[m-1,n] == 1 and M[m-1,n] != 0 and M[m-1,n] != 2:
			m = m - 1
			M[m,n] = 2
			stack.append([m,n])
			#print m,n
			
			ph[m,n] = ph[m+1,n] + v(ph1[m,n] - ph1[m+1,n])
			
		elif m < s and n + 1 < s and M[m,n+1] == 1 and M[m,n+1] != 0 and M[m,n+1] != 2: 
			n = n + 1
			M[m,n] = 2
			stack.append([m,n])
			#print m,n
			
			ph[m,n] = ph[m,n-1] + v(ph1[m,n] - ph1[m,n-1])
			
		elif m < s and n - 1 > 0 and M[m,n-1] == 1 and M[m,n-1] != 0 and M[m,n-1] != 2: 
			n = n - 1
			M[m,n] = 2
			stack.append([m,n])
			#print m,n
			
			ph[m,n] = ph[m,n+1] + v(ph1[m,n] - ph1[m,n+1])
			
		else:
			stack.pop()
	return ph

def unwrap1D(x):
	"""
	1D phase unwrap function. 
	"""
	y = x
	y[0] = x[0]
	diff = wrap_diff(x)
	for i in range(len(x) - 1):
		i = i + 1
		y[i] = y[i - 1] + diff[i - 1]
	return __np__.array(y)

def unwrap2D(wraped_phase,type="boundary",noise = True):
	"""
	2D unwarp function. There are several type to 
	use in several different situation.

	Type:
	-----------------------------------------------
	Simple: The very simple algorithm to unwrap 2D warpped phase
			just scan the whole matrix to unwrap phase. Very noise 
			sensitive

	boundary: 2D phase unwrap method for phase map with aperture, 
			  for example, circle, rectangular, ring or slit. It 
			  use a DFS(deep first search) algorithm to traverse
			  the phase map, then unwarp the phase.It is also very 
			  noise sensitive
	etc: still have more, to be continue

	"""
	if type == "simple" and noise == False:
		l = len(wraped_phase)
		b = []
		b = __np__.array(b)
		for i in range(l):
			if i%2 == 0:
				b = __np__.append(b,wraped_phase[i])
			else:
				b = __np__.append(b,wraped_phase[i][::-1])
		ph1 = unwrap1D(b)
		ph = __np__.zeros([l,l])
		for i in range(l):
			if i%2 == 0:
				ph[i] = ph1[0:l]
				ph1 = ph1[l:]
			else:
				ph[i] = ph1[0:l][::-1]
				ph1 = ph1[l:]
		return ph
		
	elif type == "boundary" and noise == False:
		ph1 = wraped_phase[0]
		M = wraped_phase[1]
		s = wraped_phase[2]
		start_pixel = __np__.where(M == 1)
		m = start_pixel[0][0]
		n = start_pixel[1][0]
		print "start pixel",m,n
		ph = DFS(M,ph1,m,n,s)
		return ph

	elif noise == True:
		ph1 = wraped_phase[0]
		M = wraped_phase[1]
		s = wraped_phase[2]
		ph = __unwrap__(ph1,wrap_around_axis_0=False,\
							wrap_around_axis_1=False,\
							wrap_around_axis_2=False)
		return ph

	else:
		print "No this type of unwrap algorithm"
		return 0




