print('Program Menghitung Waktu')
print('------------------------')

derajat = float(input(''))
hari = 3600 * 24
detik = round((derajat/360)*hari)
jam = 6
menit = 0

while(detik >= 3600):
    detik -= 3600
    jam += 1

while(detik >= 60):
    detik -= 60
    menit += 1

jam %= 24

if jam >= 6 and jam < 12:
    print("Selamat Pagi")
elif jam >= 12 and jam <= 15:
    print("Selamat Siang")
elif jam > 15 and jam <= 18:
    print("Selamat Sore")
elif jam > 18 and jam <= 24:
    print("Selamat Malam")
else :
    print("Selamat Malam")

print(f"{jam:02d}:{menit:02d}:{detik:02d}")

