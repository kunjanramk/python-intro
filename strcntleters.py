#given a string count how many each letter appears
string1 = "malayalam"
dict1 = dict()
# using if condition
for letr in string1:
	if letr in dict1:
		dict1[letr] += 1
	else:
		dict1[letr] = 1
print "string : %s" %(string1)
print "letter : count"
for key1 in dict1:
	print "%s : %d" %(key1, dict1[key1])

dict2 = dict()
# using get method
for lr in string1:
	dict2[lr] = dict2.get(lr,0) + 1
print dict2

