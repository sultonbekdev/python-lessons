#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 13:17:47 2023

@author: aepeul
"""
def get_full_name(ism,familiya,otasi=''):
   if otasi:
       return f"{ism} {otasi} {familiya}".title()
   else:
       return f"{ism} {familiya}".title()