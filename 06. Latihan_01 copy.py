print ("Masukkan kode R untuk Reamur, C untuk Celcius, F untuk Fahrenheit, dan K untuk kelvin pada satuan asal dan satuan hasil konversi")
data_suhu = float(input("Masukkan suhu = "))
satuan_asal = str(input("Masukkan satuan asal yang akan dikonversikan (C, R, F, atau K)= ")).upper()
satuan_konversi = str(input("Masukan satuan hasil konversi (C, R, F, atau K)= ")).upper()

#Penentuan pembilang 
if satuan_konversi in ('C'):
  x, sk  = 5, "°Celcius"
elif satuan_konversi in('R'):
  x, sk  = 4, "°Reaumur"
elif satuan_konversi in('K'):
  x, sk  = 5, "Kelvin"
else:
  x, sk = 9, "°Fahrenheit"

#penyebut
if satuan_asal in ('C'):
  y, sa  = 5, "°Celcius"
elif satuan_asal in('R'):
  y, sa  = 4, "°Reaumur"
elif satuan_asal in('K'):
  y, sa  = 5, "Kelvin"
else:
  y, sa = 9, "°Fahrenheit"

#penentuan operasi tambahan
if y == 9:
   data_suhu = data_suhu - 32.0

if satuan_asal== "K":
  data_suhu=data_suhu-273.15


#Cal
if y == 9:
  print("Data anda adalah =", data_suhu+32,sa)
else:
  print("Data anda adalah = ", data_suhu,sa)

if x == 9:
  print("Data hasil konversi =", (x/y*data_suhu)+32,sk)
elif satuan_konversi in('K'):
  print("Data hasil konversi =", (x/y*data_suhu)+273.15,sk)
else:
  print("Data hasil konversi =", x/y*data_suhu,sk)









    