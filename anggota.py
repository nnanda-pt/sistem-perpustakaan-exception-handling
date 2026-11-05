from exceptions import InvalidLoanLimitError, ExtensionLimitExceededError


class Anggota:
    # Mengubah parameter di class anggota menjadi objek
    def __init__(self, id_anggota, nama, jenis_anggota, batas_pinjam, jumlah_pinjam = 0):
        self.id_anggota = id_anggota
        self.nama = nama
        self.jenis_anggota = jenis_anggota
        self.batas_pinjam = batas_pinjam
        self.jumlah_pinjam = jumlah_pinjam
        
    # Method untuk mengecek batas pinjam di class anggota
    def cekBatasPinjam(self):
        # True jika anggota masih boleh meminjam, False jika sudah mencapai batas
        return self.jumlah_pinjam < self.batas_pinjam
    
    # ENCAPSULATION: data aslinya disimpan di atribut private __batas_pinjam,
    # dibaca lewat @property dan diubah lewat setter yang memvalidasi
    @property
    def batas_pinjam(self):
        return self.__batas_pinjam

    @batas_pinjam.setter
    def batas_pinjam(self, nilai):
        # VALIDASI: batas pinjam harus lebih dari 0
        if nilai <= 0:
            raise InvalidLoanLimitError(nilai)
        self.__batas_pinjam = nilai

    # @property → membaca data seperti atribut biasa.
    # @batas_pinjam.setter → mengubah data sekaligus menjalankan validasi.
    # self.__batas_pinjam → menyimpan data aslinya secara private.

    # MIXIN: class kecil berisi satu kemampuan (perpanjangan) yang bisa
    # "dititipkan" ke class lain lewat multiple inheritance.
    # Mixin tidak berdiri sendiri, jadi tidak punya __init__ dan tidak dibuat objeknya.
    # Ia memakai atribut milik class yang menumpang (jumlah_perpanjangan,
    # maks_perpanjangan, durasi_perpanjangan, nama).
class PerpanjanganMixin:
    def perpanjangPinjaman(self):
        # VALIDASI: anggota tidak boleh memperpanjang lebih dari batas maksimal
        if self.jumlah_perpanjangan >= self.maks_perpanjangan:
            raise ExtensionLimitExceededError(
                self.nama,
                self.maks_perpanjangan
            )

        self.jumlah_perpanjangan += 1
        print(f"{self.nama} berhasil memperpanjang {self.durasi_perpanjangan} hari "
              f"({self.jumlah_perpanjangan}/{self.maks_perpanjangan})")
        return True
        
# Mahasiswa merupakan child class yang mewarisi class Anggota
class Mahasiswa(PerpanjanganMixin, Anggota):
    def __init__(self, id_anggota, nama, nim, prodi, batas_pinjam=5):
        # Memanggil constructor parent class Anggota
        # untuk menginisialisasi id_anggota dan nama
        super().__init__(id_anggota, nama, "Mahasiswa", batas_pinjam)
        self.nim = nim
        self.prodi = prodi
        # variabel
        self.durasi_pinjam = 7        # durasi peminjaman awal (hari)
        self.jumlah_perpanjangan = 0   # berapa kali sudah diperpanjang
        self.maks_perpanjangan = 2     # batas maksimal perpanjangan
        self.durasi_perpanjangan = 7   # tambahan hari tiap perpanjangan

    # Method untuk melihat status peminjaman
    def lihatStatusPinjaman(self):
        # Atribut id_anggota dan nama berasal dari class Anggota
        print("ID Anggota:", self.id_anggota)
        print("Nama:", self.nama)

        # Atribut berikut berasal dari class Mahasiswa
        print("NIM:", self.nim)
        print("Prodi:", self.prodi)

    # CLASSMETHOD (alternative constructor): cara lain membuat objek Mahasiswa,
    # yaitu dari satu teks "id,nama,nim,prodi" (bukan mengisi satu per satu).
    # Parameter pertamanya cls (class itu sendiri), bukan self (objek).
    @classmethod
    def dariString(cls, data):
        id_anggota, nama, nim, prodi = data.split(",")
        return cls(int(id_anggota), nama, nim, prodi)   # memanggil __init__ biasa
    
# Dosen merupakan child class yang mewarisi class Anggota
class Dosen(PerpanjanganMixin, Anggota):
    def __init__(self, id_anggota, nama, nidn, jabatan, batas_pinjam=3):
        super().__init__(id_anggota, nama, "Dosen", batas_pinjam)
        self.nidn = nidn
        self.jabatan = jabatan
        # Atribut instance untuk menentukan durasi peminjaman Dosen
        self.durasi_pinjam = 14        # durasi peminjaman awal (hari)
        self.jumlah_perpanjangan = 0   # berapa kali sudah diperpanjang
        self.maks_perpanjangan = 2     # batas maksimal perpanjangan
        self.durasi_perpanjangan = 7   # tambahan hari tiap perpanjangan
        
    # Method untuk melihat status peminjaman
    def lihatStatusPinjaman(self):
        # Atribut id_anggota dan nama berasal dari class Anggota
        print("ID Anggota:", self.id_anggota)
        print("Nama:", self.nama)

        # Atribut berikut berasal dari class Mahasiswa
        print("NIDN:", self.nidn)
        print("Jabatan:", self.jabatan)