
import lens, trace
import matplotlib.pyplot as __plt__
New_Lens = lens.Lens(lens_name='singlet',creator='XF')
New_Lens.add_surface(number=1,radius=10000000,thickness=1,index=1)
New_Lens.add_surface(number=2,radius=61.07222,thickness=10.345634,index=1.617644,STO=True)
New_Lens.add_surface(number=3,radius=-42.17543,thickness=2.351280,index=1.717355)
New_Lens.add_surface(number=4,radius=-316.13853,thickness=92.451433,index=1)
New_Lens.add_surface(number=5,radius=10000000,thickness=0,index=1)

New_Lens.lens_info()

New_Lens.add_field(angle=0)
New_Lens.add_field(angle=2)
New_Lens.add_field(angle=3)

New_Lens.list_fields()

print '-------------------------------------------------------'
trace.trace_sys(New_Lens)

New_Lens.spotdiagram()


	