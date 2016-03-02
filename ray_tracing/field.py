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
    print 'Add field angle:'+str(angle)+' degree done'


def field_rays_generator(Lens,angle,n=12,grid_type='grid'):
    grid_list = grid_generator(n,grid_type)
    field_rays_list = grid2rays(Lens,grid_list,angle)
    return field_rays_list

def grid2rays(Lens,grid_list,angle):
    field_rays_list = []
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
        1. in grid type, n means rays accross the center of diameter, n = 12 ==> 88 points
        2. in circular type, n means how many rings in the circle.
            the ring near the center of circle is ring 1, then ring 2,3.
            ring 1 has 1*6 points on it
            ring 2 has 2*6 points on it,etc
            n = 4 ==> 60 points
        3. in random type, n means points in entrance pupil
    type: grid, circular,quasi-random 
    '''
    grid_list = []
    if grid_type == 'grid':
        x1 = y1 = __np__.linspace(-1,1,n)
        for x in x1:
            for y in y1:
                if x**2 + y**2 <= 1:
                    grid_list.append([x,y])
    elif grid_type == 'circular':
        for i in range(n):
            i = i + 1
            theta = __np__.linspace(0,360-360/i/6,i*6)
            r = 1/n*i
            for theta_1 in theta:
                x = r * __np__.cos(theta_1*__np__.pi/180)
                y = r * __np__.sin(theta_1*__np__.pi/180)
                grid_list.append([x,y])

    elif grid_type == 'random':
        r = __np__.sqrt(__np__.random.rand(n))    #sqrt(random(0--r^2)) get radius
        theta = 2*__np__.pi*__np__.random.rand(n)  # random(0--2pi) get theta
        for r_1,theta_1 in zip(r,theta):
            x = r_1 * __np__.cos(theta_1)
            y = r_1 * __np__.sin(theta_1)
            grid_list.append([x,y])
    else:
        print 'No this kind of grid!'
    if output == True:
        fig = __plt__.figure(1,figsize = (5,5))
        ax = __plt__.gca()
        ax.plot(*zip(*grid_list), marker='o', color='r', ls='')
        circle1 = __plt__.Circle((0,0),1,fill=False)
        fig.gca().add_artist(circle1)
        ax.set_xlim([-1,1])
        ax.set_ylim([-1,1])
        ax.set_title('Entrance Pupil Sampling')
        __plt__.show()
        return 0
    else:
        return grid_list



def Y_fan_rays_generator(Lens,n,angle):
    grid_list = []
    x = [0]*n
    y = __np__.linspace(-1,1,n)
    for x1,y1 in zip(x,y):
        grid_list.append([x1,y1])
    field_rays_list = grid2rays(Lens,grid_list,angle)
    return field_rays_list

    
def X_fan_rays_generator(Lens,n,angle):
    grid_list = []
    x = __np__.linspace(0,1,n)
    y = [0]*n
    for x1,y1 in zip(x,y):
        grid_list.append([x1,y1])
    field_rays_list = grid2rays(Lens,grid_list,angle)
    return field_rays_list








