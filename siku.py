
jumlah_baris = int(input("Masukan jumlah baris:"))


for baris in range(1, jumlah_baris + 1):

    for bintang in range(1, baris + 1):
        print("*", end=" ")

    print()
