def readseq(filename):
	file = open(filename)
	lines = []
	surface_data = []
	lens_dict = {'EPD': 0, 'XAN': [], 'YAN': [], 'Surface':[]}
	while 1:
		line = file.readline()
		if not line:
			break
		a = line.split()
		lines.append(a)
	count = 0
	for line in lines:
		count = count + 1
		if line[0] in ['SO','S','SI']:
			if len(line) == 3:
				line.append('')
			surface_data.append(line)
		elif line[0] in ['EPD','XAN','YAN','FNO','NA']:
			lens_dict[line[0]] = line[1:]
		elif line[0] == 'STO':
			surface_data[-1].append('STO')
	lens_dict['Surface'] = surface_data
	# for surf in lens_dict['Surface']:
	# 	print surf
	return lens_dict

def find_epd_pos(lens_dict):
	
	return 0