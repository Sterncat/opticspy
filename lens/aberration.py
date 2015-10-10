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

def fieldcurve(sigma3 = 0.05, sigma4 = -0.05, FNO = 10, H = 20):
	"""
	sigma3  Astigmatism Coefficient 
	sigma4  Petzval Coefficient 
	FNO     F-number
	H       Image Height
	"""
	uak = -1.00/(2*FNO)   # maginal ray angle
	h = __np__.linspace(0,1,40)
	XP = -sigma4/uak*h**2
	XT = -(3*sigma3+sigma4)/uak*h**2
	XS = -(sigma3+sigma4)/uak*h**2
	fig = __plt__.figure(figsize=(6, 8), dpi=80)
	__plt__.plot(XP, h*H, 'b-*', label='P')
	__plt__.plot(XT, h*H, 'b--', label='T') 
	__plt__.plot(XS, h*H, 'b', label='S')
	__plt__.xlabel('Surface sag(mm)',fontsize=18)  
	__plt__.ylabel('Real image height(mm)',fontsize=18)  
	legend = __plt__.legend(loc='lower left', shadow=True, fontsize='x-large')
	__plt__.title(r'$\sigma3 = $'+str(round(sigma3,4))+' '+r'$\sigma4 = $'+str(sigma4),fontsize=18) 
	#__plt__.axis([-16, 5, 0, H])
	__plt__.grid(b=True, which='both', color='0.65',linestyle='--')
	__plt__.show()
	return 0