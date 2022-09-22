diskon = 20

def format_rupiah(angka):
    return "Rp. " + str(int(angka))

def potong_diskon(harga_awal):
  potongan = harga_awal * diskon / 100
  return harga_awal - potongan


harga_baju = 20000
harga_baju_diskon = potong_diskon(harga_baju)


print(format_rupiah(harga_baju_diskon))