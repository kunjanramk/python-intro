# iterate a list and pull indices
plist = [x for x in range(0,11)]
print plist
for i, ele in enumerate(plist):
	print "index %d : %d" %(i, ele)

