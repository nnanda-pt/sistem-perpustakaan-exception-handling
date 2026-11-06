
from buku import Buku, BukuCetak, EBook, Jurnal
from anggota import Mahasiswa, Dosen
from peminjaman import Peminjaman
from pengembalian import Pengembalian
from denda import Denda
from exceptions import (
    PerpustakaanError,
    InvalidLoanLimitError,
    LoanLimitExceededError,
    BookNotAvailableError,
    ExtensionLimitExceededError
)


# POLYMORPHISM lewat abstract: fungsi ini menerima layanan apa saja
# (Peminjaman atau Pengembalian), karena semuanya pasti punya proses().
def jalankan_layanan(layanan):
    layanan.proses()


# EAFP (Easier to Ask Forgiveness than Permission):
# Langsung mencoba mengambil buku berdasarkan ID.
# Jika ID tidak ditemukan, KeyError ditangkap dan diubah menjadi
# custom exception PerpustakaanError.
def cari_buku(daftar_buku, id_buku):
    buku_berdasarkan_id = {
        buku.id_buku: buku for buku in daftar_buku
    }

    try:
        return buku_berdasarkan_id[id_buku]
    except KeyError as error:
        raise PerpustakaanError(
            f"Buku dengan ID {id_buku} tidak ditemukan."
        ) from error


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
    print("\n=== SEMUA BUKU ===")
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

    # ===== 5. UJI EAFP DAN RAISE FROM =====
    print("\n=== UJI PENCARIAN BUKU (EAFP) ===")

    # Skenario berhasil: buku dengan ID 1 ditemukan
    try:
        hasil_buku = cari_buku(daftar_buku, 1)
        print("Buku ditemukan:", hasil_buku)

    except PerpustakaanError as e:
        print("Pencarian gagal:", e)

    else:
        print("Pencarian buku berhasil!")

    finally:
        print("Proses pencarian pertama selesai.")

    # Skenario gagal: buku dengan ID 99 tidak ditemukan
    try:
        hasil_buku = cari_buku(daftar_buku, 99)
        print("Buku ditemukan:", hasil_buku)

    except PerpustakaanError as e:
        print("Pencarian gagal:", e)
        print("Penyebab asli:", e.__cause__)

    finally:
        print("Proses pencarian kedua selesai.")

    # ===== 6. SKENARIO PEMINJAMAN BERHASIL (ASSOCIATION) =====
    # Anggota dan Buku dibuat di luar, lalu dikirim ke Peminjaman.
    # Validasi dilakukan sebelum status buku dan jumlah pinjaman diperbarui.
    print("\n=== PEMINJAMAN BERHASIL ===")

    pinjam1 = Peminjaman(
        1, "05-11-2026", "12-11-2026", 0, mhs1, buku1
    )

    try:
        jalankan_layanan(pinjam1)

    except BookNotAvailableError as e:
        print("Peminjaman ditolak:", e)

    except LoanLimitExceededError as e:
        print("Peminjaman ditolak:", e)

    except PerpustakaanError as e:
        print("Terjadi kesalahan perpustakaan:", e)

    except Exception as e:
        print("Terjadi kesalahan umum:", e)

    else:
        print("Transaksi peminjaman berhasil diproses.")

    finally:
        print("Proses peminjaman pertama selesai.")
        print("Status buku:", buku1.cekStatus())
        print("Jumlah pinjaman anggota:", mhs1.jumlah_pinjam)

    # ===== 7. SKENARIO PEMINJAMAN GAGAL: BUKU TIDAK TERSEDIA =====
    print("\n=== PEMINJAMAN GAGAL: BUKU TIDAK TERSEDIA ===")

    # Mengubah status buku menjadi Dipinjam untuk simulasi
    buku2.updateStatus("Dipinjam")

    pinjam2 = Peminjaman(
        2, "05-11-2026", "12-11-2026", 0, mhs1, buku2
    )

    try:
        jalankan_layanan(pinjam2)

    except BookNotAvailableError as e:
        print("Peminjaman ditolak:", e)

    except PerpustakaanError as e:
        print("Terjadi kesalahan perpustakaan:", e)

    except Exception as e:
        print("Terjadi kesalahan umum:", e)

    else:
        print("Transaksi peminjaman berhasil.")

    finally:
        print("Proses peminjaman kedua selesai.")
        print("Status buku:", buku2.cekStatus())

    # ===== 8. SKENARIO PEMINJAMAN GAGAL: BATAS PINJAMAN =====
    print("\n=== PEMINJAMAN GAGAL: BATAS PINJAMAN ===")

    # Membuat anggota dengan batas pinjam 1 buku
    mhs3 = Mahasiswa(
        4, "Rina", "230103", "Sistem Informasi", batas_pinjam=1
    )

    # Jumlah pinjaman sudah sama dengan batas maksimal
    mhs3.jumlah_pinjam = 1

    pinjam3 = Peminjaman(
        3, "05-11-2026", "12-11-2026", 0, mhs3, buku3
    )

    try:
        jalankan_layanan(pinjam3)

    except BookNotAvailableError as e:
        print("Peminjaman ditolak:", e)

    except LoanLimitExceededError as e:
        print("Peminjaman ditolak:", e)

    except PerpustakaanError as e:
        print("Terjadi kesalahan perpustakaan:", e)

    except Exception as e:
        print("Terjadi kesalahan umum:", e)

    else:
        print("Transaksi peminjaman berhasil.")

    finally:
        print("Proses peminjaman ketiga selesai.")
        print("Status buku:", buku3.cekStatus())
        print("Jumlah pinjaman Rina:", mhs3.jumlah_pinjam)

    # ===== 9. ENCAPSULATION: UJI VALIDASI SETTER =====
    print("\n=== UJI VALIDASI SETTER ===")

    # VALIDASI: batas pinjam tidak boleh 0 atau negatif
    try:
        mhs1.batas_pinjam = 0

    except InvalidLoanLimitError as e:
        print("Validasi gagal:", e)

    except PerpustakaanError as e:
        print("Kesalahan perpustakaan:", e)

    else:
        print("Batas pinjam berhasil diubah.")

    finally:
        print("Batas pinjam saat ini:", mhs1.batas_pinjam)

    # STATICMETHOD dipanggil lewat nama class, tanpa objek
    print("\n=== UJI STATICMETHOD ===")
    print(Denda.validasiJumlah(5000))   # True
    print(Denda.validasiJumlah(-1))     # False

    # ===== 10. MIXIN DAN MRO =====
    print("\n=== UJI MIXIN ===")

    # Dua kali perpanjangan berhasil, percobaan ketiga ditolak
    try:
        mhs1.perpanjangPinjaman()
        mhs1.perpanjangPinjaman()
        mhs1.perpanjangPinjaman()

    except ExtensionLimitExceededError as e:
        print("Perpanjangan ditolak:", e)

    except PerpustakaanError as e:
        print("Kesalahan perpustakaan:", e)

    else:
        print("Semua perpanjangan berhasil.")

    finally:
        print("Proses perpanjangan selesai.")

    # Mixin yang sama juga digunakan oleh Dosen
    print("\nPerpanjangan oleh dosen:")
    dosen1.perpanjangPinjaman()

    print("\n=== UJI MRO ===")
    print([k.__name__ for k in Mahasiswa.mro()])

    # ===== 11. SKENARIO PENGEMBALIAN DAN DENDA (COMPOSITION) =====
    # Denda tidak dibuat di sini, tapi lahir di dalam constructor Pengembalian.
    # Buku yang dikembalikan diberikan sebagai parameter agar statusnya diperbarui.
    print("\n=== PENGEMBALIAN BERHASIL ===")

    kembali1 = Pengembalian(
        1, "06-11-2026", "Aman", mhs1, buku1
    )

    try:
        jalankan_layanan(kembali1)

    except ValueError as e:
        print("Pengembalian ditolak:", e)

    except Exception as e:
        print("Terjadi kesalahan umum:", e)

    else:
        print("Transaksi pengembalian berhasil diproses.")

    finally:
        print("Proses pengembalian selesai.")
        print("Status buku:", buku1.cekStatus())
        print("Jumlah pinjaman anggota:", mhs1.jumlah_pinjam)

    # ===== 12. UJI DENDA =====
    print("\n=== UJI DENDA ===")

    denda1 = kembali1.denda

    print("Denda awal:", denda1.jumlah)
    print("Denda milik pengembalian ini:", denda1 is kembali1.denda)

    terlambat = 2
    denda1.alasan = "Terlambat 2 hari"

    try:
        denda1.hitungDenda(terlambat)

    except ValueError as e:
        print("Perhitungan denda gagal:", e)

    else:
        print("Perhitungan denda berhasil.")

    finally:
        print("Jumlah denda:", denda1.jumlah)

    print("Alasan Denda:", denda1.alasan)

    # VALIDASI: jumlah denda tidak boleh negatif
    try:
        denda1.jumlah = -500

    except ValueError as e:
        print("Validasi denda gagal:", e)

    else:
        print("Jumlah denda berhasil diubah.")

    finally:
        print("Jumlah denda saat ini:", denda1.jumlah)

    # ===== 13. UJI ASSOCIATION =====
    # Setelah Peminjaman dihapus, Anggota dan Buku tetap ada.
    print("\n=== UJI ASSOCIATION ===")

    del pinjam1

    print("Anggota masih ada:", mhs1.nama)
    print("Buku masih ada:", buku1.judul)

    # ===== 14. STATUS AKHIR SISTEM =====
    print("\n=== STATUS AKHIR SISTEM ===")
    print("Jumlah buku:", Buku.jumlah_buku)
    print("Status buku 1:", buku1.cekStatus())
    print("Status buku 2:", buku2.cekStatus())
    print("Status buku 3:", buku3.cekStatus())
    print("Jumlah pinjaman Budi:", mhs1.jumlah_pinjam)

    print("\n=== PROGRAM SELESAI ===")
