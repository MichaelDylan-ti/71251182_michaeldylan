def perkalian(a, b):
    hasil = 0
    bentuk = ""
    for i in range(a):
        hasil = hasil + b
        bentuk = bentuk + str(b)
        if i < a-1:
            bentuk = bentuk + " + "
    print(a, "x", b, "=", bentuk, "=", hasil)

perkalian(6,5)
perkalian(7,10)