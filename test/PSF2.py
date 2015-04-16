import numpy as __np__
from numpy import sqrt as __sqrt__
from numpy import cos as __cos__
from numpy import sin as __sin__
import matplotlib.pyplot as __plt__
from mpl_toolkits.mplot3d import Axes3D as __Axes3D__
from matplotlib import cm as __cm__
from matplotlib.ticker import LinearLocator as __LinearLocator__
from matplotlib.ticker import FormatStrFormatter as __FormatStrFormatter__
from numpy.fft import fftshift as __fftshift__
from numpy.fft import ifftshift as __ifftshift__
from numpy.fft import fft2 as __fft2__

l1 = 100
#Generate test surface matrix from a detector
x = __np__.linspace(-1, 1, l1)
y = __np__.linspace(-1, 1, l1)
[X,Y] = __np__.meshgrid(x,y)
r = __sqrt__(X**2+Y**2)
Z = __sqrt__(14)*(8*X**4-8*X**2*r**2+r**4)*(6*r**2-5)
for i in range(len(Z)):
	for j in range(len(Z)):
		if x[i]**2+y[j]**2>1:
			Z[i][j]=0

d = 400
A = __np__.zeros([d,d])
A[d/2-49:d/2+51,d/2-49:d/2+51] = Z
__plt__.imshow(A)
__plt__.show()
def exp_func(a):
	if a == 0:
		return 0
	else:
		return __np__.exp(1j*2*__np__.pi*a)
exp_func1 = __np__.vectorize(exp_func,otypes=[__np__.complex64])
abbe = exp_func1(A)

fig = __plt__.figure(2)
AP = abs(__fftshift__(__fft2__(__fftshift__(abbe))))**2
AP = AP/AP.max()
__plt__.imshow(AP)
__plt__.show()