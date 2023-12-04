#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 07:02:52 2023

@author: aepeul
"""

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu Allaykum!")
# salom_ber()

# def salom_ber(ism):
#     """foydalanuvchi unga qiymat qabul qilib, unga Salom berish"""
#     print(f"Assalomu Alaykum {ism.title()}!")    
# salom_ber('sultonbek')    

# def toliq_ism(ism,familiya):
#     """Foydalanuvchi ismi va familiyasini jamlab chiqaruvchi function"""
#     print(f"Foydalanuvchi ismi {ism.title()}\n"
#           f"Foydalanuvchi familiyasi {familiya.title()}")
# toliq_ism('sultonbek', 'batirov')    

# def yosh_hisobla(ism, t_yil):
#     """Foydalanuvchi yoshini hisoblagich"""
#     print(f"{ism.title()} {2023-t_yil} yoshda")
# yosh_hisobla('sultonbek', 1995)    
def yosh_hisobla(t_yil,joriy_yil=2023):
    print(f"siz {joriy_yil-t_yil} yoshdasiz.")
#yosh_hisobla(1995, 2023)    
yosh_hisobla(1995)