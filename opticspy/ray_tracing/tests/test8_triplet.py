
import lens, trace, glass


New_Lens = lens.Lens(lens_name='triplet',creator='XF')
New_Lens.lens_info()

New_Lens.add_wavelength(wl = 656.30)
New_Lens.add_wavelength(wl = 546.10)
New_Lens.add_wavelength(wl = 486.10)
New_Lens.list_wavelengths()

New_Lens.add_field(angle=0)
New_Lens.add_field(angle=7)
New_Lens.add_field(angle=10)
New_Lens.list_fields()

New_Lens.add_surface(number=1,radius=10000000,thickness=5,glass='air')
New_Lens.add_surface(number=2,radius=16.87831,thickness=3.250000 ,glass='NSK16_SCHOTT')
New_Lens.add_surface(number=3,radius=247.02634,thickness=4.984142,glass='air')
New_Lens.add_surface(number=4,radius=-35.95718,thickness=1.250000,glass='NF2_SCHOTT',STO=True)
New_Lens.add_surface(number=5,radius=15.88615 ,thickness=6.099225 ,glass='air')
New_Lens.add_surface(number=6,radius=49.08083,thickness=3.250000,glass='NSK16_SCHOTT')
New_Lens.add_surface(number=7,radius=-27.62109,thickness=38.898042,glass='air')
New_Lens.add_surface(number=8,radius=100000000,thickness=0,glass='air')

trace.trace_sys(New_Lens)

New_Lens.spotdiagram()
