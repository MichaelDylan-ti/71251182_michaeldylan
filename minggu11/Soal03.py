file = open("berita.txt", "r")
teks = file.read()
file.close()

kata = teks.split()

unik = list(set(kata))
print("Kata unik:")
print(" ".join(unik))