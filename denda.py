class Denda:
    def __init__(self, id_denda, jumlah, alasan, tanggal):
        self.id_denda = id_denda
        self.jumlah = jumlah
        self.alasan = alasan
        self.tanggal = tanggal
        
    # ENCAPSULATION: nilai asli disimpan di atribut private __jumlah,
    # dibaca lewat @property dan diubah lewat setter yang memvalidasi
    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, nilai):
        # VALIDASI: denda tidak boleh negatif (aturannya ada di validasiJumlah)
        if not Denda.validasiJumlah(nilai):
            raise ValueError("Jumlah denda tidak boleh negatif")
        self.__jumlah = nilai

    # STATICMETHOD: fungsi pembantu milik class Denda,
    # tidak memakai self maupun cls (tidak butuh data objek sama sekali)
    @staticmethod
    def validasiJumlah(jumlah):
        return jumlah >= 0

    # method hitung denda 
    def hitungDenda(self, terlambat):
        self.jumlah = terlambat * 2000 
        print("Total denda: Rp", self.jumlah)