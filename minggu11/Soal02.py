data = []
while True:
    x = input("Masukkan angka (ketik 'done' untuk selesai): ")
    if x == "done":
        break
    data.append(int(x))

if len(data) > 0:
    rata = sum(data) / len(data)
    print("Rata-rata:", rata)
else:
    print("Tidak ada data")