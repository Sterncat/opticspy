from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
import cal_tools
# Ray Class

def spotdiagram(Lens,field_plot,wave_plot):
    '''
    Show spotdiagram of image plane for different field
    input: 
    Lens Class
    field_plot: list [1,2,3]
    wave_plot: plot wave list [1,2,3]
    '''
    all_field_ray_dict_list = Lens.field_trace_info
    field_plot_length = len(field_plot)
    wave_plot_length = len(wave_plot)

    sign_list = ['rs','go','b*','cD','m+','yx','k1','ws']
    

    fig = __plt__.figure(2,figsize=(5, 9), dpi=80)
    m = field_plot_length
    for wave_num in wave_plot:
        for field_num in field_plot:
            __plt__.subplot(field_plot_length, 1, field_plot_length-field_num+1)
            xy_list = spotdiamgram_field_wave(Lens,field_num,wave_num)
            __plt__.plot(xy_list[0],xy_list[1],sign_list[m-1])
            __plt__.axis('equal')
        m = m - 1
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

    # fig = __plt__.figure(2)
    # ax = __plt__.gca()
    # __plt__.plot(xy_list[0],xy_list[1],'r*',ls='')
    # __plt__.show()

    return xy_list




