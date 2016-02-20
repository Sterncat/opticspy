from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__

# Ray Class

class Ray(object):
    def __init__(self,Pos,KLM):
        '''
        Pos: ray position
        KLM: ray direction
        '''
        self.Pos = __np__.asarray(Pos)
        self.KLM = __np__.asarray(KLM)
    def list(self):
        print "Ray Position :",self.Pos
        print "Ray Direction:",self.KLM

class Field(object):
    def __init__(self,Raylist):
        self.ray_list = []
        for i in Raylist:
            self.ray_list.append(Ray(i[0],i[1]))

def add_field_YAN(Lens,angle):
    '''
    Add field by object angle
    Lens.EPD: Entrance pupil diameter
    angle: Object angle 
    '''
    Lens.field_angle_list.append(angle)



def field_rays_generator(Lens,angle,n=12,grid_type='grid'):
    grid_list = grid_generator(n,grid_type)
    EPD = Lens.EPD
    EP = Lens.EP_thickness
    field_rays_list = []
    l = __np__.sin(angle/180*__np__.pi)
    m = __np__.cos(angle/180*__np__.pi)
    KLM = [0,l,m]
    Pos_z = Lens.surface_list[0].thickness
    Pos_y = -(Pos_z + EP)*__np__.tan(angle/180*__np__.pi)
    for relative_ray in grid_list:
        x = EPD/2 * relative_ray[0]
        y = EPD/2 * relative_ray[1] + Pos_y
        Pos = [x,y,0]
        New_Ray = Ray(Pos,KLM)
        field_rays_list.append(New_Ray)
    return field_rays_list



def grid_generator(n,grid_type,output = False):
    '''
    Generate ray grid in normalized pupil
    ========================================
    input: 
    d: different meaning in different type
        1. in grid type, n means rays accross the center of diameter
    type: grid, circular,quasi-random 
    '''
    if grid_type == 'grid':
        grid_list = []
        x1 = y1 = __np__.linspace(-1,1,n)
        for x in x1:
            for y in y1:
                if x**2 + y**2 <= 1:
                    grid_list.append([x,y])
    if output == True:
        fig = __plt__.figure(1)
        ax = __plt__.gca()
        ax.plot(*zip(*grid_list), marker='o', color='r', ls='')
        circle1 = __plt__.Circle((0,0),1,fill=False)
        fig.gca().add_artist(circle1)
        ax.set_aspect('equal')
        __plt__.show()
    return grid_list





    