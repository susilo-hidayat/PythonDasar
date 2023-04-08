#Perulangan
# Jika fungsi IF menghasilkan alur proses linier dan pasti dieksekusi, satu jalur
# Maka dalam perulangan atau FOR LOOP alur proses terjadi secara sikis tergantung value yang kondisi dan value yang ada, bercabang

#bentuk Loop
#for [kondisi]:
    #[Aksi]

#contoh dengan list
value = [2,3,4,5,6]
print(value)

for i in value:
    print(f"Nilai i adalah :{i}")

#contoh dengan range
value = range(5,7)
print(value)

for i in value:
    print(f"Nilai i adalah {i}")

#menggunakan string
value = ["Loop", "Hoop"]
for i in value:
    print(i)

value = "Loop Hoop"
for i in value:
    print(i)