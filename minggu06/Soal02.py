def ganjil(bawah, atas):
    if bawah < atas:
        print("bawah =",bawah,",atas =",atas, ". Karena bawah < atas, berarti dari kecil ke besar, maka hasilnya adalah:", end=" ")
        for i in range(bawah, atas + 1):
            if i % 2 != 0:
                print(i, end=" ")
    elif bawah > atas:
        print("bawah = ", bawah,",atas = ",atas, ". Karena bawah > atas, berarti dari besar ke kecil, maka hasilnya adalah:", end=" ")
        for i in range(bawah, atas - 1, -1):
            if i % 2 != 0:
                print(i, end=" ")

bawah = int(input("Bawah = "))
atas = int(input("Atas = "))
ganjil(bawah, atas)