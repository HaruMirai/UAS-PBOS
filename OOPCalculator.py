class kalkulatorku:
    def tambah(self,a,b):
        return a+b
    def kurang(self,a,b):
        return a-b
    def kali(self,a,b):
        return a*b
    def bagi(self,a,b):
        return a/b
    def pangkat(self,a,b):
        return pow(a,b)

cal = kalkulatorku()

while True:
    operator = int(input("""
    1 = Penjumlahan
    2 = Pengurangan
    3 = Perkalian
    4 = Pembagian
    5 = Perpangkatan
    6 = Exit
    Pilihan = 
    """))
    if operator == 6:
        break
    elif operator >= 7:
        print("Error")
        break
    elif operator <= 0:
        print("Error")
        break

    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))

    if operator == 1:
        print("Hasil dari", a,"+",b,"=",cal.tambah(a,b))
    elif operator == 2:
        print("Hasil dari", a,"-",b,"=",cal.kurang(a,b))
    elif operator == 3:
        print("Hasil dari", a,"*",b,"=",cal.kali(a,b))
    elif operator == 4:
        print("Hasil dari", a,"/",b,"=",cal.bagi(a,b))
    elif operator == 5:
        print("Hasil dari", a,"^",b,"=",cal.pangkat(a,b))


