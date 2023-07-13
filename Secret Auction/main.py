# Librari
import asetAuction
import locale

# Inisialisasi variabel
bids = {}

# Membuat fungsi clear terminal
def clear():
    print("\033[H\033[2J", end="", flush=True)

# Membuat fungsi untuk mencari bid tertinggi
def bidTertinggi(daftarBid):
    bidTertinggi = 0
    bidderTertinggi = ""

    for bidder in daftarBid:
        nilaiBid = daftarBid[bidder]

        if nilaiBid > bidTertinggi:
            bidTertinggi = nilaiBid
            bidderTertinggi = bidder
    
    # Mengubah format angka
    locale.setlocale(locale.LC_ALL, 'id-ID')
    bidTertinggi = locale.format_string("%.2f", bidTertinggi, grouping=True)

    print(f"Pemenangnya adalah {bidderTertinggi} dengan bid Rp{bidTertinggi}")

# Membuat sebuah awalan program
print(asetAuction.logo)
print("Selamat datang di Secret Auction!")

# Input dan memanggil fungsi bid tertinggi
while True:
    # Input nama
    print("Siapa nama kamu?")
    nama = input("Jawab: ")

    # Memeriksa valid tidaknya input nilai bid
    while True:
        try:
            # Input nilai bid
            print("Berapa bid kamu?")
            bid = int(input("Jawab: Rp"))
            print("-----")
            break
        except ValueError:
            print("Input tidak valid.")
            print("-----")
    
    # Memasukkan nama dan bid ke dalam bids
    bids[nama] = bid

    # Menanyakan apakah ada bidder lainnya
    while True:
        print("Apakah ada bidder lainnya? Ketik \"ya\" atau \"tidak\".")
        bidderLainnya = input("Jawab: ").lower()

        if bidderLainnya == "ya":
            print("-----")
            # Memanggil fungsi clear untuk menghapus isi terminal sebelumnya
            clear()
            break
        elif bidderLainnya == "tidak":
            print("-----")
            break
        else:
            print("Input tidak valid.")
            print("-----")
    
    if bidderLainnya == "tidak":
        # Memanggil fungsi bid tertinggi
        bidTertinggi(bids)
        break

# Penanda
print("=" * 40)
print("Secret Auction by Einrafh")
print("=" * 40)