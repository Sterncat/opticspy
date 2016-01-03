
import lens, surface
New_Lens = lens.Lens(lens_name='singlet',creator='XF')
New_Lens.add_surface(number=1,radius=50,thickness=2,index=1.5)
New_Lens.add_surface(number=2,radius=-100,thickness=5,index=1.3,STO=True)
New_Lens.add_surface(3,5,10,1.2)
New_Lens.lens_info()
#New_Lens.list_surface()
# surface.add(I,)	

# New_Rays = ray.Ray()

# field.add()
# field.add()
# field.add()

# trace.tracing(New_Lens,New_Rays,I)
	