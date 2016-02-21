from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
import cal_tools
# All analysis functions

def spotdiagram(Lens,field_plot,wave_plot):
    '''
    Show spotdiagram of image plane for different field
    input: 
    Lens: Lens Class
    field_plot: list [1,2,3]
    wave_plot: plot wave list [1,2,3]
    '''
    all_field_ray_dict_list = Lens.field_trace_info
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
    for i in range(field_plot_length):
        tmp.append(__np__.asarray([[],[]]))
    for wave_num in wave_plot:
        n = field_plot_length
        p = 0
        print len(tmp),'asadsdasda'
        for field_num in field_plot:
            __plt__.subplot(field_plot_length, 1, n)
            xy_list = spotdiamgram_field_wave(Lens,field_num,wave_num)
            __plt__.scatter(xy_list[0],xy_list[1],marker=marker_list[m],\
                                         edgecolors=c_list[m],alpha=0.5,facecolors='none')
            __plt__.axis('equal')
            tmp[p] = __np__.concatenate((tmp[p],xy_list),1)
            p = p + 1
            n = n - 1
        m = m + 1

    for i in tmp:
        rms = cal_tools.rms(i)
        print 'RMS',rms

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




