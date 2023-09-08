nama = str(input("Masukan nama:"))
Gaji_pokok = float(input("Masukan Gaji pokok:"))

tunjangan = 0.02 * Gaji_pokok
pajak = 0.15 * (Gaji_pokok + tunjangan)
Gaji_Bersih = Gaji_pokok + tunjangan - pajak
print(nama)
print(Gaji_pokok)
print(Gaji_Bersih)