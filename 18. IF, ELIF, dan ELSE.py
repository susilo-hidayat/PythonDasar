# Menggunakan fungsi IF dan ELSE untuk membuat proam non-linier
data_input = str(input("Ketik 'Manusia' jika anda bukan robot :")).title()
if data_input == "Manusia":
    print("Selamat Anda adalah manusia")
elif data_input == "Hewan":
    print("Kamu bukan manusia, tapi hewan")
else:
    print("Kamu bukan manusia")