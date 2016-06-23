#read a file and count the words into a dictionary
import sys
import string
string.punctuation = '!@#$%^&*()_+-={[}]:;"?\|,./'
#read filename from standard input
if len(sys.argv) != 2:
	print "ERROR: Invalid usage"
	exit()
fname = sys.argv[1]
print "file entered : %s" %(fname)

#open file to read
try:
	fh = open(fname)
except:
	print "ERROR: Cannot open file %s" %(fname)
	exit()
dict1 = dict()
# read line by line and split words in line
# create a dictionary with the words and values as number
# of occurences
for line in fh:
	line = line.translate(None, string.punctuation)
	line = line.lower()
	words = line.split()
	for word in words:
		dict1[word] = dict1.get(word,0) + 1
uniqwords = dict1.keys()
uniqwords.sort()
for uword in uniqwords:
	print "%s : %d" %(uword, dict1[uword])

