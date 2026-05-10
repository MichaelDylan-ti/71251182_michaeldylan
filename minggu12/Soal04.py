counts = dict()
fname = input('Masukkan nama file : ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    email = words[1]
    domain = email.split('@')[1]
    if domain not in counts:
        counts[domain] = 1
    else:
        counts[domain] += 1

print(counts)