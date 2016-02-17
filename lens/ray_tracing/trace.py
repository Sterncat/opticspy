from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
import field,first_order_tools,surface

# Function: trace rays
# input a list of ray 
# output [ray position and direction] on next surface



def trace_sys(Lens):
	'''
	trace all field through all surfaces, and give the spotgram
	of the Image(last) surface
	'''
	surface_list = Lens.surface_list
	field_list  = Lens.field_list
	wavelength_list = Lens.wavelength_list
	for field in field_list:
		field_info = []
		for wave_num in range(len(wavelength_list)):
			ray_list = field.ray_list
			for i in range(len(surface_list)-1):
				ray_list = traceray(ray_list, surface_list[0+i], surface_list[1+i], wave_num)
			field_info.append(ray_list)
		Lens.image_plane_ray_list.append(field_info)

	# for surface in surface_list:
	# 	print surface.radius
	# 	surface.__diameter__ = 18



def trace_ab_ray(Lens):
	'''
	trace a ray and b ray
	chief ray(0,0),marginal ray(0,1)(0,-1) in different field
	so if there are 3 field, len(ab_ray_list) = 9
	output: ab_ray_list
	'''
	ab_ray_list = []
	list_1 = []
	list_2 = []
	wave_num = int(len(Lens.wavelength_list)/2+1)
	for field_num in range(len(Lens.field_list)):
		field_num = field_num + 1
		chief_ray_list = trace_one_ray(Lens,field_num,wave_num,[0,0])
		marginal_ray_list_1 = trace_one_ray(Lens,field_num,wave_num,[0,1])
		marginal_ray_list_2 = trace_one_ray(Lens,field_num,wave_num,[0,-1])
		ab_ray_list.append(chief_ray_list)
		ab_ray_list.append(marginal_ray_list_1)
		ab_ray_list.append(marginal_ray_list_2)

		list_1.append(marginal_ray_list_1) # length 3
		list_2.append(marginal_ray_list_2) # length 3

	# start find surface aperture diameter
	diameter_list = []
	print '============================================'
	for i,j in zip(list_1,list_2):
		tmp1 = []
		tmp2 = []
		print '++++++++++++++++++++++++++++++++++++++++'
		for m,n in zip(i,j):
			ray_height1 = abs(m[0].Pos[1])
			ray_height2 = abs(n[0].Pos[1])
			tmp1.append(ray_height1)
			tmp2.append(ray_height2)
		diameter_list.append(tmp1)
		diameter_list.append(tmp2)
	print '============================================'
	D = []
	diameter_list = __np__.asarray(diameter_list)
	diameter_list = __np__.transpose(diameter_list)
	for i in diameter_list:
		print i
		D.append(max(i)*2)

	for (surface,d) in zip(Lens.surface_list,D):
		surface.__diameter__ = d*1.1
	return ab_ray_list



def trace_one_ray(Lens,field_num,wave_num,ray):
    '''
    trace specific rays
    ------------------------------
    input: 
    field: int, field number
    wave_num: wavelength number
    ray: relative ray to entrance pupil
            [0,0] chef ray
            [0,1] marginal ray1
            [0,-1] marginal ray2
       	also could do [1,0] [-1,0]
    '''
    print '---------------start tracing chief rays--------------'
    Lens.chief_ray_tracing = []
    EP = Lens.EP_thickness
    EPD = Lens.EPD
    print 'Entrance pupil position',EP
    print 'Entrance pupil diameter',EPD
    angle = Lens.field_angle_list[field_num-1]
    surface_list = Lens.surface_list
    ray_list = []
    start = 2
    end = len(surface_list)
    OAL = first_order_tools.OAL(Lens,start,end)
    Pos_z = OAL*0.2
    surface_list[0] = surface.Surface(wavelength_list = Lens.wavelength_list,number=1,\
                            radius=10000000,thickness=Pos_z,glass='air',STO=False,\
                            __diameter__=0)
    #print 'z position:',Pos_z
    if ray == [0,0]:
        print 'trace chef ray'
    elif ray == [0,1] or ray == [0,-1]:
    	print 'trace marginal ray(y)'
    elif ray == [1,0] or ray == [-1,0]:
    	print 'trace marginal ray(x)'
    else:
    	print 'trace one ray'

    Pos_x = ray[0] * Lens.EPD/2
    #print angle
    Pos_y = -(OAL*0.2 + EP)*__np__.tan(angle/180*__np__.pi) + Lens.EPD/2 * ray[1]
    #print 'y position:',Pos_y
    l = __np__.sin(angle/180*__np__.pi)
    m = __np__.cos(angle/180*__np__.pi)
    Pos = [Pos_x,Pos_y,0]
    KLM = [0,l,m]
    ray = field.Ray(Pos,KLM)
    ray_list.append(ray)

    Lens.chief_ray_tracing.append(ray_list)
    for i in range(len(surface_list)-1):
        ray_list = traceray(ray_list, surface_list[0+i], surface_list[1+i], wave_num)
        Lens.chief_ray_tracing.append(ray_list)
        # three chief rays
    #print 'surface_list',len(surface_list)
    return Lens.chief_ray_tracing


def traceray(ray_list, surface1, surface2, wave_num):
    '''
	Basic ray tracing function, tracing ray position and ray direction from
	one surface to next surface 
	Return ray position and ray direction
    '''
    ray_num = len(ray_list)
    new_ray_list = []
    Pos_new_list = []
    KLM_new_list = []
    for ray in ray_list:
        Pos = ray.Pos
        #print 'Pos',Pos
        KLM = ray.KLM
        #print 'KLM:',KLM
        c1 = 1 / surface1.radius
        c2 = 1 / surface2.radius
        n1 = surface1.indexlist[wave_num]
        n2 = surface2.indexlist[wave_num]
        tn1 = surface1.thickness
        tn2 = surface2.thickness
        xyz = __np__.asarray([Pos[0], Pos[1], Pos[2] - tn1])
        #print 'xyz',xyz
        delta, cosI = pos(xyz, KLM, c2)
        Pos_new = xyz + delta * KLM
        Pos_new_list.append(Pos_new)
        # calculate new ray direction
        # if curvature == 0, it is a stop, object or image plane
        # don't need to calculate the new ray direction
        if c2 == 0:
            KLM_new = KLM
        else:
            sigma = __np__.sqrt(n2 ** 2 - n1 ** 2 * (1 - cosI ** 2)) - n1 * cosI
            Kp = (n1 * KLM[0] - c2 * sigma * Pos_new[0]) / n2
            Lp = (n1 * KLM[1] - c2 * sigma * Pos_new[1]) / n2
            Mp = (n1 * KLM[2] - c2 * sigma * Pos_new[2] + sigma) / n2
            KLM_new = __np__.asarray([Kp, Lp, Mp])
        KLM_new_list.append(KLM_new)

    for Pos,KLM in zip(Pos_new_list,KLM_new_list):
    	new_ray_list.append(field.Ray(Pos,KLM))

    return new_ray_list


def pos(Pos, KLM, curvature):
    '''
    calculate new position of a ray on spherical surface
    '''
    c = curvature
    x0 = Pos[0]
    y0 = Pos[1]
    z0 = Pos[2]
    K = KLM[0]
    L = KLM[1]
    M = KLM[2]
    E = c * (x0 ** 2 + y0 ** 2 + z0 ** 2) - 2 * z0
    G = M - c * (K * x0 + L * y0 + M * z0)
    delta = E / (G + __np__.sqrt(G ** 2 - c * E))
    cosI = __np__.sqrt(G ** 2 - c * E)
    return delta, cosI
