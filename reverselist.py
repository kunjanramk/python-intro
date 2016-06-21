# reverse a list 
mylist = range(1,11)
print mylist
llen = len(mylist)
print "length of list is %d" %(llen)
# using while loop
i = -1
while i >= -llen :
	print mylist[i],
	i -= 1
print
# using for loop
for x in mylist[::-1]:
	print x,
print
