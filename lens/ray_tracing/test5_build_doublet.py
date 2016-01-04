
import lens, trace
import matplotlib.pyplot as __plt__
New_Lens = lens.Lens(lens_name='singlet',creator='XF')
New_Lens.add_surface(number=1,radius=10000000,thickness=10,index=1)
New_Lens.add_surface(number=2,radius=61.07222,thickness=10.345634,index=1.617644,STO=True)
New_Lens.add_surface(number=3,radius=-42.17543,thickness=2.351280,index=1.717355)
New_Lens.add_surface(number=4,radius=-316.13853,thickness=92.451433,index=1)
New_Lens.add_surface(number=5,radius=10000000,thickness=0,index=1)

New_Lens.lens_info()

New_Lens.add_field(angle=3)
print '-------------------------------------------------------'
ray_list = trace.trace_sys(New_Lens)

x2 = []
y2 = []
z2 = []
for ray in ray_list:
	x2.append(ray.Pos[0])
	y2.append(ray.Pos[1])
	z2.append(ray.Pos[2])

fig = __plt__.figure()
__plt__.plot(x2,y2,'b*')
__plt__.show()

#New_Lens.list_surface()
# surface.add(I,)	

# New_Rays = ray.Ray()

# field.add()
# field.add()
# field.add()

# trace.tracing(New_Lens,New_Rays,I)
	