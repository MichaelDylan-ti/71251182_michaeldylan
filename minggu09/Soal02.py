import re

def hitung_kata(kalimat, kata_dicari):
    kalimat = kalimat.lower()
    kata_dicari = kata_dicari.lower()
    daftar_kata = re.findall(r'\b\w+\b', kalimat)
    jumlah = 0
    for kata in daftar_kata:
        if kata == kata_dicari:
            jumlah += 1
    return jumlah

kalimat = input("Masukkan kalimat: ")
kata = input("Masukkan kata yang dicari: ")
hasil = hitung_kata(kalimat, kata)
print(f"{kata} ada {hasil} buah")