angka01 = float(input("Masukkan angka pertama: "))
operasi = str(input("Masukan operasi aritmatika (+,-,/,*,//, %, **): "))
angka02 = float(input("Masukkan angka kedua: "))

if operasi=="+":
    hasil = angka01+angka02
elif operasi=="-":
     hasil = angka01-angka02
elif operasi=="/":
     hasil = angka01/angka02
elif operasi=="*":
     hasil = angka01*angka02
elif operasi=="//":
     hasil = angka01//angka02
elif operasi=="%":
     hasil = angka01%angka02
else:
     hasil = angka01**angka02
print(f"Operasi yang anda input adalah {angka01}{operasi}{angka02}\nMaka, hasilnya adalah {hasil}")