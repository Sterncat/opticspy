from __future__ import division as __division__
import numpy as np


c1 = 1/50
c2 = 1/(1175.71107)
n = 1.521414

R1 = np.array([[1,0],[-c1*(n-1),1]])
T2 = np.array([[1,5/n],[0,1]])
R2 = np.array([[1,0],[-c2*(1-n),1]])


M1 = np.dot(R2,T2)
M2 = np.dot(M1,R1)   # caution the order of dot() calculation of T1,T2... R1,R2....

A = M2[0,0]
B = M2[0,1]
C = M2[1,0]
D = M2[1,1]

print A*D-B*C

print 'f:',-1/C

print 'Front Focal Point F:',D/C
print 'Rear Focal Point F\':',-A/C
print 'Front Principal Point P:', (D-1)/C
print 'Rear Principal Point P\':',(1-A)/C
print 'Front Nodal Point N:',(D-1)/C
print 'Rear Nodal Point N\':',(1-A)/C
print 'Front Focal Length f:',-1/C
print 'Rear Focal Length f\':',-1/C


phi = -C
l = 0.000001

print 'stop position:',l

l_prime = 1/(phi + 1/l)
print 'entrance pupil position l\' = ',l_prime


