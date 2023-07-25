# Librari
import asetCoffeeMachine
import locale

# Inisialisasi menu Coffee Machine
MENU = {
    "espreso": {
        "bahan": {
            "air": 50,
            "kopi": 18,
        },
        "harga": 9500,
    },
    "latte": {
        "bahan": {
            "air": 200,
            "susu": 150,
            "kopi": 24,
        },
        "harga": 12000,
    },
    "kapucino": {
        "bahan": {
            "air": 250,
            "susu": 100,
            "kopi": 24,
        },
        "harga": 11000,
    }
}

# Inisialisasi persediaan Coffee Machine
persediaan = {
    "air": 300,
    "susu": 200,
    "kopi": 100,
}

# Inisialisasi profit Coffee Machine
profit = 0

# Membuat fungsi clear terminal
def clear():
    print("\033[H\033[2J", end="", flush=True)

# Membuat fungsi format angka menjadi format uang
def formatAngka(angka):
    locale.setlocale(locale.LC_ALL, 'id-ID')
    angka = locale.format_string("%.2f", angka, grouping=True)
    return angka

# Membuat fungsi untuk mengecek persediaan
def cekPersediaan(bahanOrderan):
    for item in bahanOrderan:
        if bahanOrderan[item] > persediaan[item]:
            print(f"Maaf, persediaan {item} tidak cukup.")
            print("-----")
            return False
    return True

# Membuat fungsi untuk proses pembayaran
def prosesBayar():
    while True:
        try:
            print("-----")
            total = int(input("Tolong masukkan uang kamu: "))
            break
        except ValueError:
            print("Input tidak valid.")
            print("-----")

    return total

# Membuat fungsi untuk mengecek pembayaran berhasil atau tidak
def pembayaran(uangBayar, hargaItem):
    if uangBayar >= hargaItem:
        global profit
        profit += hargaItem
        if uangBayar != hargaItem:
            kembalian = round(uangBayar - hargaItem, 2)
            kembalian = formatAngka(kembalian)
            print(f"Kembalian kamu: Rp{kembalian}")
        return True
    else:
        print("Uang kamu tidak mencukupi!")
        print("-----")
        return False

# Membuat fungsi untuk mengolah kopi
def olahKopi(namaOrderan, bahanOrderan):
    for item in bahanOrderan:
        persediaan[item] -= bahanOrderan[item]
    print(f"Ini {namaOrderan} kamu ☕️. Enjoy!")

# Membuat sebuah awalan program
print(asetCoffeeMachine.LOGO)

# Loop jika user ingin membeli kopi lagi
ulangi = True
while ulangi:
    # Menampilkan menu dari Coffee Machine
    print("COFFEE MACHINE MENU: ")
    for item in MENU:
        print(f"- {item.capitalize()} (Rp{formatAngka(MENU[item]['harga'])})")
    
    while True:
        # Input menu
        print("Menu apa yang ingin kamu pesan?")
        print("(Ketik \"off\" untuk mematikan Coffee Machine, ketik \"laporan\" untuk melihat sisa persediaan.)")
        pilih = input("Jawab: ").lower()

        # Mengecek kondisi apakah user memesan sebuah menu, melihat laporan persediaan, atau ingin mematikan mesin
        if pilih == "off":
            ulangi = False
            break
        elif pilih == "laporan":
            print("-----")
            print("=== Laporan Coffee Machine ===")
            print(f"Air: {persediaan['air']}ml")
            print(f"Susu: {persediaan['susu']}ml")
            print(f"Kopi: {persediaan['kopi']}g")
            print(f"Profit: Rp{formatAngka(profit)}")
            print("-----")
            break
        elif pilih in MENU:
            # Inisialisasi orderan user
            orderan = MENU[pilih]
            
            # Mengecek persediaan
            if cekPersediaan(orderan["bahan"]):
                # Proses pembayaran
                bayar = prosesBayar()

                # Mengecek apakah pembayaran berhasil atau tidak
                if pembayaran(bayar, orderan["harga"]):
                    # Mengolah kopi jika pembayaran berhasil
                    olahKopi(pilih, orderan["bahan"])
                    print("-----")
            break
        else:
            print("Input tidak valid.")
            print("-----")

# Penanda
print("=" * 40)
print("Coffee Machine by Einrafh")
print("=" * 40)