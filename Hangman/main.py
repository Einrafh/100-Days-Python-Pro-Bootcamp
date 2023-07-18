# Librari
import asetHangman
import kataHangman
import random

# Inisialisasi kata tebakan
kataTebakan = random.choice(kataHangman.daftarKata)
panjangKata = len(kataTebakan)

# Inisialisasi jumlah darah
darah = 6
maksDarah = 6

# Membuat sebuah awalan program
print(asetHangman.LOGO)

# Membuat display kotak jawaban
display = []
for _ in range(panjangKata):
    display.append("_")

while True:
    # Menebak sebuah huruf
    print("Tebak sebuah huruf pada kata tebakan!")
    tebakan = input("Tebak: ").lower()

    # Mengecek jika user menebak huruf yang sama
    if tebakan in display:
        print(f"Kamu sudah menebak huruf {tebakan}.")

    # Mengecek jika tebakan user benar
    for posisi in range(panjangKata):
        huruf = kataTebakan[posisi]
        if huruf == tebakan:
            display[posisi] = huruf

    # Mengecek jika tebakan user salah
    if tebakan not in kataTebakan:
        print(f"Huruf {tebakan} tidak terdapat pada kata tebakan. Kamu kehilangan 1 darah!")
        darah -= 1
        print(f"Darah: {darah}/{maksDarah}")

        if darah == 0:
            print("Kamu kalah!")
            print(asetHangman.TAHAPAN[darah])
            break
    
    # Menampilkan kotak display
    print(f"{' '.join(display)}")

    # Mengecek jika user telah menebak seluruh huruf pada kata tebakan
    if "_" not in display:
        print("Kamu menang!")
        break

    # Menampilkan ilustrasi hangman sesuai darah tersisa
    print(asetHangman.TAHAPAN[darah])

# Penanda
print("=" * 40)
print("Hangman by Einrafh")
print("=" * 40)