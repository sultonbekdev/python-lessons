#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:35:58 2023

@author: aepeul
"""

class Shaxs:
    def __init__(self,ism,familiya,passport,tyil):
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil
    
    def get_info(self):
        info=f"{self.ism} {self.familiya}. "
        info += f"Pasport: {self.passport}, {self.tyil}-yilda tug'ilgan"
        return info
    def get_age(self,yil):
        return yil-self.tyil
inson=Shaxs("Sultonbek", "Batirov", "AA4683068", 1995)
print(f"{inson.get_info()} {inson.get_age(2023)} yoshda.")

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

# talaba=Talaba("Ahat", "Kamilov", "AA12345567", 1989, "Q0102033")
# print(talaba.get_info())

class Manzil:
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy=uy
        self.kocha=kocha
        self.tuman=tuman
        self.viloyat=viloyat
        
    def get_manzil(self):
        manzil=f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil +=f"{self.kocha} kochasi, {self.uy}-uy"
        return manzil

talaba_manzil = Manzil(12,'Olmazor',"Bog'bon","Samarqand")
talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)
print(talaba.manzil.get_manzil())
print(talaba.manzil.tuman)
    
        
        
        
        
        
        
        
        
        
        
        
# talaba=Talaba("Hasan", "Husanov", "AA2341212", 1999, 19950901)    
# print(f"{talaba.get_info()}. ID raqam: {talaba.get_id()} ")
# print(f"{talaba.get_bosqich()}-bosqich talabasi")
        

# talaba=Talaba("Ali", "Valiyev","FA1036789", 2023)      
# print(talaba.get_info())  
# print(talaba.get_age(2023))
 
        