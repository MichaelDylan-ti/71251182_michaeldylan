nama_file1 = input("Masukkan nama file pertama: ")
nama_file2 = input("Masukkan nama file kedua: ")

try:
    file1 = open(nama_file1, 'r')
    file2 = open(nama_file2, 'r')
    isi_file1 = file1.read().lower().split()
    isi_file2 = file2.read().lower().split()
    file1.close()
    file2.close()
    set_file1 = set(isi_file1)
    set_file2 = set(isi_file2)
except:
    print("Error: File", nama_file1, "tidak ditemukan/tidak bisa dibaca!")
    exit()
    print("Error: File", nama_file2, "tidak ditemukan/tidak bisa dibaca!")
    exit()

# Tampilkan kata-kata di setiap file
print("\nKata-kata di", nama_file1, ":", set_file1)
print("Kata-kata di", nama_file2, ":", set_file2)

# Tampilkan kata yang muncul di KEDUA file (intersection)
kata_sama = set_file1.intersection(set_file2)
print("\nKata-kata yang muncul di kedua file:", kata_sama)