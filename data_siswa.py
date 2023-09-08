class contact:
    def __init__(self, nama, nomor_telepon, email):
        self.nama = nama 
        self.nomor_telepon= nomor_telepon
        self.email = email 
    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Nomor telepon: {self.nomor_telepon}")
        print(f"Email : {self.email}")
        print()

class AndressBook:
    def __init__(self):
        self.daftar_kontak = []
    
    def tambah_kontak(self, kontak):
        self.daftar_kontak.append(kontak)
    
    def tampilkan_semua_kontak(self):
        print("daftar_kontak: ")
        for kontak in self.daftar_kontak:
            kontak.tampilkan_info()

if __name__ == "__main__":
    andress_book = AndressBook()

    while True:
        print("Menu : ")
        print("1. Tambah kontak")
        print("2. Tampilkan semua kontak ")
        print("3. keluar ")

        pilihan = input("pilih menu(1/2/3):")

        if pilihan == "1":
            nama = input("nama:")
            nomor_telepon= input("Nomor telepon:")
            email = input("email: ")
            kontak_baru = contact(nama, nomor_telepon, email)
            andress_book.tambah_kontak(kontak_baru)
        elif pilihan == "2":
            andress_book.tampilkan_semua_kontak()
        elif pilihan == "3":
            break
        else:
            print("pilihan tidak valid. silahkan pilih menu yang benar")