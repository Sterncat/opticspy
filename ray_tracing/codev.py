import lens
'''
CodeV seq file convertor
return a Lens class
'''



def str2num(str_list):
    num_list = []
    for i in str_list:
        num_list.append(round(float(i),3))
    return num_list


def readseq(filename):
    file = open(filename)
    lines = []
    surface_data = []
    lens_dict = {'Name':'','EPD': 0, 'XAN': [], 'YAN': [], 'Surface':[], 'WL':[],'FNO':0,'NA':0}
    while 1:
        line = file.readline()
        if not line:
            break
        a = line.split()
        #print a
        lines.append(a)
    count = 0
    for line in lines:
        count = count + 1
        # lens name
        if line[0] == 'TITLE':
            lens_dict['Name'] = ''.join(line[1:])
        # wavelength,EPD,XAN,YAN,FNO,NA
        if line[0] in ['WL','EPD','XAN','YAN','FNO','NA']:
            lens_dict[line[0]] = str2num(line[1:])
        # surface
        if line[0] in ['SO','S','SI']:
            if len(line) == 3:
                line.append('')
            surface_data.append(line)
        elif line[0] == 'STO':
            surface_data[-1].append('STO')
    lens_dict['Surface'] = surface_data
    file.close()
    # Generate Lens class
    New_Lens = lens.Lens(lens_name=lens_dict['Name'],creator='XF')

    for w in lens_dict['WL']:
        New_Lens.add_wavelength(wl = w)
    for f in lens_dict['YAN']:
        New_Lens.add_field_YAN(angle = f)
    n = 0
    for s in lens_dict['Surface']:
        n = n + 1
        if float(s[1]) == 0:
            r = 10000000
        else:
            r = float(s[1])
        t = float(s[2])
        if s[3] == '':
            g = 'air'
        else:
            g = s[3]
        if len(s) == 5:
            STOP = True
        else:
            STOP = False
        New_Lens.add_surface(number=n,radius=r,thickness=t,glass=g,STO=STOP)
    return New_Lens






