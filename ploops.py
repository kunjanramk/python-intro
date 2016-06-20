
# while loop
count = 1
while count < 5 :
	print "while loop"
	count += 1

# for loop
# for loop to iterate a list
plist = ["aby", "dan", "joe"]
for name in plist:
	print "my name is %s" %(name)

# for loop to iterate a sequence of numbers
for iseq in xrange(1,10):
	print iseq,
print
# nested for loop to print numbers
for i in range(1,5):
	for j in range(i):
		print i,
	print
