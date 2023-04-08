# Mengubah case
## lower-> Upper
print("happy birtday!".upper())
## upper -> lower
print("HAPPY BIRTDAY!".lower())
## Upercase first
print("HAPPY BIRTDAY!".capitalize())
## Proper case
print("hAppY bIRTdaY!".title())

# Mengecek lowercase, upper, 
data = "happy birtday!"
print("Apakah ", data, "merupakan lower =", str(data.islower()))
print("Apakah ", data, "merupakan upper =", str(data.isupper()))
print("Apakah ", data, "merupakan huruf semua =", str(data.isalpha()))
data = "Ajkaja1232"
print("\nApakah ", data, "merupakan lower =", str(data.islower()))
print("Apakah ", data, "merupakan upper =", str(data.isupper()))
print("Apakah ", data, "merupakan huruf semua =", str(data.isalpha()))
print("Apakah ", data, "merupakan huruf alphanumeric =", str(data.isalnum()))
print("\n")
# Ajust
print("Tengah".center(50,"-"))
print("Kiri".ljust(50,"-"))
print("Kanan".rjust(50,"-"))
print("\n")
#
data = ['Homo', 'Sapiens', 'Yuval', 'Noah', 'Harari']
gabung = ' '.join(data)
separate = gabung.split(" ")
print("Data :",data)
print("Gabung :",gabung)
print("Split :", separate)

#cek komponen
cek_end = gabung.endswith("Harari")
print("Apakah ", gabung, "berakhiran 'Harari'", str(cek_end))
cek_start = gabung.startswith("Homo")
print("Apakah ", gabung, "berakhiran 'Homo'", str(cek_end))