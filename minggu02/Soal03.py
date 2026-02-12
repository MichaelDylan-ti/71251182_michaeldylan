gaji_perjam = int(input("Masukkan Gajinya Budi: "))
jam_kerja = float(input("Masukkan jam kerja perminggu Budi: "))
minggu = 5

pendapatan_sebelum = gaji_perjam * jam_kerja * minggu

pendapatan_sesudah_pajak = pendapatan_sebelum - ((pendapatan_sebelum * 14) / 100)
uang_pakaian_aksesoris = 0.10 * pendapatan_sesudah_pajak
uang_alattulis = 0.01 * pendapatan_sesudah_pajak
total_pengeluaran = pendapatan_sesudah_pajak - uang_pakaian_aksesoris - uang_alattulis

uang_sedekah = 0.25 * total_pengeluaran
uang_anakyatim = 0.30 * uang_sedekah
uang_kaumdhuafa = uang_sedekah - uang_anakyatim

print("Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak: ", pendapatan_sebelum)
print("Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak: ", pendapatan_sesudah_pajak)
print("Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: ", uang_pakaian_aksesoris)
print("Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: ", uang_alattulis)
print("Jumlah uang yang akan Budi sedekahkan: ", uang_sedekah)
print("Jumlah uang yang akan diterima anak yatim: ", uang_anakyatim)
print("Jumlah uang yang akan diterima kaum dhuafa", uang_kaumdhuafa)