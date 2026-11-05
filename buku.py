class Buku:
    # CLASS ATTRIBUTE: dimiliki class Buku dan dipakai bersama semua objek.
    # Beda dengan instance attribute (self.judul, dst) yang tiap objek punya sendiri.
    jumlah_buku = 0
    
    def __init__(self, id_buku, judul, penulis, tahun_terbit, status="Tersedia"):
        self.id_buku = id_buku
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        # Encapsulation,  status dibuat sebagai atribut dengan double underscore
        # agar tidak diakses langsung melalui nama atribut biasa dari luar class
        self.__status = status
        # Pakai Buku.jumlah_buku (bukan self.jumlah_buku) supaya penghitung milik class yang bertambah, bukan salinan milik satu objek
        Buku.jumlah_buku += 1

    # Method untuk membaca status buku dari luar class
    def cekStatus(self):
        return self.__status

    # Method untuk mengubah status buku melalui class
    def ubahStatus(self, status):
        self.__status = status

    # Method untuk menampilkan seluruh informasi buku
    def tampilkanInfo(self):
        print("ID Buku:", self.id_buku)
        print("Judul:", self.judul)
        print("Penulis:", self.penulis)
        print("Tahun Terbit:", self.tahun_terbit)
        print("Status:", self.__status)

    # DUNDER METHOD __str__ = cara objek ditampilkan sebagai teks.
    # Harus return string (bukan print)
    def __str__(self):
        return f"[{self.id_buku}] {self.judul} - {self.penulis} ({self.tahun_terbit})"

    # DUNDER METHOD __eq__ = cara objek menentukan apakah mereka sama
    # Dua buku dianggap sama kalau id_buku-nya sama
    def __eq__(self, other):
        return isinstance(other, Buku) and self.id_buku == other.id_buku


# Buku Cetak yang merupakan child class dari buku
class BukuCetak(Buku):
    def __init__(self, id_buku, judul, penulis, tahun_terbit, isbn, jumlah_halaman, status="Tersedia"):
        # super ini digunakan untuk memanggil parameter di class buku
        super().__init__(
            id_buku, judul, penulis, tahun_terbit, status
        )
        self.isbn = isbn
        self.jumlah_halaman = jumlah_halaman

    # # method get detail fisik untuk buku cetak
    def getDetailFisik(self):
        print("ISBN: ", self.isbn)
        print("Jumlah Halaman: ", self.jumlah_halaman)
    
    # # method update status untuk buku cetak
    def updateStatus(self, status):
        self.ubahStatus(status)
        print("Status buku cetak berhasil diubah menjadi: ", status)

    # OVERRIDE: menimpa tampilkanInfo() milik Buku dengan versi BukuCetak
    # (nama method sama, tapi isinya ditambah data khas buku cetak)
    def tampilkanInfo(self):
        super().tampilkanInfo()   # panggil versi Buku dulu (ID, judul, penulis, dst)
        print("ISBN:", self.isbn)
        print("Jumlah Halaman:", self.jumlah_halaman)
    

# Buku elektronik yang merupakan child class dari buku
class EBook(Buku):
    def __init__(self, id_buku, judul, penulis, tahun_terbit, ukuranFile, format, status="Tersedia"):
        super().__init__(
            id_buku, judul, penulis, tahun_terbit, status
        )
        self.ukuranFile = ukuranFile
        self.format = format

    # method download
    def download(self):
        print("Mengunduh e-book:", self.judul)
        print("Format file:", self.format)
        print("Ukuran file:", self.ukuranFile)
        print("E-book berhasil diunduh (simulasi).")
    
    # method get ukuran
    def getUkuran(self):   
        return self.ukuranFile

    # OVERRIDE: menimpa tampilkanInfo() milik Buku dengan versi BukuCetak
    # (nama method sama, tapi isinya ditambah data khas buku cetak)
    def tampilkanInfo(self):
        super().tampilkanInfo()   # panggil versi Buku dulu (ID, judul, penulis, dst)
        print("Ukuran File:", self.ukuranFile)
        print("Format:", self.format)

# Jurnal merupakan child class dari buku
class Jurnal(Buku):
    def __init__(self, id_buku, judul, penulis, tahun_terbit, volume, edisi, abstrak="", status="Tersedia"):
        super().__init__(
            id_buku, judul, penulis, tahun_terbit, status
        )
        self.volume = volume
        self.edisi = edisi
        # variable abstrak buat di method lihatAbstrak()
        self.abstrak = abstrak
    
    # # method lihat abstrak
    def lihatAbstrak(self):
        print("Abstrak Jurnal:")
        print(self.abstrak)
        
    # # method aksesFullText
    def aksesFullText(self):
        if self.cekStatus() == "Tersedia":
            print("Akses teks lengkap jurnal:", self.judul)
            print("Full text berhasil diakses (simulasi).")
        else:
            print("Jurnal tidak tersedia untuk diakses.")
    
    # OVERRIDE: tampilkanInfo() versi Jurnal, menambah volume dan edisi
    def tampilkanInfo(self):
        super().tampilkanInfo()   # info umum dari class Buku
        print("Volume:", self.volume)
        print("Edisi:", self.edisi)