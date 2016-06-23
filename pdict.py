#create a dictionary with dict
pdict1 = dict()
print pdict1

# create a dictionary with flower brackets
pdict2 = {}

#add key value pair to dictionary
pdict2['first'] = '1st'
print pdict2

#create a dictionary with elements
pdict3 = {'name' : 'dan', 'reg-no' : '777', 'marks' : '98'}
print pdict3

#to check if a key exists in a dictionary
if 'reg-no' in pdict3:
	print "key reg-no exists"

#to check if a value exists in a dictionary
vals = pdict3.values()
if '777' in vals:
	print "value 777 exists"

#create a dictionary with null values
pdict4 = dict()
pdict4['abc'] = ''
pdict4['xyz'] = ''
print pdict4
