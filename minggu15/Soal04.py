def jumlah_digit(n):
    if n == 0:
        return 0
    return (n % 10) + jumlah_digit(n // 10)

def tampilkan_digit(n):
    if n < 10:
        print(n, end="")
    else:
        tampilkan_digit(n // 10)
        print(" +", n % 10, end="")

bilangan = int(input("Masukkan bilangan : "))
print("Jumlah digit dari", bilangan, ":", end=" ")
tampilkan_digit(bilangan)
print(" =", jumlah_digit(bilangan))