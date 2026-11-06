
from layanan_perpustakaan import LayananPerpustakaan
from denda import Denda


class Pengembalian(LayananPerpustakaan):
    def __init__(self, id_pengembalian, tanggal_pengembalian, kondisi_buku, anggota, buku=None):
        self.id_pengembalian = id_pengembalian
        self.tanggal_pengembalian = tanggal_pengembalian
        self.kondisi_buku = kondisi_buku
        # ASSOCIATION: anggota dikirim dari luar
        self.anggota = anggota
        # Buku dikirim dari luar agar status buku bisa diperbarui saat dikembalikan
        self.buku = buku
        # COMPOSITION: objek Denda dibuat DI DALAM constructor Pengembalian.
        # Denda adalah "bagian dari" Pengembalian, jadi lahir bersamanya dan
        # ikut hilang kalau Pengembalian-nya dihapus.
        # Awalnya jumlah 0 (artinya belum ada denda); diisi nanti lewat hitungDenda().
        self.denda = Denda(id_pengembalian, 0, "Tidak ada denda", tanggal_pengembalian)
    
    # polymorpism pengembalian
    def proses(self):
        print("Memproses pengembalian:", self.id_pengembalian)

        # VALIDASI: jika buku diberikan, buku harus sedang dipinjam
        if self.buku is not None:
            if self.buku.cekStatus() != "Dipinjam":
                raise ValueError("Buku tidak sedang dalam status dipinjam")

            # VALIDASI: anggota harus memiliki peminjaman aktif
            if self.anggota.jumlah_pinjam <= 0:
                raise ValueError("Anggota tidak memiliki peminjaman aktif")

            # Jika validasi lolos, buku dikembalikan dan jumlah pinjaman berkurang
            self.buku.ubahStatus("Tersedia")
            self.anggota.jumlah_pinjam -= 1

        print("Tanggal pengembalian:", self.tanggal_pengembalian)
        print("Kondisi buku:", self.kondisi_buku)
        print("Dikembalikan oleh:", self.anggota.nama)

        if self.buku is not None:
            print("Buku:", self.buku.judul)
            print("Status buku:", self.buku.cekStatus())
            print("Jumlah pinjaman anggota:", self.anggota.jumlah_pinjam)

        print("Pengembalian berhasil!")