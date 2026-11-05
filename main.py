from buku import Buku, BukuCetak, EBook, Jurnal
from anggota import Mahasiswa, Dosen
from peminjaman import Peminjaman
from pengembalian import Pengembalian
from denda import Denda


# POLYMORPHISM lewat abstract: fungsi ini menerima layanan apa saja
# (Peminjaman atau Pengembalian), karena semuanya pasti punya proses().
def jalankan_layanan(layanan):
    layanan.proses()


if __name__ == "__main__":

    # ===== 1. MEMBUAT OBJEK ANGGOTA DAN BUKU (data hardcode/statis) =====
    mhs1 = Mahasiswa(1, "Budi", "230101", "Sistem Informasi")
    dosen1 = Dosen(2, "Pak Andi", "0012345", "Lektor")

    buku1 = Buku(1, "Pemrograman Python", "Andi", 2006)
    buku2 = BukuCetak(2, "Belajar OOP Python", "Budi", 2025, "978-1234567890", 250)
    buku3 = EBook(3, "Python Digital", "Citra", 2025, "5 MB", "PDF")
    buku4 = Jurnal(4, "Artificial Intelligence", "Dewi", 2025, 2, 1,
                   "Penelitian tentang penerapan AI.")

    # ===== 2. INHERITANCE + OVERRIDE + POLYMORPHISM =====
    # Satu perintah b.tampilkanInfo(), hasilnya beda tergantung jenis objeknya.
    print("=== SEMUA BUKU ===")
    daftar_buku = [buku1, buku2, buku3, buku4]
    for b in daftar_buku:
        print("-----")
        b.tampilkanInfo()

    # Method khas masing-masing subclass
    print("\n=== METHOD KHAS SUBCLASS ===")
    buku3.download()
    buku4.lihatAbstrak()
    buku4.aksesFullText()

    # ===== 3. DUNDER METHOD + CLASS ATTRIBUTE =====
    print("\n=== UJI DUNDER ===")
    print(buku2)                              # memanggil __str__
    print("Jumlah buku:", Buku.jumlah_buku)   # class attribute

    # Objek berbeda tapi id_buku sama dengan buku2
    buku_sama = BukuCetak(2, "Judul Lain", "Penulis Lain", 2020, "111", 100)
    print(buku2 == buku_sama)                 # memanggil __eq__ -> True
    print(buku2 == buku3)                     # id berbeda -> False

    # ===== 4. CLASSMETHOD (alternative constructor) =====
    print("\n=== UJI CLASSMETHOD ===")
    mhs2 = Mahasiswa.dariString("3,Sari,230102,Sistem Informasi")
    mhs2.lihatStatusPinjaman()

    # ===== 5. SKENARIO PEMINJAMAN (ASSOCIATION) =====
    # Anggota dan Buku dibuat di luar, lalu dikirim ke Peminjaman
    print("\n=== PEMINJAMAN ===")
    pinjam1 = Peminjaman(1, "11-10-2026", "18-10-2026", 0, mhs1, buku2)
    buku2.updateStatus("Dipinjam")
    jalankan_layanan(pinjam1)
    print("Status buku:", buku2.cekStatus())

    # ===== 6. SKENARIO PENGEMBALIAN DAN DENDA (COMPOSITION) =====
    # Denda tidak dibuat di sini, tapi lahir di dalam constructor Pengembalian
    print("\n=== PENGEMBALIAN ===")
    kembali1 = Pengembalian(1, "20-10-2026", "Aman", mhs1)
    jalankan_layanan(kembali1)
    buku2.updateStatus("Tersedia")

    print("\n=== DENDA ===")
    denda1 = kembali1.denda
    print("Denda awal:", denda1.jumlah)
    print("Denda milik pengembalian ini:", denda1 is kembali1.denda)
    terlambat = 2
    denda1.alasan = "Terlambat 2 hari"
    denda1.hitungDenda(terlambat)
    print("Alasan Denda:", denda1.alasan)

    # ===== 7. ENCAPSULATION: UJI VALIDASI SETTER =====
    print("\n=== UJI VALIDASI SETTER ===")
    try:
        mhs1.batas_pinjam = 0
    except ValueError as e:
        print("Ditolak:", e)
    print("Batas pinjam tetap:", mhs1.batas_pinjam)

    try:
        denda1.jumlah = -500
    except ValueError as e:
        print("Ditolak:", e)
    print("Jumlah denda tetap:", denda1.jumlah)

    # STATICMETHOD dipanggil lewat nama class, tanpa objek
    print(Denda.validasiJumlah(5000))   # True
    print(Denda.validasiJumlah(-1))     # False

    # ===== 8. MIXIN DAN MRO =====
    print("\n=== UJI MIXIN ===")
    print(mhs1.perpanjangPinjaman())
    print(mhs1.perpanjangPinjaman())
    print(mhs1.perpanjangPinjaman())    # sudah melewati batas (maksimal 2)
    print(dosen1.perpanjangPinjaman())  # mixin yang sama dipakai Dosen

    print("\n=== UJI MRO ===")
    print([k.__name__ for k in Mahasiswa.mro()])

    # ===== 9. UJI ASSOCIATION: taruh PALING AKHIR =====
    # Setelah Peminjaman dihapus, Anggota dan Buku tetap ada
    print("\n=== UJI ASSOCIATION ===")
    del pinjam1
    print("Anggota masih ada:", mhs1.nama)
    print("Buku masih ada:", buku2.judul)