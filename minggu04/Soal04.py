input_userpertama = input("Masukkan sisi 1:")
input_userkedua = input("Masukkan sisi 2:")
input_userketiga = input("Masukkan sisi 3:")

try:
    sisi1 = float(input_userpertama)
    sisi2 = float(input_userkedua)
    sisi3 = float(input_userketiga)
    if sisi1 <= 0 or sisi2 <= 0 or sisi3 <= 0:
        print("Input tidak valid.")
    elif sisi1 == sisi2 == sisi3:
        print("3 sisi sama")
    elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
        print("2 sisi sama")
    else:
        print("Tidak ada yang sama")
except:
    print("Input tidak valid.")