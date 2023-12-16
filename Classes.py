#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 20:19:31 2023

@author: aepeul
"""
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
    
    # def get_info(self):
    #     """Talaba haqida ma'lumot"""
    #     return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
    # def set_bosqich(self,bosqich):
    #     """Talabaning kursini yangilovchi metod"""
    #     self.bosqich = bosqich
        
    # def update_bosqich(self):
    #     self.bosqich += 1        

# talaba1 = Talaba("Sultonbek",'Batirov',1995)
# talaba1.update_bosqich()
# print(talaba1.get_info())

# talaba1.bosqich=2
# print(talaba1.bosqich)

# class Fan():
#     def __init__(self,nomi):
#         self.nomi=nomi
#         self.talabalar_soni=0
#         self.talabalar=[]
        
#     def add_student(self,talaba):
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1  
        
#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]

# matematika=Fan("Oliy matematika")
# talaba1=Talaba("Alisher", "Muzaffarov", 1993)
# talaba2=Talaba("Zuxriddin","Xasanov", 1994)
# talaba3=Talaba("Abdulxamid", "Norov", 1995)

# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# print(matematika.talabalar_soni)

# mat_talabalar = matematika.get_students()
# print(mat_talabalar)

# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(Talaba))

# class Talaba():
#     def __init__(self,ism,familiya,tyil):
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
#         self.bosqich=1
   
#     def get_name(self):
#         return self.ism    

#     def get_lastname(self):
#         return self.familiya
    
#     def get_fullname(self):
#         return f"Ismim {self.ism}, {self.familiya} {self.bosqich} bosqich talabasi."
    
#     def get_age(self, yil):
#         return yil-self.tyil
    
#     def set_bosqich(self,yangi_bosqich):
#          self.bosqich = yangi_bosqich 

    # def tanishtir(self):
    #     print(f"Ismim {self.ism}, {self.familiya}. {self.tyil} da tug'ilgan! ")
        
# talaba1=Talaba('Olim', "Xasanov", 2000)      
# talaba2=Talaba("Sultonbek", "Batirov", 1995)  
# # talaba1.tanishtir()   

class Avto:
    def __init__(self, model,rang,karobka,narh):
        self.model=model
        self.rang=rang
        self.karobka=karobka
        self.narh=narh
        self.kilometr=0
        
    def get_info(self):
        return f"{self.model} {self.rang} {self.karobka} {self.narh} kilometri {self.kilometr} km teng!"
    
    def update_km(self):  
        self.kilometr += 1

          
avto1=Avto("Kia", "qora", "avtomat", 24000) 
avto1.update_km()
#print(avto1.get_info())  

class Avtosalon():
    def __init__(self,nomi,manzili,):
        self.nomi=nomi
        self.manzili=manzili
        self.sotuvdagi_avto=0
        self.yangi_avto=[]
        
    def add_avto(self,avto):
        self.yangi_avto.append(avto)
        self.sotuvdagi_avto += 1
        
    def get_avtos(self):
        return [avto.get_info() for avto in self.yangi_avto]    
        
car=Avtosalon('Star Avto', "Bekabod")
avto1=Avto('Kia', 'sariq', "mexanika", 40000)      
avto2=Avto('Hyundai', 'qora', "avtomat", 34500) 
avto3=Avto('BMW', 'Oq', "avtomat", 48000) 

car.add_avto(avto1)
car.add_avto(avto2)
car.add_avto(avto3)

mobil=car.get_avtos()
print(mobil)






                        
        
    






















     