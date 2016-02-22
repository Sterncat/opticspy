# format output tools
from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__


# real ray tracing output
def ray_output(ray_dict,output_list,start,end):
    '''
    real ray tracing output
    ==============================================
    input:
    Lens: Lens class instance
    start: start surface, default = 2
    end: end surface, if end = 0, output from surface 1 to last(image) surface
    print: default = 'true'
    *args could be 'X','Y','Z','K','M','L','AOI','AOR'
    '''
    line_length = len(output_list)

    if start == 0 and end == 0:
        start = 2
        end = len(ray_dict['Num'])
        
    row_length = end - start + 1
    #print row_length
    
    header_format = '%-*s' * (line_length+1)
    header_tup1 = (5,'Num')
    header_tup2 = (5,'=====')
    
    for s in output_list:
        header_tup1 = header_tup1 + (10,) + (s,)
        header_tup2 = header_tup2 + (10,) + ('==========',)
    print header_format % header_tup1
    print header_format % header_tup2

    line_format = '%-*d' + '%-*.2f' * line_length
    for line in range(row_length):
        line = line + start - 1
        line_tup = (5,ray_dict['Num'][line])
        for s in output_list:
            tmp = ray_dict[s][line]
            line_tup = line_tup + (10,) + (round(tmp,2),)
        print line_format % line_tup
    print header_format % header_tup2
    return 0


    