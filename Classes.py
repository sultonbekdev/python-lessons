#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 20:19:31 2023

@author: aepeul
"""

class Talaba():
    def __init__(self,ism,familiya,tyil):
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
   
    def get_name(self):
        return self.ism    

    def get_lastname(self):
        return self.familiya
    
    def get_fullname(self):
        return f"Ismim {self.ism}, {self.familiya}"
    
    def get_age(self, yil):
        return yil-self.tyil





    # def tanishtir(self):
    #     print(f"Ismim {self.ism}, {self.familiya}. {self.tyil} da tug'ilgan! ")
        
talaba1=Talaba('Olim', "Xasanov", 2000)      
talaba2=Talaba("Sultonbek", "Batirov", 1995)  
# talaba1.tanishtir()        