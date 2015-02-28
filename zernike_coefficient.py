class Zernike(object):
	list_1 = []
	def __init__(self, 
			Z0=0, Z1=0, Z2=0, Z3=0, Z4=0, Z5=0, Z6=0, Z7=0, \
			Z8=0, Z9=0, Z10=0, Z11=0, Z12=0, Z13=0, Z14=0, \
			Z15=0, Z16=0, Z17=0, Z18=0, Z19=0, Z20=0, Z21=0, \
			Z22=0, Z23=0, Z24=0, Z25=0, Z26=0, Z27=0, Z28=0, \
			Z29=0, Z30=0, Z31=0, Z32=0, Z33=0, Z34=0, Z35=0):
		self.Z0 = Z0
		self.Z1 = Z1
		self.Z2 = Z2
		self.Z3 = Z3
		self.Z4 = Z4
		self.Z5 = Z5
		self.Z6 = Z6
		self.Z7 = Z7
		self.Z8 = Z8
		self.Z9 = Z9
		self.Z10 = Z10
		self.Z11 = Z11
		self.Z12 = Z12
		self.Z13 = Z13
		self.Z14 = Z14
		self.Z15 = Z15
		self.Z16 = Z16
		self.Z17 = Z17
		self.Z18 = Z18
		self.Z19 = Z19
		self.Z20 = Z20
		self.Z21 = Z21
		self.Z22 = Z22
		self.Z23 = Z23
		self.Z24 = Z24
		self.Z25 = Z25
		self.Z26 = Z26
		self.Z27 = Z27
		self.Z28 = Z28
		self.Z29 = Z29
		self.Z30 = Z30
		self.Z31 = Z31
		self.Z32 = Z32
		self.Z33 = Z33
		self.Z34 = Z34
		self.Z35 = Z35

		self.list_1 = [Z0, Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, \
					Z11, Z12, Z13, Z14, Z15, Z16, Z17, Z18, Z19, \
					Z20, Z21, Z22, Z23, Z24, Z25, Z26, Z27, Z28, \
					Z29, Z30, Z31, Z32, Z33, Z34, Z35,]
	def listcoefficient(self):
		m = 0
		for i in self.list_1:
			if i != 0:
				print 'Z'+str(m)+' =',i
			m = m + 1









