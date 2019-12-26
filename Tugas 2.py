print("Operasi Pertambahan, Pengurangan, Perkalian, Pembagian !!!")
Pilihan = input("Pilih Operasi 1/2/3/4 :")
if Pilihan == '1':
    print("1. Penjumlahan")
if Pilihan == '2':
    print("2. Pengurangan")
if Pilihan == '3':
    print("3. Perkalian")
if Pilihan == '4':
    print("4. Pembagian")

def Penjumlahan(x,y,z):
    return x+y+z
def Pengurangan(x,y,z):
    return x-y-z
def Perkalian(x,y,z):
    return x*y*z
def Pembagian(x,y,z):
    return x/y/z
    
Angka1 = int(input("Angka pertama : "))
Angka2 = int(input("Angka kedua : "))
Angka3 = int(input("Angka ketiga : "))

if  Pilihan == '1':
    print(Angka1," + ",Angka2," + ",Angka3," = ",Penjumlahan(Angka1,Angka2,Angka3))
    print("Hasil =",Penjumlahan(Angka1,Angka2,Angka3))
elif Pilihan == '2':
    print(Angka1," - ",Angka2," - ",Angka3," = ",Pengurangan(Angka1,Angka2,Angka3))
    print("Hasil =",Pengurangan(Angka1,Angka2,Angka3))
elif Pilihan == '3':
    print(Angka1," x ",Angka2," x ",Angka3," = ",Perkalian(Angka1,Angka2,Angka3))
    print("Hasil =",Perkalian(Angka1,Angka2,Angka3))
elif Pilihan == '4':
    print(Angka1," / ",Angka2," / ",Angka3," = ",Pembagian(Angka1,Angka2,Angka3))
    print("Hasil =",Pembagian(Angka1,Angka2,Angka3))
input('Press ENTER to Exit')
