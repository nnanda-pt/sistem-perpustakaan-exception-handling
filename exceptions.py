
class PerpustakaanError(Exception):
    """Base exception untuk sistem perpustakaan."""

    def __init__(self, pesan):
        self.pesan = pesan
        super().__init__(pesan)


class InvalidLoanLimitError(PerpustakaanError):
    def __init__(self, batas_pinjam):
        self.batas_pinjam = batas_pinjam
        super().__init__(
            f"Batas pinjam harus lebih dari 0. Nilai: {batas_pinjam}"
        )


class LoanLimitExceededError(PerpustakaanError):
    def __init__(self, nama, batas_pinjam):
        self.nama = nama
        self.batas_pinjam = batas_pinjam
        super().__init__(
            f"{nama} sudah mencapai batas maksimal peminjaman "
            f"({batas_pinjam} buku)."
        )


class BookNotAvailableError(PerpustakaanError):
    def __init__(self, judul, status):
        self.judul = judul
        self.status = status
        super().__init__(
            f"Buku '{judul}' tidak tersedia untuk dipinjam. Status: {status}."
        )


class ExtensionLimitExceededError(PerpustakaanError):
    def __init__(self, nama, maksimal):
        self.nama = nama
        self.maksimal = maksimal
        super().__init__(
            f"{nama} sudah mencapai batas maksimal perpanjangan "
            f"({maksimal} kali)."
        )
