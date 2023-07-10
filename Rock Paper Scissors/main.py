# Librari
import random

# Inisialisasi ilustrasi batu, gunting, kertas
batu = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

gunting = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

kertas = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

ilustrasi = [batu, kertas, gunting]

# Membuat sebuah awalan program
print("Selamat datang di Rock Paper Scissors!")

while True:
    while True:
        # Memastikan user input angka
        try:
            # User memilih batu, gunting, kertas
            print("Apa yang kamu pilih? Ketik 1 untuk Batu, 2 untuk Kertas, 3 untuk Gunting.")
            pilihanUser = int(input("Jawab: "))
            break
        except ValueError:
            print("Input tidak valid! Kamu harus input angka.")
            print("-----")

    # Memastikan user input angka yang valid
    if pilihanUser < 1 or pilihanUser > 3:
        print("Kamu mengetik angka yang tidak valid. Kamu kalah!")
        print("-----")
    else:
        print(ilustrasi[pilihanUser - 1])

        # Komputer memilih batu, gunting, kertas
        print("Komputer Memilih:")
        pilihanKomp = random.randint(1, 3)
        print(ilustrasi[pilihanKomp - 1])

        # Menentukan menang dan kalah
        if pilihanUser == 1 and pilihanKomp == 3:
            print("Kamu menang!")
        elif pilihanUser == 3 and pilihanKomp == 1:
            print("Kamu kalah.")
        elif pilihanUser < pilihanKomp:
            print("Kamu kalah.")
        elif pilihanUser > pilihanKomp:
            print("Kamu menang!")
        elif pilihanUser == pilihanKomp:
            print("Seri.")

        print("-----")
    
    # Menanyakan apakah ingin bermain lagi atau tidak
    while True:
        print("Apakah kamu ingin bermain lagi? Ketik \"y\" untuk ya atau \"n\" untuk tidak.")
        ulangi = input("Jawab: ")
        if ulangi.lower() == "y":
            print("-----")
            break
        elif ulangi.lower() == "n":
            break
        else:
            print("Input tidak valid! Kamu harus input antara \"y\" atau \"n\".")
            print("-----")

    if ulangi.lower() == "n":
        break

# Penanda
print("=" * 40)
print("Rock Paper Scissors by Einrafh")
print("=" * 40)