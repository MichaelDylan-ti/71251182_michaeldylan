n = int(input("Masukkan n: "))

for i in range(n-1, 1, -1):
    prima = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            prima = False
            break
    if prima:
        print(f"Prima terdekat < {n} adalah {i}")
        break