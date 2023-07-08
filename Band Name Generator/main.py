# Membuat sebuah awalan program
print("=" * 40)
print("Selamat datang di Band Name Generator!")
print("=" * 40)

# Menanyakan user di kota mana mereka dibesarkan.
print("Di kota mana kamu dibesarkan?")
kota = input("Jawab: ")
print("-----")

# Menanyakan sebuah benda yang user pikirkan.
print("Sebutkan sebuah benda yang sedang kamu pikirkan saat ini!")
benda = input("Jawab: ")
print("-----")

# Menggabungkan nama kota dan benda, dan menampilkan nama band mereka.
print(f'Nama band anda adalah "{kota.capitalize()} {benda.capitalize()}"')

# Penanda
print("=" * 40)
print("Band Name Generator by Einrafh")
print("=" * 40)