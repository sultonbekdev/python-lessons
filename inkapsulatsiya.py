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
            
avto1=Avto("GM", "Malibu", "qora", "2019", 34000)    
avto1.add_km(1100)
print(avto1.get_km())
    
    
    
    
    
    