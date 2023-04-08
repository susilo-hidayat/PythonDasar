print("Membuat checker rentang angka")
print("Angka input akan bernilai benar/True apabila \nkurang dari 4 lebih dari 12")
angka = float(input("Masukkan angka :"))
hasil = angka <= 4 or angka >= 12
print(hasil)
if hasil == False:
    print(angka, "merupakan angka lebih dari sama dengan 4 dan kurang dari sama dengan 12, sehingga salah")
if hasil == True:
    print(angka, "merupakan angka yang bernilai kurang dari sama dengan 4 atau lebih dari sama dengan 12, sehingga benar")
print("\n")
print("Membuat checker rentang angka irisan")
print("Angka input akan bernilai benar/True apabila \nlebih dari 4 kurang dari 12")
angka = float(input("Masukkan angka :"))
hasil = angka >= 4 and angka <= 12
print(hasil)
if hasil == True:
    print(angka, "merupakan angka lebih dari sama dengan 4 dan kurang dari sama dengan 12, sehingga benar")
if hasil == False:
    print(angka, "merupakan angka yang bernilai kurang dari sama dengan 4 atau lebih dari sama dengan 12, sehingga salah")