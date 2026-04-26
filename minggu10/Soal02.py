filename = input("nama file1: ")
handle = open(filename)

for line in handle:
    line = line.rstrip()
    bagian = line.split("||")
    soal = bagian[0].rstrip()
    jawaban_benar = bagian[1].strip()

    print(soal)
    jawab = input("Jawab: ")

    if jawab.lower() == jawaban_benar.lower():
        print("Jawaban benar!")
    else:
        print("Jawaban salah!")
handle.close()