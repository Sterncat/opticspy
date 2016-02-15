
import lens, trace, glass


New_Lens = lens.Lens(lens_name='singlet',creator='XF')
New_Lens.lens_info()

New_Lens.add_wavelength(wl = 500)
New_Lens.list_wavelengths()

New_Lens.add_field(angle=0)
New_Lens.add_field(angle=7)
New_Lens.add_field(angle=10)
New_Lens.list_fields()

New_Lens.add_surface(number=1,radius=10000000,thickness=5,glass='air')
New_Lens.add_surface(number=2,radius=50.00000,thickness=5.000000 ,glass='BK7_SCHOTT')
New_Lens.add_surface(number=3,radius=1175.71107,thickness=96.572831,glass='air')
New_Lens.add_surface(number=4,radius=100000000,thickness=0,glass='air')

#trace.trace_sys(New_Lens)
New_Lens.EFL()
New_Lens.OAL(2,3)