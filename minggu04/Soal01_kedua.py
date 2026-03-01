inputuser = input("Masukkan suatu bilangan: ")

try:
    bilangan = int(inputuser)
    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    elif bilangan == 0:
        print("Nol")
except:
    print("Salah input mas, Masukkan angka bilangan integer!")