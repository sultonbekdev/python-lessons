#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:09:43 2023

@author: aepeul
"""

# def bahola(ismlar):
#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho=input(f"Talaba {ism.title()}ning bahosini kiriting! ")
#         baholar[ism]=int(baho)
#     return baholar
# talabalar=['sultonbek','abdulxamid','xojiakbar','shahzod']
# baholar=bahola(talabalar[:])
# print(baholar)
# print(talabalar)
# def katta_harflar(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
# ismlar=['ali','vali','hasan','husan']        
# katta_harflar(ismlar)
# print(ismlar)

def katta_harflar(matnlar):
    matnlar=matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
        return matnlar
ismlar=['ali','vali','hasan','husan']        
yangi_harflar=katta_harflar(ismlar)
print(ismlar)
print(yangi_harflar)