# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:45:48 2021

@author: Tyler
"""
actualPassword = 'password'

attempts = 1

while True:
    x = input("Enter your password:")
    
    if x == actualPassword:
        print("Welcome in")
        break
    elif attempts==3:
        print("You are not allowed access to this computer!")
        break
    else:
        print("Wrong password. Please try again.")
        
    attempts += 1