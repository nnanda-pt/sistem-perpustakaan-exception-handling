from layanan_perpustakaan import LayananPerpustakaan
from denda import Denda
class Pengembalian(LayananPerpustakaan):
    def __init__(self, id_pengembalian, tanggal_pengembalian, kondisi_buku, anggota):
        self.id_pengembalian = id_pengembalian
        self.tanggal_pengembalian = tanggal_pengembalian
        self.kondisi_buku = kondisi_buku
        # ASSOCIATION: anggota dikirim dari luar
        self.anggota = anggota
        # COMPOSITION: objek Denda dibuat DI DALAM constructor Pengembalian.
        # Denda adalah "bagian dari" Pengembalian, jadi lahir bersamanya dan
        # ikut hilang kalau Pengembalian-nya dihapus.
        # Awalnya jumlah 0 (artinya belum ada denda); diisi nanti lewat hitungDenda().
        self.denda = Denda(id_pengembalian, 0, "Tidak ada denda", tanggal_pengembalian)
    
    # polymorpism pengembalian
    def proses(self):
        print("Memproses pengembalian:", self.id_pengembalian)
        print("Tanggal pengembalian:", self.tanggal_pengembalian)
        print("Kondisi buku:", self.kondisi_buku)
        print("Dikembalikan oleh:", self.anggota.nama)
        
    