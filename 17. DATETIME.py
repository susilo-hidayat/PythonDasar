tanggal = int(input("Masukkan tanggal lahir"))
bulan = int(input("Masukkan bulan lahir"))
tahun = int(input("Masukkan tahun lahir"))
print(f"{tanggal}/{bulan}/{tahun}")
import datetime as dt
date = dt.date(tahun,bulan,tanggal)
print(date)
print(f"{date:%A}")

umur = (dt.date.today()-date)/360
print(umur.days, "tahun")