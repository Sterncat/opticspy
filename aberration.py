import numpy as __np__
import matplotlib.pyplot as __plt__
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
	py = __np__.linspace(-1,1,100)
	px = __np__.linspace(0,1,50)

	height = [1,0.7,0]
	count = 0
	ax = []
	maxTan = 0
	maxSag = 0


	fig = __plt__.figure(1)
	for h in height:
		Tan = s1*py**3+3*s2*h*py**2+(3*s3+s4)*h**2.*py+s5*h**3
		ax.append(__plt__.subplot2grid((3, 3), (count, 0), colspan=2))
		__plt__.plot(py, Tan)
		if maxTan < max(abs(Tan)): maxTan = max(abs(Tan))
		if count == 0: __plt__.title('TANGENTIAL')
		__plt__.axis([-1, 1, -maxTan, maxTan])
		if count == len(height)-1: __plt__.xlabel('\n' + r'$\rho_y$',fontsize=20)
		__plt__.ylabel('h = '+str(h),fontsize=15)
		__plt__.grid(True)

		Sag = s1*px**3+(s3+s4)*h**2*px
		ax.append(__plt__.subplot2grid((3, 3), (count, 2)))
		__plt__.plot(px, Sag)
		if maxSag < max(abs(Sag)): maxSag = max(abs(Sag))
		__plt__.axis([0, 1, -maxSag, maxSag])
		if count == 0: __plt__.title('SAGITTAL')
		if count == len(height)-1: __plt__.xlabel('\n' + r'$\rho_x$',fontsize=20)
		__plt__.grid(True)
		
		count = count + 1

	fig.set_tight_layout(True)

	__plt__.show()