def tiga_terbaik(data):
    data_unik = list(set(data))   
    data_unik.sort(reverse=True) 
    return data_unik[:3]         

angka = input("Masukkan angka (pisah dengan spasi): ")
list_angka = [int(x) for x in angka.split()]

hasil = tiga_terbaik(list_angka)
print("3 bilangan terbaik:", hasil)