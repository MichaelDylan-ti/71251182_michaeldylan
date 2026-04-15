import re
from datetime import datetime

teks = input("Masukkan teks: ")
pola = r'\d{4}-\d{2}-\d{2}'
daftar_tanggal = re.findall(pola, teks)
sekarang = datetime.now()

for t in daftar_tanggal:
    tgl = datetime.strptime(t, "%Y-%m-%d")
    selisih = (sekarang - tgl).days
    print(tgl, "selisih", selisih, "hari")