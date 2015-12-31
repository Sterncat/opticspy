from __future__ import division as __division__
import numpy as np
def T(t,n):
	return np.array([[1,t/n],[0,1]])

def R(c,n_left,n_right):
	return np.array([[1,0],[-c*(n_right-n_left),1]])

c1 = 1/41.15909
c2 = 1/(-957.83146)
c3 = 1/(-51.32104)
c4 = 1/42.37768
c6 = 1/247.44562
c7 = 1/(-40.04016)

n1 = 1.638537
n2 = 1.647685
n3 = n1

#n1 = 1.635052
#n2 = 1.642088
#n3 = n1

#n1 = 1.646586
#n2 = 1.661257
#n3 = n1

t1 = 6.097555
t2 = 9.349584
t3 = 2.032518
t4 = 5.995929 
t5 = 4.065037
t6 = 6.097555

def ABCD(matrix_list):
	M = matrix_list.pop()
	while matrix_list:
		M = np.dot(M,matrix_list.pop())
	return M
	
R1 = R(c1,1,n1)
T1 = T(t1,n1)
R2 = R(c2,n1,1)
T2 = T(t2,1)
R3 = R(c3,1,n2)
T3 = T(t3,n2)
R4 = R(c4,n2,1)
T4 = T(t4+t5,1)
R5 = R(c6,1,n3)
T5 = T(t6,n3)
R6 = R(c7,n3,1)

ABCD_list = [R1,T1,R2,T2,R3,T3,R4,T4,R5,T5,R6]

M2 = ABCD(ABCD_list)

print M2

A = M2[0,0]
B = M2[0,1]
C = M2[1,0]
D = M2[1,1]

print A*D-B*C

print 'Front Focal Point F:',D/C
print 'Rear Focal Point F\':',-A/C
print 'Front Principal Point P:', (D-1)/C
print 'Rear Principal Point P\':',(1-A)/C
print 'Front Nodal Point N:',(D-1)/C
print 'Rear Nodal Point N\':',(1-A)/C
print 'Front Focal Length f:',-1/C
print 'Rear Focal Length f\':',-1/C


F = D/C
Fp = -A/C
f = -1/C
fp = -1/C
z = -10000000


zp = f*fp/z

print 'zp:',zp
print 'image position:',Fp + zp



print '-----start finding entrance pupil location-----\n'
front2_ABCD_list = [R1,T1,R2,T2,R3,T3,R4]
M2 = ABCD(front2_ABCD_list)
A = M2[0,0]
B = M2[0,1]
C = M2[1,0]
D = M2[1,1]

print A*D-B*C

print 'Front Focal Point F:',D/C
print 'Rear Focal Point F\':',-A/C
print 'Front Principal Point P:', (D-1)/C
print 'Rear Principal Point P\':',(1-A)/C
print 'Front Nodal Point N:',(D-1)/C
print 'Rear Nodal Point N\':',(1-A)/C
print 'Front Focal Length f:',-1/C
print 'Rear Focal Length f\':',-1/C

phi = -C
P = (D-1)/C
Pp = (1-A)/C

lp = t4-Pp
print 'power', phi
print 'stop position:',lp

l = 1/(1/lp - phi)
print 'entrance pupil position l\' = ',l + P
# one reason that the value different from codev is we 
# only use one wavelength only use one(but not the only reason)
