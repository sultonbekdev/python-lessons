#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 18:11:30 2023

@author: aepeul
"""

from uuid import uuid4

class Avto:
    
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
   
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        if km >= 0:
            self.__km += km
        else:
            print("Moshinani km kamaytirib bo'lmaydi.")
            
    def __repr__(self):
        return f"Avto: {self.rang} {self.make} {self.model}"
    
    def __lt__(self,y):
        return self.narh<y.narh
        
            
avto1=Avto("GM", "Malibu", "qora", 2019, 34000)
avto2=Avto("GM", "Lacetti", "oq", 2019, 24000)    
avto1.add_km(1100)
print(avto1.get_km())

class Avtosalon:
    def __init__(self,name):
        self.name=name
        self.avtolar=[]
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
salon1=Avtosalon("SultanAvto")  
print(salon1)  
    
    
    
    
    
    
    