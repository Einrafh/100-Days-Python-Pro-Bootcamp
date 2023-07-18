# Librari
import asetGuessTheNumber
import random

# Membuat fungsi clear terminal
def clear():
    print("\033[H\033[2J", end="", flush=True)

# Membuat fungsi menentukan jumlah turns sesuai tingkat kesulitan
def setKesulitan(kesulitan):
    level = kesulitan
    TURNS_MUDAH = 10
    TURNS_SULIT = 5

    if level == "mudah":
        return TURNS_MUDAH
    elif level == "sulit":
        return TURNS_SULIT

# Membuat fungsi cek jawaban dan return sisa turns
def cekTebakan(tebakan, jawaban, turns):
    if tebakan > jawaban:
        print("-----")
        print(f"Tebakan kamu: {tebakan}")
        print("Terlalu tinggi.")
        return turns - 1
    elif tebakan < jawaban:
        print("-----")
        print(f"Tebakan kamu: {tebakan}")
        print("Terlalu rendah.")
        return turns - 1
    elif tebakan == jawaban:
        print(f"Kamu berhasil menebaknya! Jawabannya adalah {jawaban}")
        print("-----")
        turns = 0
        return turns

# Membuat fungsi utama dari Guess The Number
def main():
    # Membuat sebuah awalan program
    print(asetGuessTheNumber.LOGO)
    print("Selamat datang di permainan Guess The Number!")
    print("Pikirkan angka antara 1 hingga 100.")

    # Menentukan jawaban secara acak
    jawaban = random.randint(1, 100)
    
    # Mengecek input kesulitan valid
    while True:
        # Input kesulitan
        print("Pilih tingkat kesulitannya. Ketik \"mudah\" atau \"sulit\".")
        kesulitan = input("Jawab: ").lower()

        if kesulitan == "mudah" or kesulitan == "sulit":
            print("-----")
            break
        else:
            print("Input tidak valid.")
            print("-----")

    # Inisialisasi tingkat kesulitan
    turns = setKesulitan(kesulitan)

    # Loop jika jawaban user tidak tepat dan turns masih tersisa
    tebakan = 0
    while tebakan != jawaban and turns != 0:
        # Mengecek input tebakan valid
        try:
            # Input tebakan
            print(f"Kamu memiliki {turns} kesempatan tersisa untuk menebak angkanya.")
            tebakan = int(input("Tebak angkanya: "))

            # Mengecek tebakan
            turns = cekTebakan(tebakan, jawaban, turns)

            # Mengecek kondisi apakah tebakan user tepat atau tidak, dan mengecek apakah ada turns tersisa
            if tebakan != jawaban and turns == 0:
                print("Kamu kehabisan kesempatan menebak. Kamu kalah.")
                print("-----")
            elif tebakan != jawaban:
                print("Tebak lagi!")
        except ValueError:
            print("Input tidak valid.")
            print("-----")
    
    # Menanyakan apakah user ingin memainkan ulang permainan Guess The Number
    while True:
        print("Apakah kamu ingin memainkan Guess The Number lagi? Ketik \"ya\" atau \"tidak\".")
        ulangi = input("Jawab: ").lower()

        if ulangi == "ya":
            clear()
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
print("Caesar Cipher by Einrafh")
print("=" * 40)