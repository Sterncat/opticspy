from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
import field,first_order_tools,surface
import output_tools

# Function: trace rays
# input a list of ray 
# output [ray position and direction] on next surface


def trace_spotdiagram(Lens,n,grid_type):
    '''
    trace all field,all wavelength through all surfaces
    return list of dictionary
    '''
    all_field_ray_dict_list = []
    for wave_num in range(len(Lens.wavelength_list)):
        wave_num = wave_num + 1
        one_wavelength_trace = []
        for field_num in range(len(Lens.field_angle_list)):
            field_num = field_num + 1
            field_ray_dict_list = trace_field_wave(Lens,field_num,wave_num,n,grid_type)
            one_wavelength_trace.append(field_ray_dict_list)
        all_field_ray_dict_list.append(one_wavelength_trace)
    Lens.field_trace_info = all_field_ray_dict_list
    return all_field_ray_dict_list

def trace_Y_fan(Lens):
    all_Y_fan_ray_dict_list = []
    for wave_num in range(len(Lens.wavelength_list)):
        wave_num = wave_num + 1
        one_wavelength_trace = []
        for field_num in range(len(Lens.field_angle_list)):
            field_num = field_num + 1
            field_ray_dict_list = trace_Y_fan_field_wave(Lens,field_num,wave_num,n=25)
            one_wavelength_trace.append(field_ray_dict_list)
        all_Y_fan_ray_dict_list.append(one_wavelength_trace)

    Lens.Y_fan_info = all_Y_fan_ray_dict_list
    return all_Y_fan_ray_dict_list

def trace_X_fan(Lens):
    all_X_fan_ray_dict_list = []
    for wave_num in range(len(Lens.wavelength_list)):
        wave_num = wave_num + 1
        one_wavelength_trace = []
        for field_num in range(len(Lens.field_angle_list)):
            field_num = field_num + 1
            field_ray_dict_list = trace_X_fan_field_wave(Lens,field_num,wave_num,n=20)
            one_wavelength_trace.append(field_ray_dict_list)
        all_X_fan_ray_dict_list.append(one_wavelength_trace)

    Lens.X_fan_info = all_X_fan_ray_dict_list
    return all_X_fan_ray_dict_list




def trace_field_wave(Lens,field_num,wave_num,n,grid_type):
    '''
    trace one field in one wavelength
    '''
    field_angle = Lens.field_angle_list[field_num-1]
    field_rays_list = field.field_rays_generator(Lens,field_angle,n,grid_type)
    field_ray_dict_list = raylist2raydict(Lens,field_rays_list,wave_num)
    return field_ray_dict_list

def trace_Y_fan_field_wave(Lens,field_num,wave_num,n):
    field_angle = Lens.field_angle_list[field_num-1]
    Y_fan_rays_list = field.Y_fan_rays_generator(Lens,n,field_angle)
    Y_fan_ray_dict_list = raylist2raydict(Lens,Y_fan_rays_list,wave_num)
    return Y_fan_ray_dict_list

def trace_X_fan_field_wave(Lens,field_num,wave_num,n):
    field_angle = Lens.field_angle_list[field_num-1]
    X_fan_rays_list = field.X_fan_rays_generator(Lens,n,field_angle)
    X_fan_ray_dict_list = raylist2raydict(Lens,X_fan_rays_list,wave_num)
    return X_fan_ray_dict_list


def raylist2raydict(Lens,rayslist,wave_num):
    '''
    Trace ray from entrance pupil through all surface
    ==========================================================
    input:
    Lens: Lens instance
    raylist: ray list in EP
    wave_num: wavelength number
    '''
    field_ray_dict_list = []
    surface_list = Lens.surface_list
    for ray_list in rayslist:
        ray_list = [ray_list]
        ray_tracing = []
        ray_tracing.append(ray_list)
        for i in range(len(surface_list)-1):
            ray_list = traceray(ray_list, surface_list[0+i], surface_list[1+i], wave_num)
            ray_tracing.append(ray_list)
        ray_dict = ray2dict(ray_tracing)
        field_ray_dict_list.append(ray_dict)
    return field_ray_dict_list





def trace_draw_ray(Lens):
    '''
    trace ray for drawing lens and find the diameter of lens
    chief ray(0,0),marginal ray(0,1)(0,-1) in different field
    so if there are 3 field, len(ab_ray_list) = 9

    It is trace the marginal rays, so it is similar to the set vig part

    output: ab_ray_list
    '''
    ab_ray_list = []
    list_1 = []
    list_2 = []
    wave_num = int(len(Lens.wavelength_list)/2+1)
    for field_num in range(len(Lens.field_angle_list)):
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
    #print '============================================'
    for i,j in zip(list_1,list_2):
        tmp1 = []
        tmp2 = []
        #print '++++++++++++++++++++++++++++++++++++++++'
        for m,n in zip(i,j):
            ray_height1 = abs(m[0].Pos[1])
            ray_height2 = abs(n[0].Pos[1])
            tmp1.append(ray_height1)
            tmp2.append(ray_height2)
        diameter_list.append(tmp1)
        diameter_list.append(tmp2)
    #print '============================================'
    D = []
    diameter_list = __np__.asarray(diameter_list)
    diameter_list = __np__.transpose(diameter_list)
    for i in diameter_list:
        #print i
        D.append(max(i)*2)

    for (surface,d) in zip(Lens.surface_list,D):
        surface.__diameter__ = d*1.1
    return ab_ray_list



def trace_one_ray(Lens,field_num,wave_num,ray,start=0,end=0,output=False,output_list=[]):
    '''
    trace specific rays
    ------------------------------
    input: 
    field: int, field number
    wave_num: wavelength number
    ray: relative ray to entrance pupil
            [0,0]  Chief ray
            [0,1]  (+Y)Meridional ray
            [0,-1] (-Y)Meridional ray
            [1,0]  (+X)Sagital Ray 
            [-1,0] (-X)Sagiral Ray
    '''
    #print '-------------------ray tracing------------------'
    ray_tracing = []
    EP = Lens.EP_thickness
    EPD = Lens.EPD
    # print 'Entrance pupil position',EP
    # print 'Entrance pupil diameter',EPD
    angle = Lens.field_angle_list[field_num-1]
    surface_list = Lens.surface_list
    ray_list = []
    Pos_z = surface_list[0].thickness

  #   if ray == [0,0]:
  #       print 'trace chief ray'
  #   elif ray == [0,1] or ray == [0,-1]:
        # print 'trace meridional ray(y)'
  #   elif ray == [1,0] or ray == [-1,0]:
        # print 'trace sagiral ray(x)'
  #   else:
  #       print 'trace one ray'

    Pos_x = Lens.EPD/2 * ray[0]    # not general enough, now only could trace y angle ray
                                   # not really need to be traced?
                                   # need to think
    Pos_y = -(Pos_z + EP)*__np__.tan(angle/180*__np__.pi) + Lens.EPD/2 * ray[1]
    l = __np__.sin(angle/180*__np__.pi)
    m = __np__.cos(angle/180*__np__.pi)
    Pos = [Pos_x,Pos_y,0]
    KLM = [0,l,m]
    Ray_1 = field.Ray(Pos,KLM)
    ray_list.append(Ray_1)
    ray_tracing.append(ray_list)
    for i in range(len(surface_list)-1):
        ray_list = traceray(ray_list, surface_list[0+i], surface_list[1+i], wave_num)
        ray_tracing.append(ray_list)

    ray_dict = ray2dict(ray_tracing)
    if output == True:
        output_tools.ray_output(ray_dict=ray_dict,start=start,end=end,output_list=output_list)
        return 0
    else:
        return ray_tracing


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
        n1 = surface1.indexlist[wave_num-1]
        n2 = surface2.indexlist[wave_num-1]
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

def ray2dict(ray_tracing):
    #print 'ray2dict============',len(ray_tracing),'============='
    ray_dict = {'Num':[],'X':[],'Y':[],'Z':[],'K':[],'L':[],'M':[]}
    n = 0
    for ray_list in ray_tracing:
        n = n + 1
        Ray = ray_list[0]
        Pos = Ray.Pos
        KLM = Ray.KLM
        ray_dict['X'].append(Pos[0])
        ray_dict['Y'].append(Pos[1])
        ray_dict['Z'].append(Pos[2])
        ray_dict['K'].append(KLM[0])
        ray_dict['L'].append(KLM[1])
        ray_dict['M'].append(KLM[2])
        ray_dict['Num'].append(n)
    return ray_dict







