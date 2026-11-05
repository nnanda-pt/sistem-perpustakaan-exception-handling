
from layanan_perpustakaan import LayananPerpustakaan

class Peminjaman(LayananPerpustakaan):
    def __init__(self, id_peminjaman, tanggal_pinjam, tanggal_kembali, denda, anggota, buku):
        self.id_peminjaman = id_peminjaman
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.denda = denda
        # ASSOCIATION: objek Anggota dan Buku sudah ada lebih dulu,
        # dikirim dari luar (bukan dibuat di sini seperti Denda di Pengembalian).
        # Peminjaman hanya "mengenal" keduanya.
        self.anggota = anggota
        self.buku = buku

    # Implementasi abstract method
    # polymorpism peminjaman
    def proses(self):
        print("Memproses peminjaman:", self.id_peminjaman)
        print("Peminjam:", self.anggota.nama)
        print("Buku:", self.buku.judul)
        print("Tanggal pinjam:", self.tanggal_pinjam)
        print("Tanggal kembali:", self.tanggal_kembali)
        
  