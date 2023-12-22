#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 17:16:46 2023

@author: aepeul
"""
import json

# x=10
# x_json = json.dumps(x)

# ism='anvar'
# ism_json = json.dumps(ism)

# bemor={
#        "ism":"Batirov Sultonbek",
#        "yosh":28,
#        "oila":True,
#        "farzandlar":("Ahmad","Bonu"),
#        "alergiya": None,
#        "dorilar": [
#            {"nomi":"Analgin","miqdori":0.5},
#            {"nomi":"Panadol","miqdori":1.2}
#            ]
#        }

# with open('bemor_json', 'w') as f:
#     json.dump(bemor,f)

# bemor_json = json.dumps(bemor, indent=4)
# print(bemor_json)
# bemor = json.loads(bemor_json)
# print(bemor)

# data = {"Model": "Malibu", "Rang": "Qora", "Yil": 2020, "Narh": 40000}
# a=json.dumps(data, indent=4)
# print(a)

talaba_json ={"ism":"Hasan","familiya":"Husanov","tyil":2000}

talaba = json.loads(talaba_json)
print(f"{talaba['ism']} {talaba['familiya']}")






# filename = 'bemor.json'
# with open(filename) as f:
#     bemor=json.load(f)
# print(type(bemor))    

{
    "address_components": [
        {
            "long_name": "Almazar District",
            "short_name": "Almazar District",
            "types": [
                "political",
                "sublocality",
                "sublocality_level_1"
            ]
        },
        {
            "long_name": "Tashkent",
            "short_name": "Tashkent",
            "types": [
                "locality",
                "political"
            ]
        },
        {
            "long_name": "Tashkent Region",
            "short_name": "Tashkent Region",
            "types": [
                "administrative_area_level_1",
                "political"
            ]
        },
        {
            "long_name": "Uzbekistan",
            "short_name": "UZ",
            "types": [
                "country",
                "political"
            ]
        }
    ],
    "formatted_address": "Almazar District, Tashkent, Uzbekistan",
    "geometry": {
        "bounds": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        },
        "location": {
            "lat": 41.3645355,
            "lng": 69.2281531
        },
        "location_type": "APPROXIMATE",
        "viewport": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        }
    },
    "place_id": "ChIJ195FnkeMrjgR3nkapKKdk7A",
    "types": [
        "political",
        "sublocality",
        "sublocality_level_1"
    ]
}