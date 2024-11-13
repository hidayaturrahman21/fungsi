def hitung_luas(panjang, lebar):
    return panjang * lebar
def hitung_keliling(panjang, lebar):
    return 2 * (panjang + lebar)

panjang = int(input("Masukkan panjang persegi panjang: "))
lebar = int(input("Masukkan lebar persegi panjang: "))

luas = hitung_luas(panjang, lebar)
keliling = hitung_keliling(panjang, lebar)

print("Luas persegi panjang adalah:", luas)
print("Keliling persegi panjang adalah:", keliling)
