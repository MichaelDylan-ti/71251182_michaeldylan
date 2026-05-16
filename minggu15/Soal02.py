def cek_palindrom(kalimat):
    kalimat = kalimat.replace(" ", "").lower()
    def rekursif(s):
        if len(s) <= 1:
            return True
        
        if s[0] != s[-1]:
            return False
        return rekursif(s[1:-1])
    return rekursif(kalimat)

kalimat = input("Masukkan kata/kalimat: ")

if cek_palindrom(kalimat):
    print(f'"{kalimat}" adalah PALINDROM')
else:
    print(f'"{kalimat}" bukan palindrom')