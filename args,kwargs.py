#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:58:37 2023

@author: aepeul
"""
# def summa(*sonlar):
#     return sum(sonlar)
# print(summa(4,5,6,7))

# def summa(x,y,*sonlar):
#     return x+y+sum(sonlar)
# print(summa(2, 13,1,2))

# def avto_info(kompaniya,model,**malumotlar):
#     malumotlar['compani']=kompaniya
#     malumotlar['madel']=model
#     return malumotlar
# avto1=(avto_info("GM", 'malubu',yili=2018, narhi=34000))
# avto2=(avto_info('Kia', 'k5', karobka='avtomat',narhi=41000))
# print(avto1)

# def multiple(*sonlar):
#     kopaytma=1
#     for son in sonlar:
#         kopaytma *= son
#         return kopaytma    
# print(multiple(4,5,6))

def talaba_info(ism,familiya,**talabalar):
    talabalar['ism']=ism
    talabalar['familiya']=familiya
    return talabalar
talaba1=talaba_info('ali', "valiyev", yoshi=28, kasbi='duradgor')
talaba2=talaba_info('sultonbek', 'batirov', yoshi=28, kasbi='programist')
print(talaba1)    
print(talaba2)










