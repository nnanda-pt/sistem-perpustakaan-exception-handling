class Denda:
    def __init__(self, id_denda, jumlah, alasan, tanggal):
        self.id_denda = id_denda
        self.jumlah = jumlah
        self.alasan = alasan
        self.tanggal = tanggal

    # ENCAPSULATION: menyimpan jumlah denda dalam atribut private
    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, nilai):
        if not Denda.validasiJumlah(nilai):
            raise ValueError("Jumlah denda tidak boleh negatif")
        self.__jumlah = nilai

    # STATICMETHOD: memvalidasi jumlah denda
    @staticmethod
    def validasiJumlah(jumlah):
        return jumlah >= 0

    # Menghitung total denda berdasarkan hari keterlambatan
    def hitungDenda(self, terlambat):
        if terlambat < 0:
            raise ValueError("Jumlah hari keterlambatan tidak boleh negatif")

        self.jumlah = terlambat * 2000
        print("Total denda: Rp", self.jumlah)