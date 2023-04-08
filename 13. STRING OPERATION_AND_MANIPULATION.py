# 1. Menyambung String (concanenate)
Fist_name = "Jacob"
Middle_name = "Sholomo"
Last_name = "Shaddix"

Full_name = Fist_name+" "+Middle_name+" "+Last_name
print(Full_name)

# 2. Menghitung panjang String
#"len" untuk mengetahui jumlah karakter string
length = len(Full_name)
print("Jumlah karakter string dalam", Full_name, "adalah", str(length))

# 3. Operator untuk String
# Mengecek keberadaan komponen string
find = "ere"
status = find in Full_name
print(find + " ada di "+ Full_name+" "+ str(status))

find = "J" and "S"
status = find in Full_name
print(find + " ada di "+ Full_name+" "+ str(status))

find = "z" and "Q"
status = find not in Full_name
print(find + " tidak ada di "+ Full_name+" "+ str(status))

# Pengulangan String
print("lol"*4)

#indexing
print("Index ke-0: "+Full_name[0])
print("Index ke-1: "+Full_name[1])
print("Index ke-2: "+Full_name[2])
print("Index ke-3: "+Full_name[3])
print("Index ke-4: "+Full_name[4])
print("Index ke-5: "+Full_name[5])
print("Index ke-6: "+Full_name[6])
print("Index ke-0 hingga 5: "+Full_name[0:5])
print("Index ke-6 hingga 12: "+Full_name[6:12])
print("Index ke-2: "+Full_name[0:5:12])

#Item paling kecil
print("Smallest Character on= ", Full_name,"=", min(Full_name))
#Item paling besar
highest_value = max(Full_name)
print("Smallest Character on= ", Full_name,"=", highest_value)

ascii_code = ord(str(highest_value))
print("\nLalu, ASCII Code untuk huruf ", highest_value," = ", str(ascii_code))

data = ascii_code
print("Sementara jika dibalik menggunakan fungsi 'chr',", ascii_code, "merupakan kode untuk karakter =", chr(ascii_code))

value = "G"
ascii_code = ord(value)
print("\nASCII Code untuk huruf ", value," = ", str(ascii_code))

data = ascii_code
print("Sementara jika dibalik menggunakan fungsi 'chr',", ascii_code, "merupakan kode untuk karakter =", chr(ascii_code))

# 4. Operator dalam bentuk Method
data = "The Quick Brown Fox Jumps over lazy Doggos"
letter = "o"
count = data.count(letter)
print("Data =", data, "\nHuruf yang dicari dalam data =", letter, "\nJumlahnya =", count)