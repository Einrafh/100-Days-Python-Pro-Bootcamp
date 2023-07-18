# Librari
import asetBlackjack
import random

# Membuat fungsi clear terminal
def clear():
    print("\033[H\033[2J", end="", flush=True)

# Membuat fungsi deal card sebagai pemilihan kartu secara acak
def dealCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Membuat fungsi kalkulasi skor
def kalkulasiSkor(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

# Membuat fungsi komparasi untuk membandingkan skor user dan komputer
def komparasi(userSkor, kompSkor):
    if userSkor > 21 and kompSkor > 21:
        return "Kamu melewati batas. Kamu kalah 😤"
    
    if userSkor == kompSkor:
        return "Seri 🙃"
    elif kompSkor == 0:
        return "Kalah, lawan memiliki Blackjack 😱"
    elif userSkor == 0:
        return "Menang! Kamu memiliki Blackjack 😎"
    elif userSkor > 21:
        return "Kamu melewati batas. Kamu kalah 😭"
    elif kompSkor > 21:
        return "Lawan melewati batas. Kamu menang! 😁"
    elif userSkor > kompSkor:
        return "Kamu menang! 😃"
    else:
        return "Kamu kalah 😤"

# Menanyakan user apakah ingin memainkan permainan Blackjack
while True:
    print("Apakah kamu ingin memainkan permainan Blackjack? Ketik \"ya\" atau \"tidak\".")
    main = input("Jawab: ").lower()

    if main == "ya":
        blackJack = True
        clear()
        break
    elif main == "tidak":
        blackJack = False
        break
    else:
        print("Input tidak valid.")
        print("-----")

# Loop jika user ingin memainkan ulang permainan Blackjack
while blackJack:
    # Inisialisasi list kartu user dan komputer
    userCards = []
    kompCards = []

    # Mengambil secara acak kartu awalan user dan komputer
    for _ in range(2):
        userCards.append(dealCard())
        kompCards.append(dealCard())

    # Membuat sebuah awalan program
    print(asetBlackjack.LOGO)

    # Loop jika user ingin mengambil kartu kembali
    ambilKartu = True
    while ambilKartu:
        # Kalkulasi skor user dan komputer
        userSkor = kalkulasiSkor(userCards)
        kompSkor = kalkulasiSkor(kompCards)

        # Menampilkan kartu dan skor user dan komputer saat ini
        print(f"    Kartu kamu: {userCards}, skor sekarang: {userSkor}")
        print(f"    Kartu komputer pertama: {kompCards[0]}")

        # Mengecek kondisi skor user dan komputer tidak merupakan Blackjack dan tidak lebih dari 21
        if userSkor == 0 or kompSkor == 0 or userSkor > 21:
            print("-----")
            ambilKartu = False
        else:
            # Menanyakan apakah user ingin mengambil kartu kembali atau tidak
            print("Ketik \"ya\" untuk mengambil kartu lainnya, ketik \"tidak\" untuk stop.")
            userDeal = input("Jawab: ").lower()

            if userDeal == "ya":
                userCards.append(dealCard())
                print("-----")
            elif userDeal == "tidak":
                ambilKartu = False
                print("-----")
            else:
                print("Input tidak valid.")
                print("-----")
                
    # Mengecek apabila skor komputer tidak merupakan Blackjack dan kurang dari 17 maka komputer mengambil kartu secara acak lagi
    while kompSkor != 0 and kompSkor < 17:
        kompCards.append(dealCard())
        kompSkor = kalkulasiSkor(kompCards)

    # Menampilkan kartu dan skor final user dan komputer
    print(f"    Kartu final kamu: {userCards}, final skor kamu: {userSkor}")
    print(f"    Kartu final komputer: {kompCards}, final skor komputer: {kompSkor}")
    print(komparasi(userSkor, kompSkor))

    # Menanyakan apakah user ingin memainkan permainan Blackjack lagi
    while True:
        print("Apakah kamu ingin memainkan permainan Blackjack lagi? Ketik \"ya\" atau \"tidak\".")
        ulangi = input("Jawab: ").lower()

        if ulangi == "ya":
            blackJack = True
            clear()
            break
        elif ulangi == "tidak":
            blackJack = False
            break
        else:
            print("Input tidak valid.")
            print("-----")

# Penanda
print("=" * 40)
print("Blackjack by Einrafh")
print("=" * 40)