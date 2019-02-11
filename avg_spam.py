# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0
total = 0
data = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue

    data.append(float(line[20:].rstrip()))

for confid in data:
    count += 1

for val in data :
    total += val

print ("Average spam confidence:", total/count)
