
import lens, trace, glass


New_Lens = lens.Lens(lens_name='doublet',creator='XF')
New_Lens.lens_info()

New_Lens.add_wavelength(wl = 656.30)
New_Lens.add_wavelength(wl = 546.10)
New_Lens.add_wavelength(wl = 486.10)
New_Lens.list_wavelengths()

New_Lens.add_field(angle=0)
New_Lens.add_field(angle=2)
New_Lens.add_field(angle=3)
New_Lens.list_fields()

New_Lens.add_surface(number=1,radius=10000000,thickness=0,glass='air')
New_Lens.add_surface(number=2,radius=61.07222,thickness=10.345634,glass='BSM24_OHARA',STO=True)
New_Lens.add_surface(number=3,radius=-42.17543,thickness=2.351280,glass='SF1_SCHOTT')
New_Lens.add_surface(number=4,radius=-316.13853,thickness=92.451433,glass='air')
New_Lens.add_surface(number=5,radius=10000000,thickness=0,glass='air')


trace.trace_sys(New_Lens)

New_Lens.spotdiagram()
