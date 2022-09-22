class Buah:
  def __init__(self, nama, warna):
    self.nama =nama
    self.warna = warna

  # def dimakan(self):
  #   print(f"{self.nama} telah dimakan")
  
  # @staticmethod
  # def tentang():
  #   return "Buah adalah buah, tahu aja kan?"

apel = Buah("merah", "manis")
apel.dimakan()