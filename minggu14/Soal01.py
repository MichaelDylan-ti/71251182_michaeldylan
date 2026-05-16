n = int(input('Masukkan jumlah kategori: '))
data_aplikasi = {}

for i in range(n):
    nama_kategori = input('Masukkan nama kategori: ')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)
    data_aplikasi[nama_kategori] = set(aplikasi)

print('\nDaftar aplikasi per kategori:')
for kategori, aplikasi in data_aplikasi.items():
    print(kategori, ':', aplikasi)

daftar_set = list(data_aplikasi.values())

semua = daftar_set[0]
for s in daftar_set[1:]:
    semua = semua.intersection(s)
print('\nAplikasi yang muncul di semua kategori:', semua)

print('\nAplikasi yang hanya muncul di satu kategori:')
for kategori, aplikasi in data_aplikasi.items():
    gabungan_lain = set()
    for kategori_lain, aplikasi_lain in data_aplikasi.items():
        if kategori_lain != kategori:
            gabungan_lain = gabungan_lain.union(aplikasi_lain)
    hanya_satu = aplikasi.difference(gabungan_lain)
    print(kategori, ':', hanya_satu)

if n > 2:
    print('\nAplikasi yang muncul tepat di dua kategori:')
    kategori_list = list(data_aplikasi.keys())
    tepat_dua = set()
    for i in range(len(kategori_list)):
        for j in range(i+1, len(kategori_list)):
            irisan = data_aplikasi[kategori_list[i]].intersection(data_aplikasi[kategori_list[j]])
            # Pastikan tidak muncul di kategori lain
            for k in range(len(kategori_list)):
                if k != i and k != j:
                    irisan = irisan.difference(data_aplikasi[kategori_list[k]])
            tepat_dua = tepat_dua.union(irisan)
    print(tepat_dua)