# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:45:48 2021

@author: Tyler
"""


attempts = 1

while attempts <= 3:
    x = input("Enter your password:")
    
    if x == "password":
        print("Welcome in")
        break
    elif attempts==3:
        print("You are not allowed access to this computer!")
    else:
        print("Wrong password. Please try again.")
        
    attempts += 1