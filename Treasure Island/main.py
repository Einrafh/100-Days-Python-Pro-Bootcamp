# Membuat sebuah awalan program
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Selamat datang di Treasure Island!")
print("Misi kamu adalah menemukan sebuah harta karun.")
print("-----")

# Pertanyaan pertama
def pertanyaanPertama():
    print("Kamu berada di persimpangan jalan. Ke mana kamu mau pergi? Ketik \"kiri\" atau \"kanan\"")
    pilihan1 = input("Jawab: ").lower()

    if pilihan1 == "kiri":
        pertanyaanKedua()
    elif pilihan1 == "kanan":
        print("Kamu terjatuh ke dalam jurang yang dalam. Permainan berakhir.")
    else:
        print("Tolong masukkan jawaban yang valid!")
        print("-----")
        pertanyaanPertama()

# Pertanyaan kedua
def pertanyaanKedua():
    print("Kamu menemukan sebuah danau, ada sebuah pulau di tengah danau itu. Ketik \"tunggu\" untuk menunggu perahu atau ketik \"berenang\" untuk berenang ke pulau tersebut.")
    pilihan2 = input("Jawab: ").lower()

    if pilihan2 == "tunggu":
        pertanyaanKetiga()
    elif pilihan2 == "berenang":
        print("Kamu diserang oleh ikan piranha yang kelaparan. Permainan berakhir.")
    else:
        print("Tolong masukkan jawaban yang valid!")
        print("-----")
        pertanyaanKedua()

# Pertanyaan ketiga
def pertanyaanKetiga():
    print("Kamu tiba di pulau itu tanpa cedera. Ada sebuah rumah dengan 3 pintu. Satu merah, satu kuning dan satu biru. Warna apa yang kamu pilih?")
    pilihan3 = input("Jawab: ").lower()
    
    if pilihan3 == "merah":
        print("Ini adalah ruangan yang penuh dengan api. Permainan berakhir.")
    elif pilihan3 == "kuning":
        print("Kamu menemukan harta karunnya! Kamu menang!")
    elif pilihan3 == "biru":
        print("Kamu memasuki ruangan yang dipenuhi binatang buas. Permainan berakhir.")
    else:
        print("Kamu memilih pintu yang tidak ada. Permainan berakhir.")

# Memanggil fungsi pertanyaan pertama
pertanyaanPertama()

# Penanda
print("=" * 40)
print("Treasure Island by Einrafh")
print("=" * 40)