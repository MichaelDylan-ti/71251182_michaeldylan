import re

kalimat = input("Masukkan kalimat: ")
kata_list = re.findall(r'[a-zA-Z]+', kalimat)
terpendek = kata_list[0]
terpanjang = kata_list[0]

for kata in kata_list:
    if len(kata) < len(terpendek):
        terpendek = kata
    if len(kata) > len(terpanjang):
        terpanjang = kata

print("Terpendek:", terpendek)
print("Terpanjang:", terpanjang)