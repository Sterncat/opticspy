import os

filepath = []
rootdir = "glass_database/"
glass_catalog = 'schott'
filename = 'N-LAK9.yml'
for root, subFolders, files in os.walk(rootdir):
	if root.endswith(glass_catalog):
		break
for f in files:
	if f == filename:
		filepath = os.path.join(root,filename)
		break
print filepath

