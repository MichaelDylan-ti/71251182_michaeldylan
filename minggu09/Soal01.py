import re

def bersihkan_kata(kata):
    kata = re.sub(r'[^a-zA-Z]', '', kata)
    return kata.lower()

def cek_anagram(kata1, kata2):
    kata1 = bersihkan_kata(kata1)
    kata2 = bersihkan_kata(kata2)
    return sorted(kata1) == sorted(kata2)

kata1 = input("Masukkan kata acuan: ")
kata2_input = input("Masukkan kata pembaliknya: ")
daftar_kata2 = kata2_input.split(",")

for kata2 in daftar_kata2:
    kata2 = kata2.strip()  # hapus spasi
    if cek_anagram(kata1, kata2):
        print(f"{kata2} -> Anagram")
    else:
        print(f"{kata2} -> Bukan Anagram")