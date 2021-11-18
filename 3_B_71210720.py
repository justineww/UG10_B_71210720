x=float(input("Masukkan bilangan pertama:"))
y=float(input("Masukkan bilangan kedua:"))
z=str(input("Masukkan Kalimat:"))
if  "tambah" in z:
    print("Hasil Penjumlahan",x,"dengan",y,"adalah",x+y)
elif "kurang" in z:
    print("Hasil Pengurangan",x,"dengan",y,"adalah",x-y)
elif "kali" in z:
    print("Hasil Perkalian",x,"dengan",y,"adalah",x*y)
elif "bagi" in z:
    print("Hasil Pembagian",x,"dengan",y,"adalah",x/y)
else:
    print("Tidak bisa dikonfersikan")
    