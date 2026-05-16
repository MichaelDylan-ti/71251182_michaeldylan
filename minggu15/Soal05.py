def kombinasi(n, r):
    if r == 0:
        return 1
    
    if r == n:
        return 1
    return kombinasi(n-1, r-1) + kombinasi(n-1, r)

n = int(input("Masukkan nilai n : "))
r = int(input("Masukkan nilai r : "))

if r > n:
    print("Nilai r tidak boleh lebih besar dari n!")
else:
    print("C(", n, ",", r, ") =", kombinasi(n, r))