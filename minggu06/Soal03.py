print("Program penghitung IPS Mahasiswa")

jumlah_matkul = int(input("Berapa jumlah mata kuliah? "))
total_bobotIPS = 0

for i in range(1,jumlah_matkul + 1):
    nilai = input(f"Nilai MK {i} : ").upper()

    if nilai == "A":
        bobot = 4
    elif nilai == "B":
        bobot = 3
    elif nilai == "C":
        bobot = 2
    elif nilai == "D":
        bobot = 1
    else:
        bobot = 0
    total_bobotIPS= total_bobotIPS + (bobot * 3)

ips = total_bobotIPS / (jumlah_matkul * 3)
print(f"Nilai IPS anda Semester ini {ips:.2f}")