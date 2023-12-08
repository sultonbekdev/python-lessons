#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 19:49:23 2023

@author: aepeul
"""

# import math
# uzunlik=lambda pi,r: 2*pi*r
# print(uzunlik(math.pi,10))

# kvadrat=lambda x,y: x**y
# print(kvadrat(3,4))

# def daraja(n):
#     return lambda x: x**n
# kvadrat=daraja(2)
# kub=daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga kubi esa {kub(3)} ga teng!")

# from math import sqrt
# sonlar=list(range(11))
# # ildizlar=list(map(sqrt, sonlar))
# # print(ildizlar)

# def daraja2(x):
#     return x*x
# print(daraja2(3))
# print(list(map(daraja2, sonlar)))

# kvadratlar=list(map(lambda x: x*x, sonlar))
# print(kvadratlar)

# a=[7,5,3]
# b=[2,6,8]
# a_plus_b=list(map(lambda x,y: x+y, a,b))
# print(a_plus_b)

# import random as r 
# sonlar=r.sample(range(100), 10)
# # def juftmi(x):
# #     return x%2==0
# # juft_sonlar=list(filter(juftmi, sonlar)) #yoki lambda bo'yicha
# juft_sonlar=list(filter(lambda x: x%2==0, sonlar))
# print(juft_sonlar)


mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva: meva.startswith('a'), mevalar))
mevalar2=list(filter(lambda meva: len(meva)<=5, mevalar))
fruits=list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
print(mevalar_b)
print(mevalar2)
print(fruits)





















