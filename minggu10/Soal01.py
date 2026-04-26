file1 = open("Canada.txt")
file2 = open("Swiss.txt")
baris1 = []
baris2 = []
ada_beda = False

for line in file1:
    baris1.append(line.rstrip())
for line in file2:
    baris2.append(line.rstrip())

file1.close()
file2.close()

print("=== Perbandingan File ===")

jumlah_baris = len(baris1)
if len(baris2) > jumlah_baris:
    jumlah_baris = len(baris2)

for i in range(jumlah_baris):
    if i < len(baris1):
        b1 = baris1[i]
    else:
        b1 = "(tidak ada)"
    if i < len(baris2):
        b2 = baris2[i]
    else:
        b2 = "(tidak ada)"
    if b1 != b2:
        ada_beda = True
        print("Baris " + str(i+1) + " berbeda:")
        print("  Canada.txt : " + b1)
        print("  Swiss.txt  : " + b2)
        print()
if ada_beda == False:
    print("Kedua file identik, tidak ada perbedaan.")