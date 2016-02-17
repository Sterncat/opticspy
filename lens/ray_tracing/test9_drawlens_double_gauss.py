
import lens, trace, glass, draw


New_Lens = lens.Lens(lens_name='doublegauss',creator='XF')
New_Lens.lens_info()

New_Lens.add_wavelength(wl = 656.30)
New_Lens.add_wavelength(wl = 587.60)
New_Lens.add_wavelength(wl = 486.10)
New_Lens.list_wavelengths()

New_Lens.add_field(angle=0)
New_Lens.add_field(angle=10)
New_Lens.add_field(angle=14)
New_Lens.list_fields()

New_Lens.add_surface(number=1,radius=10000000,thickness=10000000,glass='air')
New_Lens.add_surface(number=2,radius=56.20238,thickness=8.75 ,glass='NSSK2_SCHOTT')
New_Lens.add_surface(number=3,radius=152.28580,thickness=0.5,glass='air')
New_Lens.add_surface(number=4,radius=37.68262,thickness=12.5,glass='NSK2_SCHOTT')
New_Lens.add_surface(number=5,radius=10000000 ,thickness=3.8 ,glass='F5_SCHOTT')
New_Lens.add_surface(number=6,radius=24.23130,thickness=16.369445,glass='air')
New_Lens.add_surface(number=7,radius=10000000,thickness=13.747957,glass='air',STO=True)
New_Lens.add_surface(number=8,radius=-28.37731,thickness=3.8,glass='F5_SCHOTT')
New_Lens.add_surface(number=9,radius=100000000,thickness=11,glass='NSK16_SCHOTT')
New_Lens.add_surface(number=10,radius=-37.92546,thickness=0.5,glass='air')
New_Lens.add_surface(number=11,radius=177.41176,thickness=7,glass='NSK16_SCHOTT')
New_Lens.add_surface(number=12,radius=-79.41143,thickness=61.487536,glass='air')
New_Lens.add_surface(number=13,radius=100000000,thickness=0,glass='air')

trace.trace_sys(New_Lens)
New_Lens.EP()
New_Lens.EX()
draw.draw_system(New_Lens)
