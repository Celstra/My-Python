name = input("Enter file:")
handle = open(name)

email = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email[words[1]] = email.get(words[1],0) + 1

largest = -1
mostemail = None
for k, v in email.items():
    if v > largest :
        largest = v
        mostemail = k
print(mostemail,largest)
