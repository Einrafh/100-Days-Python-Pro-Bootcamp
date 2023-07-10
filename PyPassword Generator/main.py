# Librari
import random

# Inisialisasi huruf, angka, dan simbol
huruf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
angka = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Membuat sebuah awalan program
print("Selamat datang di PyPassword Generator!")

# Menanyakan jumlah huruf yang ingin dipakai user
while True:
    try:
        print("Berapa banyak huruf yang ingin kamu gunakan pada password kamu?")
        nHuruf = int(input("Jumlah huruf: "))
        print("-----")
        break
    except ValueError:
        print("Input tidak valid! Mohon masukkan angka yang benar.")
        print("-----")

# Menanyakan jumlah angka yang ingin dipakai user
while True:
    try:
        print("Berapa banyak angka yang ingin kamu gunakan pada password kamu?")
        nAngka = int(input("Jumlah angka: "))
        print("-----")
        break
    except ValueError:
        print("Input tidak valid! Mohon masukkan angka yang benar.")
        print("-----")

# Menanyakan jumlah simbol yang ingin dipakai user
while True:
    try:
        print("Berapa banyak simbol yang ingin kamu gunakan pada password kamu?")
        nSimbol = int(input("Jumlah simbol: "))
        print("-----")
        break
    except ValueError:
        print("Input tidak valid! Mohon masukkan angka yang benar.")
        print("-----")

# Memilih secara acak huruf, angka, dan simbol serta menggabungnya ke dalam sebuah list password
listPassword = []

for karakter in range(nHuruf):
    listPassword.append(random.choice(huruf))

for karakter in range(nAngka):
    listPassword.append(random.choice(angka))

for karakter in range(nSimbol):
    listPassword.append(random.choice(simbol))

# Mengacak kembali isi list password
random.shuffle(listPassword)

# Mengubah isi list password menjadi sebuah string password
password = ""
for karakter in listPassword:
    password += karakter

# Menampilkan hasil PyPassword Generator
print(f"Password untuk kamu adalah {password}")

# Penanda
print("=" * 40)
print("Tip Calculator by Einrafh")
print("=" * 40)