def hitung_gaji():
    print("=== Penghitung Gaji Karyawan ===")
    
    jam_kerja = float(input("Masukkan jumlah jam kerja: "))
    tarif_per_jam = float(input("Masukkan tarif per jam: "))
    
    gaji_dasar = jam_kerja * tarif_per_jam
    
    if jam_kerja > 160:
        bonus = 0.1 * gaji_dasar
        total_gaji = gaji_dasar + bonus
        print(f"Kerja Bagus! Anda mendapatkan bonus 10%")
        print(f"Gaji dasar: Rp {gaji_dasar:}")
        print(f"Bonus: Rp {bonus:}")
        print(f"Total gaji: Rp {total_gaji:}")
    else:
        print(f"Gaji Anda: Rp {gaji_dasar:}")
        print("Anda tidak mendapatkan bonus karena jam kerja kurang dari atau sama dengan 160 jam")

def login():
    print("=== Login ===")
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    print(f"Selamat datang, {nama}!")
    return nama, nim

nama, nim = login()

while True:
    hitung_gaji()
    
    selesai = input("Apakah Anda ingin menghitung gaji lagi? (hitung lagi/tidak): ")
    if selesai.lower() != 'hitung lagi':
        print("Sampai Jumpa Karyawan!")
        break