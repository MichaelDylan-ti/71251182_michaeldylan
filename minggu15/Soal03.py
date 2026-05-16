def suku(n):
    return (2 ** n) - 1

def deret_ganjil(n):
    if n == 1:
        return 1
    return suku(n) + deret_ganjil(n - 1)

def tampilkan_deret(n):
    if n == 1:
        print(suku(1), end="")
    else:
        tampilkan_deret(n - 1)
        print(f" + {suku(n)}", end="")

n = int(input("Masukkan jumlah suku (n): "))
print("Deret  : ", end="")
tampilkan_deret(n)
print(f"\nJumlah : {deret_ganjil(n)}")