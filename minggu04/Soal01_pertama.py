inputuser = input("Masukkan suhu tubuh: ")

try:
    suhu = int(inputuser)
    if suhu >= 38:
        print("Anda demam")
    else:
        print("Anda tidak demam")
except:
    print("Anda salah memasukkan input")