# Librari
import asetCipher

# Inisialisasi alfabet
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Membuat fungsi cipher untuk enkode dan dekode teks
def cipher(teksAwal, jumlahShift, jenisCipher):
    teksAkhir = ""

    # Mengubah jumlah shift menjadi negatif jika ingin dekode teks
    if jenisCipher == "dekode":
        jumlahShift *= -1

    # Proses enkode dan dekode
    for karakter in teksAwal:
        if karakter in alfabet:
            posisi = alfabet.index(karakter)
            posisiBaru = posisi + jumlahShift
            teksAkhir += alfabet[posisiBaru]
        else:
            teksAkhir += karakter
    
    # Menampilkan hasil akhir teks
    print(f"Berikut hasil {jenisCipher}nya:")
    print(f"{teksAkhir}")

# Membuat sebuah awalan program
print(asetCipher.LOGO)
print("Selamat datang di Caesar Cipher!")

# Input dan memanggil fungsi cipher
while True:
    # Memeriksa valid tidaknya input jenis
    while True:
        # Input jenis
        print("Ketik \"enkode\" untuk enkripsi, ketik \"dekode\" untuk dekripsi.")
        jenis = input("Jawab: ").lower()

        if jenis == "enkode" or jenis == "dekode":
            print("-----")
            break
        else:
            print("Input tidak valid.")
            print("-----")

    # Input teks
    print("Ketik pesan kamu:")
    teks = input("Jawab: ").lower()
    print("-----")

    # Memeriksa valid tidaknya input jumlah shift
    while True:
        try:
            # Input shift
            print("Masukkan jumlah shift yang kamu inginkan:")
            shift = int(input("Jawab: "))
            shift = shift % 26
            print("-----")
            break
        except ValueError:
            print("Input tidak valid.")
            print("-----")

    # Memanggil fungsi cipher
    cipher(teksAwal=teks, jumlahShift=shift, jenisCipher=jenis)
    print("-----")

    # Menanyakan apakah user ingin mengulangi program atau tidak
    while True:
        print("Ketik \"ya\" jika kamu ingin mengulangi program. Jika tidak ketik \"tidak\".")
        ulangi = input("Jawab: ").lower()

        if ulangi == "ya":
            print("-----")
            break
        elif ulangi == "tidak":
            break
        else:
            print("Input tidak valid.")
            print("-----")
    
    if ulangi == "tidak":
        break

# Penanda
print("=" * 40)
print("Caesar Cipher by Einrafh")
print("=" * 40)