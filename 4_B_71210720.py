x=int(input("Masukkan angka:"))
if x%2 ==0 and x%3 !=0: 
    print("Bilangan tersebut habis dibagi 2 dan tidak dihabis 3? Jawab: YA")
else:
    print("Bilangan tersebut tidak habis dibagi 2 dan habis dibagi 3. Program dihentikan")
    quit()
if x%5 !=0 or x%10 ==0:
    print("Apakah bilangan tersbeut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: IYA DONG")
else:
    print("Apakah bilangan tersbeut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: TIDAK")