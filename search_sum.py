import re
fname = input('Enter a file name: ')

try:
	fhandle = open(fname)
except:
	print ('File cannot be opened:', fname)
	exit()

x = list()

for line in fhandle:
     y = re.findall('[0-9]+', line)
     x = x + y

sum = 0

for z in x:
    sum = sum + int(z)

print(sum)
