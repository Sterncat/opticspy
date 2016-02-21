
import lens, trace, glass, draw, analysis, field


New_Lens = lens.Lens(lens_name='triplet',creator='XF')
New_Lens.FNO = 10
New_Lens.lens_info()

New_Lens.add_wavelength(wl = 656.30)
New_Lens.add_wavelength(wl = 587.60)
New_Lens.add_wavelength(wl = 486.10)
New_Lens.list_wavelengths()

New_Lens.add_field_YAN(angle=0)
New_Lens.add_field_YAN(angle=14)
New_Lens.add_field_YAN(angle=20)
New_Lens.list_fields()

New_Lens.add_surface(number=1,radius=10000000,thickness=1000000,glass='air')
New_Lens.add_surface(number=2,radius=41.15909,thickness=6.097555 ,glass='BSM18_OHARA')
New_Lens.add_surface(number=3,radius=-957.83146,thickness=9.349584,glass='air')
New_Lens.add_surface(number=4,radius=-51.32104,thickness=2.032518,glass='PBM22_OHARA')
New_Lens.add_surface(number=5,radius=42.37768 ,thickness=5.995929 ,glass='air')
New_Lens.add_surface(number=6,radius=10000000,thickness=4.065037,glass='air',STO=True)
New_Lens.add_surface(number=7,radius=247.44562,thickness=6.097555,glass='BSM18_OHARA')
New_Lens.add_surface(number=8,radius=-40.04016,thickness=85.593426,glass='air')
New_Lens.add_surface(number=9,radius=10000000,thickness=0,glass='air')

New_Lens.refresh_paraxial()
#field.grid_generator(5,grid_type='random',output = 1)
#print New_Lens.EP_thickness
#print New_Lens.EFL
#print New_Lens.EPD
#print New_Lens.FNO
#trace.trace_ab_ray(New_Lens)
#New_Lens.image_position()
dict_list = trace.trace_draw_ray(New_Lens)
draw.draw_system(New_Lens)
trace.trace_sys(New_Lens,n=5,grid_type='circular')
analysis.spotdiagram(New_Lens,[1,2,3],[1,2,3])
