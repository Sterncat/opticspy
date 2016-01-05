from __future__ import division as __division__
import numpy as np
def T(t,n):
	return np.array([[1,t/n],[0,1]])

def R(c,n_left,n_right):
	return np.array([[1,0],[-c*(n_right-n_left),1]])

c1 = 1/56.20238
c2 = 1/(152.28580)
c3 = 1/(37.68262)
c4 = 1/10000000
c5 = 1/24.23130

c6 = 1/(-28.37731)
c7 = 1/(1000000)
c8 = 1/(-37.92546)
c9 = 1/(177.41176)
c10 = 1/(-79.41143)


n1 = 1.622292
n2 = 1.607379
n3 = 1.603417
n4 = 1.620408

t1 = 8.750000
t2 = 0.500000
t3 = 12.500000
t4 = 3.800000 
t5 = 16.369445
t5a = 13.747957
t6 = 3.800000
t7 = 11
t8 = 0.5
t9 = 7


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
R4 = R(c4,n2,n3)
T4 = T(t4,n3)
R5 = R(c5,n3,1)
T5 = T(t5+t5a,1)
R6 = R(c6,1,n3)
T6 = T(t6,n3)
R7 = R(c7,n3,n4)
T7 = T(t7,n4)
R8 = R(c8,n4,1)
T8 = T(t8,1)
R9 = R(c9,1,n4)
T9 = T(t9,n4)
R10 = R(c10,n4,1)
print '-----------------------lens data-----------------------'
ABCD_list = [R1,T1,R2,T2,R3,T3,R4,T4,R5,T5,R6,T6,R7,T7,R8,T8,R9,T9,R10]
M2 = ABCD(ABCD_list)
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


P = (D-1)/C
Pp = (1-A)/C
phi = -C
l = -10000000

lp = 1/(phi + 1/l)
print 'lp',lp
print 'image position 2 l\' = ',lp+Pp






print
print '-----start finding entrance pupil location-----\n'
front3_ABCD_list = [R1,T1,R2,T2,R3,T3,R4,T4,R5]
M2 = ABCD(front3_ABCD_list)
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

P = (D-1)/C
Pp = (1-A)/C
phi = -C
lp = t5 - Pp

l = 1/(1/lp-phi)
print 'P',P
print 'P\'',Pp
print 'lp',lp
print 'entrance pupil position l\' = ',l + P
print

print '-----start finding exit pupil location-----'

back3_ABCD_list = [R6,T6,R7,T7,R8,T8,R9,T9,R10]
M2 = ABCD(back3_ABCD_list)
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

l = -(t5a+P)
print 'power', phi
print 'stop position:',l

lp = 1/(1/l + phi)
print 'exit pupil position l\' = ',lp+Pp

