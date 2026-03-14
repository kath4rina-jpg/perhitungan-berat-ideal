# Program Menghitung Berat Badan Ideal
# Rumus: (Tinggi - 100) - (10% * (Tinggi - 100))

# Masukkan input tinggi badan
tinggi_badan = float(input("Masukkan tinggi badan Anda (cm): "))

# Langkah 1: Pengurangan pertama dengan 100
hasil_awal = tinggi_badan - 100

# Langkah 2: Hitung potongan 10% dari hasil awal
potongan = 0.1 * hasil_awal

# Langkah 3: Hitung berat ideal akhir
berat_ideal = hasil_awal - potongan

# Tampilkan hasil
print(f"Berat badan ideal Anda adalah: {berat_ideal} kg")
