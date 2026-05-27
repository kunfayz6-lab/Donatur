import os
import sys
os.system("clear")
print("""
\033[38;5;39m╭─────╮\033[32m                         ╭─╮
\033[38;5;39m│╭───╮╰╮\033[38;5;214m╭─────╮\033[94m╭─╮────╮\033[37m╭───╭─╮\033[32m  │ │\033[38;5;206m╭╮  ╭─╮\033[38;5;220m╭─╮────╮
\033[38;5;39m││   │ │\033[38;5;214m│╭──╮ │\033[94m│ ╭───╮│\033[37m│╭──╮ │\033[32m╭─╯ ╰───╮\033[38;5;206m│ │\033[38;5;220m│ ╭──╮
\033[38;5;39m││   │ │\033[38;5;214m││  │ │\033[94m│ │   ││\033[37m││  │ │\033[32m╰─╮ ╭───╯\033[38;5;206m│ │\033[38;5;220m│ │  ╰─╯
\033[38;5;39m││   │ │\033[38;5;214m││  │ │\033[94m│ │   ││\033[37m││  │ │\033[32m  │ │\033[38;5;206m││  │ │\033[38;5;220m│ │
\033[38;5;39m││   │ │\033[38;5;214m││  │ │\033[94m│ │   ││\033[37m││  │ │\033[32m  │ │\033[38;5;206m││  │ │\033[38;5;220m│ │
\033[38;5;39m││   │ │\033[38;5;214m│╰──╯ │\033[94m│ │   ││\033[37m│╰──╯ │\033[32m  │ │\033[38;5;206m│╰──╯ │\033[38;5;220m│ │
\033[38;5;39m│╰───╯╭╯\033[38;5;214m╰─────╯\033[94m╰─╯   ╰╯\033[37m╰───╰─╯\033[32m  ╰─╯\033[38;5;206m╰───╰─╯\033[38;5;220m╰─╯
\033[38;5;39m╰─────╯
\033[37m╭───────────────────────────────────────────────╮
\033[37m╰───────────────────────────────────────────────╯
\033[0m""")

# Script Manajemen Daftar Donatur dan Sumbangan
def tampilkan_menu():
    print("\033[38;5;39m\n=== MENU MANAJEMEN DONASI ===")
    print("1. Tambah Data Donatur")
    print("2. Lihat Daftar Donatur & Donasi")
    print("3. Lihat Total dan Rata-rata Donasi")
    print("4. Keluar\033[0m")

# Inisialisasi list untuk menyimpan data dictionary
daftar_donasi = []

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        print("\033[33m\n--- Tambah Donatur Baru ---")
        nama = input("\033[33mNama Donatur : ")
        try:
            # Memastikan input berupa angka (integer)
            jumlah = int(input("\033[37mJumlah Uang Sumbangan (Rp): "))
            
            # Simpan data ke dalam list
            daftar_donasi.append({
                "nama": nama,
                "jumlah": jumlah,
                "no_rek": no_Rek,
                "a/n": a/n
            })
            print("Data donatur berhasil ditambahkan!")
        except ValueError:
            print("Input jumlah uang harus berupa angka (integer) tanpa titik/koma!\033[0m")

    elif pilihan == '2':
        print("\n--- Daftar Donatur ---")
        if not daftar_donasi:
            print("Belum ada data donatur yang tercatat.")
        else:
            print("-" * 35)
            print(f"033[38;5;39m{'NAMA DONATUR':<20} | {'JUMLAH (Rp)':<12}")
            print("-" * 35)
            for i, data in enumerate(daftar_donasi, 1):
                # Memformat angka menjadi format mata uang
                jumlah_format = f"{data['jumlah']:,}"
                print(f"{data['nama']:<20} | {jumlah_format:<12}")
            print("-" * 35)

    elif pilihan == '3':
        print("\n--- Rekapitulasi Donasi ---")
        if not daftar_donasi:
            print("Belum ada data donasi untuk direkap.")
        else:
            total_donasi = sum(data['jumlah'] for data in daftar_donasi)
            rata_rata = total_donasi / len(daftar_donasi)
            
            print(f"Total Donatur : {len(daftar_donasi)} orang")
            print(f"Total Dana Terkumpul : Rp. {total_donasi:,}")
            print(f"Rata-rata Sumbangan  : Rp. {rata_rata:,.2f}")

    elif pilihan == '4':
        print("\n\033[37mTERIMAKASIH SUDAH MEMPERCAYAKAN AMANAHNYA MELALUI BUMI SYAM & 313!\033[33m Jajakallahu khairan....!!\033[0m")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1 hingga 4.")
  
