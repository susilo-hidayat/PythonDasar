#Format String
#daripada menulis
movie = "Pulp Fiction"
director = "Quentin Tarantino"
full = "Movie name: "+ movie+ " directed by "+director
print(full)
#mending ditulis seperti ini
format_full = f"Movie name: {movie} directed by {director}"
print(format_full)

#bool
end_check = format_full.endswith("Tarantino")
format_str = f"Boolean {str(end_check)}"
print(format_str)

#angka
import math as m
value = m.pi
format_str = f"Rumus lingkaran = {value} * Radius**2"
print(format_str)
#menyingkat float
import math as m
value = m.pi
format_str = f"Rumus lingkaran = {value:.2f} * Radius**2"
print(format_str)
#menyingkat float dan menambah angka didepan
import math as m
value = m.pi
format_str = f"Rumus lingkaran = {value:06.2f} * Radius**2"
print(format_str)

#persen
value = 0.45968679
format_str = f"Persentase {value:.2%}"
print(format_str)

#melakukan operasi 
value2 = 0.265656
format_str = f"Total hasil penjumlahan: {value+value2:.2%}"
print(format_str)

#format angka lain
value = 4
print("\nFormat angka lain")
print("Angka = ", value)
print(f"Binary = {bin(value)}")
print(f"Octal = {oct(value)}")
print(f"Hexadecimal = {hex(value)}")