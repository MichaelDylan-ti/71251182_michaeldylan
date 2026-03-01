inputuser = input("Masukkan bulan (1-12): ")
try:
    bulan = int(inputuser)
    if bulan < 1 or bulan > 12:
        print("Bulan tidak valid.")
    elif bulan == 2:
        print("Jumlah hari: 29")
    elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
        print("Jumlah hari: 30")
    else:
        print("Jumlah hari: 31")
except:
    print("Bulan tidak valid.")