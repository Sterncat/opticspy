import numpy
import matplotlib.pyplot as plt
def third(s1,s2,s3,s4,s5):
	"""
	Third order aberrations:
	Ray aberrations
	Field curve
	Distortion

	input: third order aberration coefficient
		   sigma 1~5 

	output: third order aberration graph
	"""
	print "third order aberration"
	py = numpy.linspace(-1,1,100)
	px = numpy.linspace(0,1,50)

	height = [1,0.7,0]
	count = 0
	ax = []
	maxTan = 0
	maxSag = 0


	fig = plt.figure(1)
	for h in height:
		Tan = s1*py**3+3*s2*h*py**2+(3*s3+s4)*h**2.*py+s5*h**3
		ax.append(plt.subplot2grid((3, 3), (count, 0), colspan=2))
		plt.plot(py, Tan)
		if maxTan < max(abs(Tan)): maxTan = max(abs(Tan))
		if count == 0: plt.title('TANGENTIAL')
		plt.axis([-1, 1, -maxTan, maxTan])
		if count == len(height)-1: plt.xlabel('\n' + r'$\rho_y$',fontsize=20)
		plt.ylabel('h = '+str(h),fontsize=15)
		plt.grid(True)

		Sag = s1*px**3+(s3+s4)*h**2*px
		ax.append(plt.subplot2grid((3, 3), (count, 2)))
		plt.plot(px, Sag)
		if maxSag < max(abs(Sag)): maxSag = max(abs(Sag))
		plt.axis([0, 1, -maxSag, maxSag])
		if count == 0: plt.title('SAGITTAL')
		if count == len(height)-1: plt.xlabel('\n' + r'$\rho_x$',fontsize=20)
		plt.grid(True)
		
		count = count + 1

	fig.set_tight_layout(True)

	plt.show()