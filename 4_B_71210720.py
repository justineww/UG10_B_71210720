x=int(input("Masukkan angka:"))
j1="YA"
j2="IYA DONG"
j3="TIDAK"
if x%2 ==0 and x%3 !=0:
    print("Bilangan tersebut habis dibagi 2 dan tidak dihabis 3? Jawab:",j1)
else:
    print("Bilangan tersebut tidak habis dibagi 2 dan habis dibagi 3. Program dihentikan")
    quit()

if x%5 !=0 or x%10 ==0:
    print("Apakah bilangan tersbeut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab:",j2)
else: 
    x%5 ==0 or x%10 !=0
    print("Apakah bilangan tersbeut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab:",j3)