dic_jam = dict()
lst = list()

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File tidak bisa dibuka:', fname)
    quit()
for baris in fhand:
    kata = baris.split()
    if len(kata) < 3 or kata[0] != 'From':
        continue
    else:
        jam = kata[5].split(':')[0]
        if jam not in dic_jam:
            dic_jam[jam] = 1
        else:
            dic_jam[jam] += 1
for key, val in list(dic_jam.items()):
    lst.append((key, val))
lst.sort()
for key, val in lst:
    print(key, val)