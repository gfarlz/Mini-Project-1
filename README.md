# Mini-Project-1
NAMA: Ghifari Al Azhar 
NIM:2409116059

FLOWCHART
![flowchart drawio](https://github.com/user-attachments/assets/53ea4aef-5c19-4cd7-88d4-e9e149b05289)

Penjelasan code 
  1. def hitung_gaji():
def berguna untuk mendefinisikan sebuah fungsi

  2. jam_kerja = float(input("Masukkan jumlah jam kerja: "))
     tarif_per_jam = float(input("Masukkan tarif per jam: "))

     gaji_dasar = jam_kerja * tarif_per_jam

     def login():
         print("=== Login ===")
         nama = input("Masukkan Nama: ")
         nim = input("Masukkan NIM: ")
         print(f"Selamat datang, {nama}!")
         return nama, nim

  nama, nim = login()

Penginputan jam kerja, tarif per jam, nama, dan NIM

  3. if jam_kerja > 160:
        bonus = 0.1 * gaji_dasar
        total_gaji = gaji_dasar + bonus
        print(f"Kerja Bagus! Anda mendapatkan bonus 10%")
        print(f"Gaji dasar: Rp {gaji_dasar:}")
        print(f"Bonus: Rp {bonus:}")
        print(f"Total gaji: Rp {total_gaji:}")
    else:
        print(f"Gaji Anda: Rp {gaji_dasar:}")
        print("Anda tidak mendapatkan bonus karena jam kerja kurang dari atau sama dengan 160 jam")

Jika jam kerja lebih dari 160 jam maka akan mendapatkan bonus 10% dari total gaji

  4. while True:
    hitung_gaji()
    
      selesai = input("Apakah Anda ingin menghitung gaji lagi? (hitung lagi/tidak): ")
      if selesai.lower() != 'hitung lagi':
        print("Sampai Jumpa Karyawan!")
        break
Melakukan pengulangan hitung gaji dengan menggunakan while

Penjelsan output
![image](https://github.com/user-attachments/assets/2c14d699-2bc8-41c3-9a62-2bf960de9d47)

Program dimulai dengan memasukan nama dan NIM lalu dilanjutkan dengan mengisi jam kerja dan tarif per jam, jika jam kerja lebih dari 160 jam maka akan mendapat bonus 10% dari total gaji pokok
dan jika jam kerja tidak lebih dari 160 jam maka tidak akan mendapatkan bonus dan hanya mendapatkan gaji pokok, setelah total gaji keluar akan ditanya "Apakah Anda ingin menghitung gaji lagi? (hitung lagi/tidak)"
jika memilih "hitung lagi" maka akan kembali lagi ke bagian mengisi jam kerja dan tarif per jam lalu jika memilih "tidak" maka program akan selesai















     
