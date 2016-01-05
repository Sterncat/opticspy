import surface, field, analysis

# Ray Class

class Lens(object):
	def __init__(self,lens_name='',creator=''):
		self.surface_list = []
		self.field_list = []
		self.lens_name = lens_name
		self.creator = creator
		self.image_plane_ray_list = []
	def lens_info(self):
		print self.lens_name
		print self.creator

	def list_surface(self):
		print 'list all surface information'
		for i in self.surface_list:
			print i

	def list_fields(self):
		print 'list all fields information'
		for i in self.field_list:
			print i

	def first_order(self):
		print 'first order information'

	def thickness(self,start_surface,end_surface):
		print 'thickness between 2 surface'

	def radius(self,surface_number):
		print 'surface radius' 
#-----------------------surface functions-----------------------
	def add_surface(self,number,radius,thickness,index,STO=False):
		surface.add(self,number,radius,thickness,index,STO)
	# def update_surface(self,number,radius,thickness,index,STO):
	# 	surface.update(self,number,radius,thickness,index,STO)
	# def delete_surface(self,number,radius,thickness,index,STO):
	# 	surface.delete(self,number,radius,thickness,index,STO)


#-----------------------Field functions--------------------------
	def add_field(self,angle):
		field.add_field_YAN(self,angle)

#-----------------------Spotdiagram------------------------------
	def spotdiagram(self):
		analysis.spotdiagram(self)







	