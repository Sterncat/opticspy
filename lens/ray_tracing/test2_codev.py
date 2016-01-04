from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
from mpl_toolkits.mplot3d import Axes3D
import codev
a = codev.readseq("ag_dblgauss.seq")
print a['EPD']
print a['XAN']
print a['YAN'],'\n'
for i in a['Surface']:
	print i