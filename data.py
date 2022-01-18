class orang:
    def __init__(self, nama, alamat, nim):
        self.nama = nama
        self.alamat = alamat
        self.nim = nim


data = orang(input("Nama = "), input("Alamat = "), input("NIM = "))
print("Nama = ",data.nama)
print("Alamat = ", data.alamat)
print("NIM = ", data.nim)
    

