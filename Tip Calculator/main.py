# Librari
import locale

# Membuat sebuah awalan program
print("=" * 40)
print("Selamat datang di Tip Calculator!")
print("=" * 40)

# Menanyakan total bill/tagihan
while True:
    try:
        print("Berapa total bill/tagihannya?")
        bill = int(input("Jawab: Rp"))
        print("-----")
        break
    except ValueError:
        print("Input tidak valid! Mohon masukkan angka yang benar.")
        print("-----")

# Menanyakan berapa persen tip yang ingin diberikan
while True:
    try:
        print("Berapa persen tip yang ingin kamu berikan?")
        tip = int(input("Jawab: "))
        print("-----")
        break
    except ValueError:
        print("Input tidak valid! Mohon masukkan angka yang benar.")
        print("-----")

# Menanyakan jumlah orang yang ingin berbagi tagihan
while True:
    try:
        print("Berapa banyak orang yang ingin berbagi bill/tagihan?")
        orang = int(input("Jawab: "))
        print("-----")
        break
    except ValueError:
        print("Input tidak valid! Mohon masukkan angka yang benar.")
        print("-----")

# Kalkulasi
tipPersen = tip / 100
totalTip = bill * tipPersen
totalBill = bill + totalTip
billPerOrang = totalBill / orang
totalFinal = round(billPerOrang, 2)

# Mengubah format angka
locale.setlocale(locale.LC_ALL, 'id-ID')
totalFinal = locale.format_string("%.2f", totalFinal, grouping=True)

# Menampilkan hasil Tip Calculator
print(f"Setiap orang harus membayar sejumlah Rp{totalFinal}")

# Penanda
print("=" * 40)
print("Tip Calculator by Einrafh")
print("=" * 40)