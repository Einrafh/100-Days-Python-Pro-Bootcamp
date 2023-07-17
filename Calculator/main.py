# Librari
import asetCalculator

# Membuat fungsi clear terminal
def clear():
    print("\033[H\033[2J", end="", flush=True)

# Membuat fungsi tambah
def tambah(a1, a2):
    return a1 + a2

# Membuat fungsi kurang
def kurang(a1, a2):
    return a1 - a2

# Membuat fungsi kali
def kali(a1, a2):
    return a1 * a2

# Membuat fungsi bagi
def bagi(a1, a2):
    return a1 / a2

# Membuat dictionary operasi
operasi = {
    "+": tambah,
    "-": kurang,
    "*": kali,
    "/": bagi
}

# Membuat fungsi kalkulator
def kalkulator(angkaPertama, angkaKedua, operator):
    kalkulasi = operasi[operator]
    jawaban = kalkulasi(angkaPertama, angkaKedua)
    return jawaban

# Loop jika user ingin mengulang program
ulang = True
while ulang:
    # Membuat sebuah awalan program
    print(asetCalculator.logo)

    # Mengecek input angka pertama valid
    while True:
        try:
            # Input angka pertama
            angka1 = float(input("Ketik angka pertama: "))
            print("-----")
            break
        except ValueError:
            print("Input tidak valid.")
            print("-----")
    
    # Loop jika user ingin lanjut kalkulasi dari hasil
    lanjut = True
    while lanjut:
        # Menampilkan semua operator yang berada pada operasi
        opKeys = list(operasi.keys())
        panjangOpKeys = len(opKeys)

        # Mengecek input operator valid
        while True:
            for i, key in enumerate(opKeys):
                print(key, end="")
                if i == panjangOpKeys - 1:
                    print("")
                else:
                    print(" ", end="")

            # Input operator
            print("Pilih salah satu operator di atas!")
            operator = input("Operator: ")

            if operator in operasi:
                print("-----")
                break
            else:
                print("Input tidak valid.")
                print("-----")

        # Mengecek input angka kedua valid
        while True:
            try:
                # Input angka kedua
                angka2 = float(input("Ketik angka selanjutnya: "))
                print("-----")
                break
            except ValueError:
                print("Input tidak valid.")
                print("-----")

        # Kalkulasi hasil operasi
        hasil = kalkulator(angkaPertama=angka1, angkaKedua=angka2, operator=operator)

        # Mengecek apakah angka pertama, angka kedua, dan hasil merupakan integer
        if angka1.is_integer():
            angka1 = int(angka1)
        if angka2.is_integer():
            angka2 = int(angka2)
        if hasil.is_integer():
            hasil = int(hasil)

        # Menampilkan hasil
        print(f"Hasil dari {angka1} {operator} {angka2} adalah {hasil}")

        # Menanyakan user apakah ingin melanjutkan kalkulasi dari hasil
        while True:
            print(f"Apakah kamu ingin melanjutkan menghitung dengan {hasil}? Ketik \"ya\" atau \"tidak\".")
            lanjutkan = input("Jawab: ").lower()

            if lanjutkan == "ya":
                angka1 = float(hasil)
                print("-----")
                break
            elif lanjutkan == "tidak":
                print("-----")
                lanjut = False
                break
            else:
                print("Input tidak valid.")
                print("-----")

    # Menanyakan user apakah ingin mengulang program atau tidak
    while True:
        print("Apakah kamu ingin mengulang program? Ketik \"ya\" atau \"tidak\".")
        ulangi = input("Jawab: ").lower()

        if ulangi == "ya":
            clear()
            break
        elif ulangi == "tidak":
            break
        else:
            print("Input tidak valid.")
            print("-----")
    
    # Mengecek apakah user ingin mengulang program atau tidak
    if ulangi == "tidak":
        ulang = False

# Penanda
print("=" * 40)
print("Calculator by Einrafh")
print("=" * 40)