from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
import cal_tools,trace
# All analysis functions

def spotdiagram(Lens,field_plot,wave_plot,n=12,grid_type='grid'):
    '''
    Show spotdiagram of image plane for different field
    input: 
    Lens: Lens Class
    field_plot: list [1,2,3]
    wave_plot: plot wave list [1,2,3]
    '''
    trace.trace_spotdiagram(Lens,n,grid_type)
    field_plot_length = len(field_plot)
    wave_plot_length = len(wave_plot)

    sign_list = ['rs','go','b*','cD','m+','yx','k1','ws']
    marker_list = ['s','o','^','*','D','x','1','s']
    c_list = ['b','g','r','c','m','y','k','w']

    fig = __plt__.figure(2,figsize=(5, 9), dpi=80)
    fig.canvas.set_window_title('Spotdiagram')
    fig.suptitle("Spotdiagram", fontsize="x-large")
    m = 0
    tmp = []
    RMS_list = []
    for i in range(field_plot_length):
        tmp.append(__np__.asarray([[],[]]))
    for wave_num in wave_plot:
        n = field_plot_length
        p = 0
        for field_num in field_plot:
            __plt__.subplot(field_plot_length, 1, n)
            xy_list = spotdiamgram_field_wave(Lens,field_num,wave_num)
            __plt__.scatter(xy_list[0],xy_list[1],marker=marker_list[m],\
                                         edgecolors=c_list[m],alpha=0.5,facecolors='none')
            tmp[p] = __np__.concatenate((tmp[p],xy_list),1)
            p = p + 1
            n = n - 1
        m = m + 1

    for i in tmp:
        rms = cal_tools.rms(i)
        RMS_list.append(str(round(rms,5)))
        print 'RMS',rms


    n = field_plot_length
    m = 0
    for field_num in field_plot:
        __plt__.subplot(field_plot_length, 1, n)
        ax = __plt__.gca()

        Relative_field = str(round(Lens.field_angle_list[field_num-1]/Lens.field_angle_list[-1],2))
        str_angle = str(Lens.field_angle_list[field_num-1]) + ' DG'
        label1 = 'Field'+str(field_num)+'\n'+'0.00, '+Relative_field+'\n'+'0.000, '+str_angle
        ax.annotate(label1, xy=(0.08, 0.73), xycoords='axes fraction', fontsize=12)
        label2 = 'RMS:'+RMS_list[m]
        ax.annotate(label2, xy=(0.7, 0.9), xycoords='axes fraction', fontsize=12)
        ax.set_aspect('equal', 'datalim')
        n = n - 1
        m = m + 1

    __plt__.show()
    return 0

def spotdiamgram_field_wave(Lens,field_num,wave_num):
    all_field_ray_dict_list = Lens.field_trace_info
    n = len(Lens.surface_list)-1
    rays_dict = all_field_ray_dict_list[wave_num-1][field_num-1]
    xy_list = []
    for ray_dict in rays_dict:
        xy_list.append([ray_dict['X'][n],ray_dict['Y'][n]])
    xy_list = __np__.asarray(xy_list)
    xy_list = __np__.transpose(xy_list)
    return xy_list

def Ray_fan(Lens,field_plot,wave_plot):
    '''
    Plot ray fan
    '''
    trace.trace_Y_fan(Lens)
    trace.trace_X_fan(Lens)
    field_plot_length = len(field_plot)
    wave_plot_length = len(wave_plot)
    c_list = ['b','g','r','c','m','y','k','w']
    fig = __plt__.figure(5,figsize=(10, 9), dpi=80)
    fig.canvas.set_window_title('Ray aberration')
    fig.suptitle("Ray aberration: "+Lens.lens_name, fontsize="x-large")
    m = 0
    Py = __np__.linspace(-1,1,25)
    Px = __np__.linspace(0,1,20)
    max_E = 0
    for wave_num in wave_plot:
        n = field_plot_length
        for field_num in field_plot:
            #plot y fan
            __plt__.subplot(field_plot_length, 2, n*2-1)
            xy_list = Y_fan_field_wave(Lens,field_num,wave_num)
            Ey = xy_list[1]-xy_list[1][12]
            __plt__.plot(Py,Ey,c=c_list[m])
            max_tmp = max(abs(Ey))
            if max_tmp > max_E:
                max_E = max_tmp
            #plot x fan
            __plt__.subplot(field_plot_length, 2, n*2)
            xy_list = X_fan_field_wave(Lens,field_num,wave_num)
            Ex = xy_list[0]-xy_list[0][0]
            max_tmp = max(abs(Ex))
            if max_tmp > max_E:
                max_E = max_tmp
            __plt__.plot(Px,Ex,c=c_list[m]) 
            n = n - 1
        m = m + 1


    n = field_plot_length
    for field_num in field_plot:
        # Y fan axis
        __plt__.subplot(field_plot_length, 2, n*2-1)
        ax = __plt__.gca()
        if n == 1:
            ax.set_title("Tangential", fontsize=16)
        ax.set_xlim([-1.1,1.1])
        ax.set_ylim([-max_E*1.1,max_E*1.1])
        __plt__.plot([-1,1],[0,0],c='k')
        __plt__.plot([0,0],[-max_E,max_E],c='k')
        ax.set_ylabel('Field '+str(field_num))
        Relative_field = str(round(Lens.field_angle_list[field_num-1]/Lens.field_angle_list[-1],2))
        str_angle = str(Lens.field_angle_list[field_num-1])+' DG'
        label = Relative_field+' Relative\n'+ 'Field Height\n'+ str_angle 

        ax.annotate(label, xy=(0.7, 0.7), xycoords='axes fraction', fontsize=12)
        # X fan axis
        __plt__.subplot(field_plot_length, 2, n*2)
        ax = __plt__.gca()
        if n == 1:
            ax.set_title("Sagittal", fontsize=16)
        ax.set_xlim([-0.1,1.1])
        ax.set_ylim([-max_E*1.1,max_E*1.1])
        __plt__.plot([0,1],[0,0],c='k')
        __plt__.plot([0,0],[-max_E,max_E],c='k')

        n = n - 1
    __plt__.show()
    return 0

def Y_fan(Lens,field_plot,wave_plot):
    '''
    Tangential fan,plot Ey vs Py
    ''' 
    trace.trace_Y_fan(Lens)
    field_plot_length = len(field_plot)
    wave_plot_length = len(wave_plot)

    c_list = ['b','g','r','c','m','y','k','w']
    fig = __plt__.figure(3,figsize=(5, 9), dpi=80)
    fig.canvas.set_window_title('Ray aberration')
    fig.suptitle("Ray aberration", fontsize="x-large")
    
    m = 0
    Py = __np__.linspace(-1,1,25)
    max_Ey = 0
    for wave_num in wave_plot:
        n = field_plot_length
        for field_num in field_plot:
            __plt__.subplot(field_plot_length, 1, n)
            xy_list = Y_fan_field_wave(Lens,field_num,wave_num)
            Ey = xy_list[1]-xy_list[1][12]
            __plt__.plot(Py,Ey,c=c_list[m])  
            #xy_list[1][12] is the Ey generate by Py=0
            max_tmp = max(abs(Ey))
            if max_tmp > max_Ey:
                max_Ey = max_tmp
            n = n - 1
        m = m + 1


    n = field_plot_length
    for field_num in field_plot:
        __plt__.subplot(field_plot_length, 1, n)
        ax = __plt__.gca()
        ax.set_xlim([-1.1,1.1])
        ax.set_ylim([-max_Ey*1.1,max_Ey*1.1])
        __plt__.plot([-1,1],[0,0],c='k')
        __plt__.plot([0,0],[-max_Ey,max_Ey],c='k')
        n = n - 1

    __plt__.show()
    return 0

def Y_fan_field_wave(Lens,field_num,wave_num):
    all_Y_fan_ray_dict_list = Lens.Y_fan_info
    n = len(Lens.surface_list)-1
    rays_dict = all_Y_fan_ray_dict_list[wave_num-1][field_num-1]
    xy_list = []
    for ray_dict in rays_dict:
        xy_list.append([ray_dict['X'][n],ray_dict['Y'][n]])
    xy_list = __np__.asarray(xy_list)
    xy_list = __np__.transpose(xy_list)
    return xy_list


def X_fan(Lens,field_plot,wave_plot):
    '''
    Sagittal fan,plot Ex vs Px
    ''' 
    trace.trace_X_fan(Lens)
    field_plot_length = len(field_plot)
    wave_plot_length = len(wave_plot)

    c_list = ['b','g','r','c','m','y','k','w']
    fig = __plt__.figure(4,figsize=(5, 9), dpi=80)
    fig.canvas.set_window_title('Ray aberration')
    fig.suptitle("Ray aberration", fontsize="x-large")
    m = 0
    Px = __np__.linspace(0,1,20)
    max_Ex = 0
    for wave_num in wave_plot:
        n = field_plot_length
        for field_num in field_plot:
            __plt__.subplot(field_plot_length, 1, n)
            xy_list = X_fan_field_wave(Lens,field_num,wave_num)
            Ex = xy_list[0]-xy_list[0][0]
            max_tmp = max(abs(Ex))
            if max_tmp > max_Ex:
                max_Ex = max_tmp
            __plt__.plot(Px,Ex,c=c_list[m]) 
            #xy_list[0][0] is the Ex generate by Px=0
            n = n - 1
        m = m + 1


    n = field_plot_length
    for field_num in field_plot:
        __plt__.subplot(field_plot_length, 1, n)
        ax = __plt__.gca()
        ax.set_xlim([-0.1,1.1])
        ax.set_ylim([-max_Ex*1.1,max_Ex*1.1])
        __plt__.plot([0,1],[0,0],c='k')
        __plt__.plot([0,0],[-max_Ex,max_Ex],c='k')
        n = n - 1
    __plt__.show()
    return 0

def X_fan_field_wave(Lens,field_num,wave_num):
    all_X_fan_ray_dict_list = Lens.X_fan_info
    n = len(Lens.surface_list)-1
    rays_dict = all_X_fan_ray_dict_list[wave_num-1][field_num-1]
    xy_list = []
    for ray_dict in rays_dict:
        xy_list.append([ray_dict['X'][n],ray_dict['Y'][n]])
    xy_list = __np__.asarray(xy_list)
    xy_list = __np__.transpose(xy_list)
    return xy_list

