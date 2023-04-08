#Hasil dari operasi komparasi adalah boolean (true/false)
#operator komparasi tersebut di antaranya >,<,>=,>=,==, !=, is, is not
a = 12
b = 3

print("==========Lebih besar dari > ==========")
hasil = a > 3
print(a, ">", 3, "=", hasil)
hasil = a > 15
print(a, ">", 15, "=", hasil)
hasil = a > 12
print(a, ">", 12, "=", hasil)

print("==========Kurang dari dari < ==========")
hasil = b < 4
print(b, "<", 4, "=", hasil)
hasil = a < 10
print(a, "<", 10, "=", hasil)
hasil = a < 12
print(a, "<", 12, "=", hasil)

print("==========Lebih besar dari sama dengan >= ==========")
hasil = a >= 3
print(a, ">=", 3, "=", hasil)
hasil = a >= 15
print(a, ">=", 15, "=", hasil)
hasil = a >= 12
print(a, ">=", 12, "=", hasil)

print("==========Kurang dari dari <= ==========")
hasil = b <= 4
print(b, "<=", 4, "=", hasil)
hasil = a <= 10
print(a, "<=", 10, "=", hasil)
hasil = a <= 12
print(a, "<=", 12, "=", hasil)

print("==========Sama dengan == ==========")
hasil = b==3
print(b, "==", 3, hasil)
hasil = b==2
print(b, "==", 2, hasil)

print("========== Tidak sama dengan != ==========")
hasil = b!=3
print(b, "!=", 3, hasil)
hasil = b!=2
print(b, "!=", 2, hasil)

print("========== IS dan IS NOT ==========")
print("digunakan untuk membandingan dua objek non literal")
print("Misal X = 2, maka x merupakan objek/variabel benilai literal 2")
print("Jika kita memiliki y = 3, maka y juga merupakan objek/variabel bernilai literal 3")
x = 3
y = 3
z = 4

print("x =", x)
print("y =", y)
print("z =", z)
print("========================")
hasil = x is y
print("x is y ->", x, "is", y, hasil)
print(x, "= x =", hex(id(x)))
print(y,"= y =", hex(id(x)))
print("x dan y dikarenakan bernilai literal sama yaitu 3, maka hasil perbandingan is adalah True. Dari nilai hex juga terbukti sama")
print("========================")
hasil = x is z
print("x is z", x, "is", z, hasil)
print(x, "= x =", hex(id(x)))
print(z,"= z =", hex(id(z)))
print("x dan z dikarenakan bernilai literal berbeda yaitu 3 dan 4, maka hasil perbandingan is adalah False. Dari nilai hex juga berbeda")
print("========================")
hasil = x is not y
print("x is not y ->", x, "is not", y, hasil)
print(x, "= x =", hex(id(x)))
print(y,"= y =", hex(id(x)))
print("x dan y dikarenakan bernilai literal sama yaitu 3, maka hasil perbandingan is not adalah False. Dari nilai hex juga terbukti sama")
print("========================")
hasil = x is not z
print("x is not z ->", x, "is not", z, hasil)
print(x, "= x =", hex(id(x)))
print(z,"= z =", hex(id(z)))
print("x dan z dikarenakan bernilai literal berbeda yaitu 3 dan 4, maka hasil perbandingan is not adalah True. Dari nilai hex juga berbeda")
