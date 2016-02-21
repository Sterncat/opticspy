import lens, trace, glass, draw, analysis, field


New_Lens = lens.Lens(lens_name='triplet',creator='XF')
New_Lens.FNO = 3
New_Lens.lens_info()

New_Lens.add_wavelength(wl = 656.30)
New_Lens.add_wavelength(wl = 546.10)
New_Lens.add_wavelength(wl = 486.10)
New_Lens.list_wavelengths()

New_Lens.add_field_YAN(angle=0)
New_Lens.add_field_YAN(angle=14)
New_Lens.add_field_YAN(angle=20)
New_Lens.list_fields()

New_Lens.add_surface(number=1,radius=10000000,thickness=1000000,glass='air')
New_Lens.add_surface(number=2,radius=16.87831,thickness=3.250000,glass='NSK16_SCHOTT')
New_Lens.add_surface(number=3,radius=247.02634,thickness=4.984142,glass='air')
New_Lens.add_surface(number=4,radius=10000000,thickness=0,glass='air',STO=True)
New_Lens.add_surface(number=5,radius=-35.95718 ,thickness=1.250000,glass='NF2_SCHOTT')
New_Lens.add_surface(number=6,radius=15.88615,thickness=6.099225,glass='air')
New_Lens.add_surface(number=7,radius=49.08083,thickness=3.250000,glass='NSK16_SCHOTT')
New_Lens.add_surface(number=8,radius=-27.62109,thickness=38.898042,glass='air')
New_Lens.add_surface(number=9,radius=10000000,thickness=0,glass='air')

New_Lens.refresh_paraxial()
trace.trace_draw_ray(New_Lens)
trace.trace_one_ray(New_Lens,field_num=3,wave_num=2,ray=[0,-1],start=0,end=0,output=True,output_list=['X','Y','Z','K','L','M'])
draw.draw_system(New_Lens)
#field_ray_dict_list = trace.trace_field_wave(New_Lens,1,2)
#all_field_ray_dict_list = trace.trace_sys(New_Lens)
#analysis.spotdiamgram_field_wave(New_Lens,2,3)
#analysis.spotdiagram(New_Lens,[1,2,3],[1,2,3])

#New_Lens.image_position()
#New_Lens.EFY()

