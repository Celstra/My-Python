fname = input("Enter file name: ")

fh = open(fname)
lst = list()
uniq = []
print(uniq)

for line in fh:
    line.rstrip()
    lst = line.split()
    for x in lst:
        if x not in uniq:
            uniq.append(x)
            uniq.sort()
print(uniq)
