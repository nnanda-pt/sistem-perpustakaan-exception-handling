from layanan_perpustakaan import LayananPerpustakaan
from exceptions import BookNotAvailableError, LoanLimitExceededError


class Peminjaman(LayananPerpustakaan):
    def __init__(self, id_peminjaman, tanggal_pinjam, tanggal_kembali, denda, anggota, buku):
        self.id_peminjaman = id_peminjaman
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.denda = denda
        self.anggota = anggota
        self.buku = buku

    def proses(self):
        print("Memproses peminjaman:", self.id_peminjaman)

        # Validasi ketersediaan buku
        if self.buku.cekStatus() != "Tersedia":
            raise BookNotAvailableError(
                self.buku.judul,
                self.buku.cekStatus()
            )

        # Validasi batas peminjaman anggota
        if not self.anggota.cekBatasPinjam():
            raise LoanLimitExceededError(
                self.anggota.nama,
                self.anggota.batas_pinjam
            )

        # Proses peminjaman jika seluruh validasi berhasil
        self.buku.ubahStatus("Dipinjam")
        self.anggota.jumlah_pinjam += 1

        print("Peminjaman berhasil!")
        print("Peminjam:", self.anggota.nama)
        print("Buku:", self.buku.judul)
        print("Tanggal pinjam:", self.tanggal_pinjam)
        print("Tanggal kembali:", self.tanggal_kembali)
        print("Jumlah pinjaman anggota:", self.anggota.jumlah_pinjam)
