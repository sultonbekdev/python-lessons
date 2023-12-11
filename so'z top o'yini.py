#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:50:13 2023

@author: aepeul
"""

import random
from uzwords import words

def get_word():
    word=random.choice(words)
    while "-" in word or " " in word:
        word=random.choice(words)
    return word.upper()                
        
def display(user_letter,word):
    display_letter=" "
    for letter in word:
        if letter in user_letter.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter 

def play() :
    word=get_word()
    word_letters=set(word)
    user_letters=''
    print(f"Men {len(word)} xonali son o'yladim. Topa olasizmi?")      
    while len(word_letters)>0:
        print(display(user_letters, word))
        if len(user_letters)>0:
            print(f"shu vaqtgacha kiritgan harfingiz {user_letters}")
        letter=input("harf kiriting: ").upper()
        if letter in user_letters:
            print("Bu harfni avval kiritgansiz. Boshqa harf kiriting!")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harfi to'g'ri.")
        else:
            print("Bundey harf yo'q.")
        user_letters += letter    
    print(f"Tabrikleyman! {word} so'zni {len(user_letters)} ta urinishda topdingiz!")    
            