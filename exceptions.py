class PerpustakaanError(Exception):
    """Exception dasar untuk sistem perpustakaan."""
    pass


class InvalidLoanLimitError(PerpustakaanError):
    def __init__(self, nilai):
        self.nilai = nilai
        super().__init__(
            f"Batas pinjam harus lebih dari 0. Nilai yang diberikan: {nilai}"
        )


class ExtensionLimitExceededError(PerpustakaanError):
    def __init__(self, nama, batas):
        self.nama = nama
        self.batas = batas
        super().__init__(
            f"{nama} sudah mencapai batas maksimal perpanjangan ({batas} kali)."
        )


class InvalidLateDaysError(PerpustakaanError):
    def __init__(self, terlambat):
        self.terlambat = terlambat
        super().__init__(
            f"Jumlah hari keterlambatan tidak boleh negatif. "
            f"Nilai yang diberikan: {terlambat}"
        )