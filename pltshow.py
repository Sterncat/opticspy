import matplotlib.pyplot as plt
def apershow(obj):
	obj = abs(obj)
	gamax=obj.max()
	gamin=obj.min()
	print gamax
	print gamin
	plt.imshow(obj,vmax=gamax, vmin=gamin)
	plt.show()