import re

kalimat = input("Masukkan kalimat: ")
hasil = re.sub(r'\s+', ' ', kalimat).strip()

print("Hasil:", hasil)