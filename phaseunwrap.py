import numpy as __np__

# def V(x):
# 	return __np__.arctan2(__np__.sin(x), __np__.cos(x))
# def wrap_diff(x):
# 	return V(np.diff(x))
v = lambda x: __np__.arctan2(__np__.sin(x), __np__.cos(x))
wrap_diff = lambda x: v(__np__.diff(x)) 

def unwrap1D(x):
	y = x
	y[0] = x[0]
	diff = wrap_diff(x)
	for i in range(len(x) - 1):
		i = i + 1
		y[i] = y[i - 1] + diff[i - 1]
	return __np__.array(y)

def unwrap2D(wraped_phase,type="simple"):
	if type == "simple":
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
	else:
		print "No this type of unwrap algorithm"
		return 0




