from __future__ import division as __division__
import numpy as __np__
import matplotlib.pyplot as __plt__
from mpl_toolkits.mplot3d import Axes3D
import codev
a = codev.readseq("test.seq")
for key,value in a.iteritems():
	print key,value