from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__

def zoom_cal(f1,f2,fshort,flong):
	"""
	Two element infinite conjugate zoom - 1st order analysis
	Try example:
	zoom_cal(f1 = 30,f2 = -30, fshort = 35, flong = 70)
	========================================================
	input
	--------------------------------------------------------
	f1: first element focal length
	f2: second element focal length
	fshort: big focal length
	flong: small focal length

	output
	--------------------------------------------------------
	zoom position analysis

	"""
	fsys = __np__.linspace(fshort,flong,20)
	t = f1 + f2 - f1*f2/fsys
	s2_prime = (f1-t)*f2/((f1-t)+f2) 
	__plt__.figure(figsize=(8, 6), dpi=80)
	__plt__.plot(fsys,s2_prime, 'b-*', label='Lens #2')
	__plt__.plot(fsys,s2_prime + t, 'b-s', label='Lens #1')
	__plt__.xlabel('Focal length(mm)',fontsize=18)  
	__plt__.ylabel('Position from image(mm)',fontsize=18)  
	legend = __plt__.legend(loc='lower right', shadow=True, fontsize='x-large')
	__plt__.title('Lens position\n'+' f1='+str(f1)+'mm f2='+str(f2)+\
				'mm fshort='+str(fshort)+'mm flong='+str(flong)+'mm',fontsize=18) 
	__plt__.grid(b=True, which='both', color='0.65',linestyle='--')
	__plt__.show()
	return 0

def __solve__(f1,f2,L,M):
	"""
	quadratic equation solve
	"""
	delta = L**2-4*(L*(f1+f2)+(M-1)**2*f1*f2/M)
	t1 = (L + __np__.sqrt(delta))/2
	t2 = (L - __np__.sqrt(delta))/2
	return [t1,t2]


def zoom_cal2(f1,f2,L,Mhigh,Mlow):
	"""
	Two element finite conjugate zoom
	Try example 
	zoom_cal2(40,60,400,-15,-2.5)
	========================================================
	input
	--------------------------------------------------------
	f1: first element focal length
	f2: second element focal length
	Mhigh: high Magnification
	Mlow: low Magnification

	output
	--------------------------------------------------------
	zoom position analysis
	"""
	points = 20
	M = __np__.linspace(Mlow,Mhigh,points)
	M = __np__.asarray(M)
	[t1,t2] = __solve__(f1,f2,L,M)
	# Solution 1
	s1a = ((M-1)*t1+L)/((M-1)-M*t1/f1)
	P1a = L + s1a
	P2a = L + s1a - t1
	P3a = [L]*len(M)
	# Solution 2
	s1b = ((M-1)*t2+L)/((M-1)-M*t2/f1)
	P1b = L + s1b
	P2b = L + s1b - t2
	P3b = [L]*len(M)
	
	__plt__.figure(1,figsize=(8, 6), dpi=80)
	__plt__.plot(M,P1a,'b-s',label='Lens #1')
	__plt__.plot(M,P2a,'b-*',label='Lens #2')
	__plt__.plot(M,P3a,'b-d',label='Object position')
	__plt__.xlabel('Magnification',fontsize=18)  
	__plt__.ylabel('Position from Image Plane(mm)',fontsize=18)
	__plt__.title("Solution 1",fontsize=18)  
	__plt__.grid(b=True, which='both', color='0.65',linestyle='--')
	legend = __plt__.legend(loc='lower right', shadow=True, fontsize='medium')
	min_1 = min(min(P1a),min(P2a),min(P3a))
	max_1 = max(max(P1a),max(P2a),max(P3a))
	__plt__.axis([min(M), max(M), min_1-50, max_1+50])
	__plt__.show()
	
	__plt__.figure(2,figsize=(8, 6), dpi=80)
	__plt__.plot(M,P1b,'b-s',label='Lens #1')
	__plt__.plot(M,P2b,'b-*',label='Lens #2')
	__plt__.plot(M,P3b,'b-d',label='Object position')
	__plt__.xlabel('Magnification',fontsize=18)  
	__plt__.ylabel('Position from Image Plane(mm)',fontsize=18)
	__plt__.title("Solution 2",fontsize=18)  
	__plt__.grid(b=True, which='both', color='0.65',linestyle='--')
	legend = __plt__.legend(loc='lower left', shadow=True, fontsize='medium')
	min_2 = min(min(P1b),min(P2b),min(P3b))
	max_2 = max(max(P1b),max(P2b),max(P3b))
	__plt__.axis([min(M), max(M), min_2-50, max_2+50])
	__plt__.show()
	return 0

def zoom_cal3(f0,f1,f2,flong,fshort,L_prime):
	Mhigh = flong/f0
	Mlow = fshort/f0
	L = L_prime - f0
	points = 20
	F = __np__.linspace(fshort,flong,points)
	M = __np__.linspace(Mlow,Mhigh,points)
	M = __np__.asarray(M)
	[t1,t2] = __solve__(f1,f2,L,M)
	
	s1a = ((M-1)*t1+L)/((M-1)-M*t1/f1)
	P0a = [L + f0]*points
	P1a = L + s1a
	P2a = L + s1a - t1
	
	s1b = ((M-1)*t2+L)/((M-1)-M*t2/f1)
	P0b = [L + f0]*points
	P1b = L + s1b
	P2b = L + s1b - t2
	
	__plt__.figure(1,figsize=(8, 6), dpi=80)
	__plt__.plot(F,P0a,'b-d',label='Lens #1')
	__plt__.plot(F,P1a,'b-s',label='Lens #2')
	__plt__.plot(F,P2a,'b-*',label='Lens #3')
	__plt__.xlabel('Focal length(mm)',fontsize=18)  
	__plt__.ylabel('Position from Image Plane(mm)',fontsize=18)
	__plt__.title("Lens Position Solution 1",fontsize=18)  
	__plt__.grid(b=True, which='both', color='0.65',linestyle='--')
	legend = __plt__.legend(loc='lower right', shadow=True, fontsize='medium')
	min_1 = min(min(P0a),min(P1a),min(P2a))
	max_1 = max(max(P0a),max(P1a),max(P2a))
	__plt__.axis([min(F), max(F), min_1-50, max_1+50])
	__plt__.show()
	
	__plt__.figure(1,figsize=(8, 6), dpi=80)
	__plt__.plot(F,P0b,'b-d',label='Lens #1')
	__plt__.plot(F,P1b,'b-s',label='Lens #2')
	__plt__.plot(F,P2b,'b-*',label='Lens #3')
	__plt__.xlabel('Focal length(mm)',fontsize=18)  
	__plt__.ylabel('Position from Image Plane(mm)',fontsize=18)
	__plt__.title("Lens Position Solution 2",fontsize=18)  
	__plt__.grid(b=True, which='both', color='0.65',linestyle='--')
	legend = __plt__.legend(loc='lower right', shadow=True, fontsize='medium')
	min_2 = min(min(P0b),min(P1b),min(P2b))
	max_2 = max(max(P0b),max(P1b),max(P2b))
	__plt__.axis([min(F), max(F), min_2-50, max_2+50])
	__plt__.show()
	return 0




