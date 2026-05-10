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
    if words[1] not in counts:
        counts[words[1]] = 1
    else:
        counts[words[1]] += 1

print(counts)