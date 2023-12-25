#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:30:30 2023

@author: aepeul
"""

yosh=input("yoshingizni kiriting: ")
try:
    yosh=int(yosh)
    print(f"Siz {2023-yosh} yilda tug'ilgansiz")
except:
    print("Butun son kiritmadingiz")    

print("Dastur tugadi!")    
    

x,y=3,6
try:
    y/(x-3)
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmeydi")    




















