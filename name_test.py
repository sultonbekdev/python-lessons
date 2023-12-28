#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 13:20:53 2023

@author: aepeul
"""

import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        formatted_name=get_full_name('sultonbek', 'batirov')
        self.assertEqual(formatted_name,'Sultonbek Batirov')
    
    def test_toliq_ism_otasi(self):
        name=get_full_name('orif', "oripov",'olimovich')
        self.assertEqual(name, 'Orif Olimovich Oripov')

unittest.main()
    