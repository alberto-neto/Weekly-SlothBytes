# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 23:55:29 2025

@author: alber
"""


numbers=[1,2,3,4,5,6,7,8,9,0]

def FormatPhoneNumber(numbers):
    
    area = "".join(map(str, numbers[0:3]))

    first3 = "".join(map(str, numbers[3:6]))
    
    last4 = "".join(map(str, numbers[6:10]))
    
    return f"({area}) {first3}-{last4}"

FormatPhoneNumber(numbers)
