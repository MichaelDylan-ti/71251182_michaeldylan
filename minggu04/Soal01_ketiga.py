inputpertama = input("Masukkan bilangan pertama: ")
inputkedua = input("Masukkan bilangan kedua: ")
inputketiga = input("Masukkan bilangan ketiga: ")

try:
    a = int(inputpertama)
    b = int(inputkedua)
    c = int(inputketiga)
    if a > b and a > c:
        print("Terbesar: ", a)
    elif b > a and b > c:
        print("Terbesar: ", b)
    elif c > a and c > b:
        print("Terbesar: ", c)
except:
    print("Masukkan angka integer MAS!!!")