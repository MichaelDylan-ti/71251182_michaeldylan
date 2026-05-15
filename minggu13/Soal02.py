data = ('Michael Dylan', '71251182', 'JL. Kusbisni, Kota Yogyakarta')
print("Data: ", data)
print()

nama, nim, alamat = data
print("NIM   :", nim)
print("NAMA  :", nama)
print("ALAMAT:", alamat)
print()

print("NIM:", tuple(nim))
print()
nama_depan = nama.split()[0]
print("NAMA DEPAN:", tuple(nama_depan[1:]))
print()
nama_terbalik = tuple(nama.split()[::-1])
print("NAMA TERBALIK:", nama_terbalik)