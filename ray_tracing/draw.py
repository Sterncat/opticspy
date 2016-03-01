from __future__ import division as __division__
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
import trace
# All lens drawing and ray drawing functions

def draw_surface(r,x0,d1,d2):
    '''
    d1: diameter that rays go through
    d2: max diameter for a lens, doublet, let edge be flat
    '''
    verts_1 = []
    verts_2 = []
    codes = []
    for y in np.linspace(0,d1/2,10):
        if r > 0:
            x = -np.sqrt(r**2-y**2) + r
        else:
            x = np.sqrt(r**2-y**2) + r
        verts_1.append([x+x0,y])
        verts_2.append([x+x0,-y])
    if d1 == d2:
        verts = verts_1[::-1] + verts_2[1:]
    elif d1 < d2:
        verts = [[verts_1[-1][0],d2/2]] + verts_1[::-1] + verts_2[1:] + [[verts_2[-1][0],-d2/2]]
    codes.append(Path.MOVETO)
    for j in range(len(verts)-1):
        codes.append(Path.LINETO)
    return verts,codes,[verts[0],verts[-1]]



def draw_system(Lens):
    print '------------------start drawing lens system-------------'
    # adjust diameter
    surface_list = Lens.surface_list
    m = len(surface_list)
    label_list = []
    label_list1 = []
    for num in range(m):
        if num == 0:
            if surface_list[num].glass != ('air' or 'AIR'):
                label_list.append(1)
            else:
                label_list.append(0)
        else:
            if (surface_list[num-1].glass == ('air' or 'AIR')) and (surface_list[num].glass != ('air' or 'AIR')):
                label_list.append(1)
            elif (surface_list[num-1].glass != ('air' or 'AIR')) and (surface_list[num].glass != ('air' or 'AIR')):
                label_list.append(1)
            elif (surface_list[num-1].glass != ('air' or 'AIR')) and (surface_list[num].glass == ('air' or 'AIR')):
                label_list.append(2)
            else:
                label_list.append(0)

    label_list1.append([])
    for num in range(m):
        n = len(label_list1)
        if label_list[num] == 0:
            label_list1[n-1].append(num)
            label_list1.append([])
            n = n + 1
        elif label_list[num] == 1:
            label_list1[n-1].append(num)
        else:
            label_list1[n-1].append(num)
            label_list1.append([])
            n = n + 1
    label_list1.pop()

    draw_diameter_list = [0]*len(surface_list)
    max_diameter_list = []
    for unit_list in label_list1:
        max_d = 0
        for s_index in unit_list:
            if surface_list[s_index].__diameter__ >= max_d:
                max_d = surface_list[s_index].__diameter__
        max_diameter_list.append(max_d)

    k = -1
    for unit_list in label_list1:
        k = k + 1
        for s_index in unit_list:
            draw_diameter_list[s_index] = max_diameter_list[k]

    fig = plt.figure(figsize=(12, 6))
    fig.canvas.set_window_title('View Lens')
    fig.suptitle('View Lens: '+Lens.lens_name, fontsize="x-large")
    ax = fig.add_subplot(111)
    thinkness_list = []
    start_end_list = []
    verts_list = []
    codes_list = []
    for num in range(m):
        r = surface_list[num].radius
        glass = surface_list[num].glass
        t = surface_list[num].thickness
        thinkness_list.append(t)
        d1 = surface_list[num].__diameter__
        d2 = draw_diameter_list[num]

        if num == 0:
            x0 = 0 - thinkness_list[0]
        else:
            x0 = sum(thinkness_list[0:-1]) - thinkness_list[0]
            #print x0
        verts,codes,start_end = draw_surface(r,x0,d1,d2)
        start_end_list.append(start_end)
        verts_list.append(verts)
        codes_list.append(codes)

        # start drawing surface
        #print 'draw surface:',num+1
        path = Path(verts, codes)
        patch = patches.PathPatch(path, facecolor='none', lw=1)
        ax.add_patch(patch)

        # start drawing edge
        if num == 0:
            pass
        elif surface_list[num-1].glass != ('air' or 'AIR'):
            #print 'drawing edge:',num,'---',num+1
            verts1 = [start_end_list[num-1][0],start_end_list[num][0]]
            #print verts1
            verts2 = [start_end_list[num-1][1],start_end_list[num][1]]
            #print verts2
            codes = [Path.MOVETO,Path.LINETO]
            path = Path(verts1,codes)
            patch = patches.PathPatch(path,fill=0, lw=1)
            ax.add_patch(patch)
            path = Path(verts2,codes)
            patch = patches.PathPatch(path, facecolor='none',fill=0, lw=1)  
            ax.add_patch(patch)
        else:
            pass

    'start drawing rays'
    path_list = draw_rays(Lens)
    m = 0
    color_list = ['red']*3+['green']*3+['blue']*3 
    for path, linecolor in zip(path_list,color_list):
        patch1 = patches.PathPatch(path, facecolor='none',fill=0, lw=1,edgecolor=linecolor)
        ax.add_patch(patch1)
    ax.set_xlim(-0.5*sum(thinkness_list[1:-1]),1.1*sum(thinkness_list[1:-1]))
    d = max(draw_diameter_list)
    ax.set_ylim(-d/4*3,d/4*3)
    plt.show()


def draw_rays(Lens):
    '''
    draw chief and marginal rays, draw field
    '''
    ray_list = trace.trace_draw_ray(Lens)
    path_list = []
    for ray in ray_list:
        p = draw_line(Lens,ray)
        path_list.append(p)
    return path_list

def draw_line(Lens,ray_tracing):
    verts = []
    codes = []
    n = 0
    t = 0
    for ray in ray_tracing:
        Pos = ray[0].Pos
        if n == 0:
            verts.append([-(Pos[2]+Lens.surface_list[n].thickness),Pos[1]])
        elif n == 1:
            verts.append([Pos[2],Pos[1]])
        else:
            t = t + Lens.surface_list[n-1].thickness
            verts.append([Pos[2]+t,Pos[1]])
        codes.append(Path.LINETO)
        n = n + 1
    codes[0] = Path.MOVETO
    path = Path(verts,codes)
    #print verts
    return path




