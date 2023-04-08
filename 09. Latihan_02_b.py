print("Membuat checker angka menggunakan komparasi objek nonliteral")
angka_input = float(input("Masukan angka = "))
x = 4
y = 12
#Eksklusi
print("\n")
print("Kurang dari sama dengan 4 atau Lebih dari sama dengan 12")
isKurang_dari = angka_input <= x
islebih_dari = angka_input >= y

hasil_akhir = isKurang_dari or islebih_dari
print(hasil_akhir)
#Irisan
print("\n")
isKurang_dari = angka_input <= y
islebih_dari = angka_input >= x

hasil_akhir = isKurang_dari and islebih_dari
if hasil_akhir == True:
        print("angka yang anda input",angka_input, "berada di rentang kurang dari sama dengan", y, "dan lebih dari sama dengan", x, "maka bernilai Benar")
if hasil_akhir == False:
     print("angka yang anda input",angka_input, "berada di rentang lebih dari sama dengan", y, "atau kurang dari sama dengan", x, "maka bernilai salah")