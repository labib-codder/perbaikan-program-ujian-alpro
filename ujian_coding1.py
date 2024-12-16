# -*- coding: utf-8 -*-
"""
muhamad ihsanul labib
mahasiswa polines ik-1b
Created on Wed Dec 11 08:47:58 2024
"""
# Mulai program
def hitung_jumlah(n):
    # Tetapkan nilai awal
    total = 0
    i = 1
    
    # Periksa apakah i <= n
    while i <= n:
        total += i
        i += 1
    
    # Cetak total
    return total

# Masukkan nilai n
n = int(input("Masukkan nilai n: "))
hasil = hitung_jumlah(n)
print(f"Jumlah bilangan dari 1 hingga {n} adalah {hasil}")
