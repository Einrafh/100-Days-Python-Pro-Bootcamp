# Librari
import asetHigherLower
import dataHigherLower
import random

# Membuat fungsi clear terminal
def clear():
    print("\033[H\033[2J", end="", flush=True)

# Membuat fungsi random akun untuk memilih data secara acak
def randomAkun():
    return random.choice(dataHigherLower.data)

# Membuat fungsi format data
def formatData(akun):
    nama = akun["nama"]
    deskripsi = akun["deskripsi"]
    negara = akun["negara"]
    return f"{nama}, seorang {deskripsi} dari {negara}"

# Membuat fungsi untuk mengecek tebakan user benar atau salah
def cekTebakan(tebakan, followerA, followerB):
    if followerA > followerB:
        return tebakan == "A"
    elif followerA < followerB:
        return tebakan == "B"

# Membuat fungsi utama dari Higher Lower
def main():
    # Clear terminal
    clear()

    # Inisialisasi akun A dan B
    akunA = randomAkun()
    akunB = randomAkun()

    # Inisialisasi skor
    skor = 0

    # Print logo Higher Lower
    print(asetHigherLower.LOGO)

    # Loop ketika user menjawab benar
    while True:
        # Mengganti nilai akun A menjadi akun B dan menginisialisasi akun B kembali
        akunA = akunB
        akunB = randomAkun()

        # Mengecek jika nilai akun A dan B sama maka akun B akan di isi nilai yang lain dari list data
        while akunA == akunB:
            akunB = randomAkun()
        
        # Loop jika input tebakan tidak valid
        tebakan = ""
        while tebakan != "A" and tebakan != "B":
            # Menampilkan komparasi nilai akun A terhadap akun B
            print(f"Komparasi A: {formatData(akunA)}.")
            print(asetHigherLower.VS)
            print(f"Terhadap B: {formatData(akunB)}.")

            # Input tebakan
            print("Siapa yang memiliki lebih banyak follower di Instagram? Ketik \"A\" atau \"B\".")
            tebakan = input("Jawab: ").upper()

            # Mengecek input tebakan valid
            if tebakan != "A" and tebakan != "B":
                clear()
                print(asetHigherLower.LOGO)
                print("Input tidak valid.")
                print(f"Skor kamu sekarang: {skor}")

        # Inisialisasi jumlah follower akun A dan B
        followerA = akunA["jumlahFollower"]
        followerB = akunB["jumlahFollower"]

        # Validasi tebakan user
        validasi = cekTebakan(tebakan, followerA, followerB)

        # Clear terminal
        clear()

        # Print logo Higher Lower
        print(asetHigherLower.LOGO)

        # Mengecek kondisi apakah tebakan user tepat atau tidak
        if validasi:
            skor += 1
            print(f"Kamu benar! Skor kamu sekarang: {skor}")
        else:
            print(f"Maaf, kamu salah. Final skor kamu: {skor}")
            break
    
    # Menanyakan apakah user ingin memainkan ulang permainan Higher Lower
    while True:
        print("Apakah kamu ingin memainkan Higher Lower lagi? Ketik \"ya\" atau \"tidak\".")
        ulangi = input("Jawab: ").lower()

        if ulangi == "ya":
            main()
        elif ulangi == "tidak":
            return
        else:
            print("Input tidak valid.")
            print("-----")

# Memanggil fungsi main()
main()

# Penanda
print("=" * 40)
print("Higher Lower by Einrafh")
print("=" * 40)