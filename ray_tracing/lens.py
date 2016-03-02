import surface, field, analysis, wavelength, first_order_tools, draw

# Ray Class

class Lens(object):
	surface_list = []
	def __init__(self,lens_name='',creator=''):
		self.lens_name = lens_name
		self.creator = creator
		self.field_angle_list = []
		self.wavelength_list = []
		self.EP_thickness = 0
		self.EFL = 0
		self.EPD = 0
		self.FNO = 0
		self.tmp_ray = []
		self.object_position = 0
		self.image_plane_ray_list = []
		self.field_trace_info = []
		self.Y_fan_info = []

	def lens_info(self):
		print self.lens_name
		print self.creator

	def list_surface(self):
		print 'list all surface information'
		for i in self.surface_list:
			print i

	def list_fields(self):
		print 'list all fields information'
		for i in self.field_angle_list:
			print 'Field angle:',i


	def refresh_paraxial(self):
		self.EFL = first_order_tools.EFL(self,0,0)
		self.EPD = self.EFL/self.FNO
		self.EP_thickness = first_order_tools.EP(self)
		self.object_position = -1000000    # temporary only for infinity conjugate
		start = 2
		end = len(self.surface_list)
		OAL = first_order_tools.OAL(self,start,end)
		Pos_z = OAL * 0.2

		# entrance pupil fake surface use as surface 1
		self.surface_list[0] = surface.Surface(wavelength_list = self.wavelength_list,number=1,\
										radius=10000000,thickness=Pos_z,glass='air',STO=False,\
										__diameter__=0)

	def solve_imageposition(self):
		self.surface_list[-2].thickness = first_order_tools.image_position(self)

	def first_order(self):
		print 'first order information'

	def EFY(self,start_surface=0,end_surface=0):
		EFY = first_order_tools.EFL(self,start_surface,end_surface)
		return EFY

	def BFL(self):
		first_order_tools.BFL(self)

	def OAL(self,start_surface=0,end_surface=0):
		first_order_tools.OAL(self,start_surface,end_surface)

	def image_position(self):
		first_order_tools.image_position(self)

	def EP(self):
		EP = first_order_tools.EP(self)
		return EP

	def EX(self):
		first_order_tools.EX(self)

	def radius(self,surface_number):
		print 'surface radius' 
#-----------------------surface functions-----------------------
	def add_surface(self,number,radius,thickness,glass,STO=False):
		surface.add(self,number,radius,thickness,glass,STO)
	# def update_surface(self,number,radius,thickness,index,STO):
	# 	surface.update(self,number,radius,thickness,index,STO)
	# def delete_surface(self,number,radius,thickness,index,STO):
	# 	surface.delete(self,number,radius,thickness,index,STO)


#-----------------------Field functions--------------------------
	def add_field_YAN(self,angle):
		field.add_field_YAN(self,angle)

#-----------------------Wavelength Fucntions---------------------
	def add_wavelength(self,wl):
		print 'Add wavelength '+ str(wl) + 'nm done'
		wavelength.add(self,wl)

	def list_wavelengths(self):
		print 'List all wavelength information'
		for i in self.wavelength_list:
			print 'Wavelength',i,'nm'

#-----------------------Spotdiagram------------------------------
	def spotdiagram(self):
		analysis.spotdiagram(self)

	def list_image_ray_info(self):
		print self.image_plane_ray_list






	