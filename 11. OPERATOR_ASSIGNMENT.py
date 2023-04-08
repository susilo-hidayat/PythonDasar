print("Pada bagian ini akan dijelaskan bagimana cara melakukan assignment sekaligus operasi")
print(" x = 3 adalah assignment, sementara +,-, dan semua operasi artimatika adalah operasi")
x = 5

print("Jika x = 5, maka")
x += 1 #ini memiliki arti bahwa x = x + 1
print("x = x + 1 =",x)
print("x =+ 1 =",x)

x -= 1 #ini memiliki arti bahwa x = x - 1
print("x -= 1 =", x)

x *= 2 #ini memiliki arti bahwa x = x * 2
print("x *= 2 =", x)

x /= 5 #ini memiliki arti bahwa x = x / 5
print("x /= 2 =",x)

b = 50
print("\n b = ",b)
b //= 25 #ini memiliki arti bahwa b = b // 25
print("b //= 25 =", b)

c = 37
print("\n c =",c)
c %= 12 #ini memiliki arti bahwa c = c & 12
print("c %= 12 =", c)

c = 2
print("\n c =",c)
c **= 4 #ini memiliki arti bahwa c = c ** 2
print("c **= 4 =", c)

print("\n")
#operasi bitwise
print("=======OR======")
c = True
print("c =", c)
c |= False #ini memiliki arti bahwa c = True, True or False =  True
print("c |= False =", c)
c |= True
print("c |= True =", c)
print("Perlu diingat bahwa aturan OR adalah jika salah satu value ada true, hasil akan true")
print("\n=======AND======")
c = True
print("c =", c)
c &= False #ini memiliki arti bahwa c = True, c = c and false = True and False =  True
print("c &= False =", c)
d = True
print("d = ", d)
d &= True #ini memiliki arti bahwa d = True, d = d and true = True and true =  True
print("d &= True =", d)

print("Perlu diingat bahwa aturan AND adalah jika salah satu value ada false, hasil akan false")
print("\n=======XOR======")
e = True
print("e =", e)
e ^= False #ini memiliki arti bahwa e = True, e = e and false = True and False =  True
print("c ^= False =", e)
f = True
print("f = ", f)
f ^= True #ini memiliki arti bahwa f = True, f = f and true = True and true =  True
print("f ^= True =", f)

print("Hasil dari XOR berlaku seperti pengurangan 1 dan 0 -> 1 adalah true, 0 adalah false, yang mana hasil selain 0 baik bernilai positif maupun negati menghasilkan nilai True")