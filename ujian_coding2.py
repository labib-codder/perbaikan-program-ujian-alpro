# -*- coding: utf-8 -*-
"""
muhamad ihsanul labib
mahasiswa polines ik-1b
Created on Mon Dec 16 13:30:15 2024
"""

from math import pi

def lingkaran(r):
    area = pi * r ** 2
    print(f"Luas Lingkaran: {area}")
    return area

# Contoh pemanggilan fungsi
r = int(input("Masukkan jari-jari: "))
lingkaran(r)
