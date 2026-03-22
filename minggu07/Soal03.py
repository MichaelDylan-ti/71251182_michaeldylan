n1 = int(input("Masukkan tinggi = "))
n2 = int(input("Masukkan lebar = "))
angka = 1

for i in range(n1):
    for j in range(n2):
        print(angka, end=" ")
        angka += 1
    print()