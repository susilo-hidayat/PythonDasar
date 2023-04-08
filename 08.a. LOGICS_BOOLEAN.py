print("Jenis operasi logika dan boolean NOT, AND, OR, dan XOR")
print("============ NOT ============ ")
x = False
y = not x
print("x")
print("x = ", x)
print("y = NOT x =", y)
print("=====")
x = True
y = not x
print("x")
print("x = ", x)
print("y = NOT x =", y)
print("hasil dari NOT selalu berkebalikan")
print("============ AND ============ ")
x = True
y = True
z = x and y
print(x, "AND", y,"=", z)
x = False
y = False
z = x and y
print(x, "AND", y,"=", z)
x = False
y = True
z = x and y
print(x, "AND", y,"=", z)
x = True
y = False
z = x and y
print(x, "AND", y,"=", z)
print("Hasil dari AND berlaku seperti perkalian 1 dan 0 -> 1 adalah true, 0 adalah false")
print("============ OR ============ ")
x = True
y = True
z = x or y
print(x, "OR", y,"=", z)
x = False
y = False
z = x or y
print(x, "OR", y,"=", z)
x = False
y = True
z = x or y
print(x, "OR", y,"=", z)
x = True
y = False
z = x or y
print(x, "OR", y,"=", z)
print("Hasil dari OR berlaku seperti penjumlahan 1 dan 0 -> 1 adalah true, 0 adalah false")
print("============ XOR ============ ")
x = True
y = True
z = x ^ y
print(x, "XOR", y,"=", z)
x = False
y = False
z = x ^ y
print(x, "XOR", y,"=", z)
x = False
y = True
z = x ^ y
print(x, "XOR", y,"=", z)
x = True
y = False
z = x ^ y
print(x, "XOR", y,"=", z)
print("Hasil dari XOR berlaku seperti pengurangan 1 dan 0 -> 1 adalah true, 0 adalah false, yang mana hasil selain 0 baik bernilai positif maupun negati menghasilkan nilai True")

