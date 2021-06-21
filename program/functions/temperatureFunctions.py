# -*- coding: utf-8 -*-

"""
    Functions:
        - convert_celcius_to_kelvin
        - convert_kelvin_to_celcius
        - convert_kelvin_to_fahrenheit
"""

import sys
import os

currDir = os.path.dirname(os.path.abspath(__file__))
print(currDir)
sys.path.append(currDir)
sys.path.append(currDir + "/../" + "constants")

import constants

def convert_celcius_to_kelvin(temperatureC):
    """
    Convert Temperature from degrees Celcius to Kelvin
    
    Input Parameters:
        -temperatureC: (float) temperate in degrees Celcius
    
    Returned Value:
        -converted temperature in degrees Kelvin
    """
    return temperatureC + constants.zeroCelcius

def convert_kelvin_to_celcius(temperatureK):
    """
    Convert Temperature from degrees Kelvin to Celcius
    
    Input Parameters:
        -temperatureK: (float) temperate in degrees Kelvin
    
    Returned Value:
        -converted temperature in degrees Celcius
    """
    return temperatureK - constants.zeroCelcius 

def convert_kelvin_to_fahrenheit(temperatureK):
    """
    Convert Temperature from degrees Kelvin to fahrenheit
    
    Input Parameters:
        -temperatureK: (float) temperate in degrees Kelvin
    
    Returned Value:
        -converted temperature in degrees fahrenheit
    """
    return 9.0/5.0 * (temperatureK - constants.zeroCelcius) + 32.0
    
    
if __name__ == '__main__':
    print(convert_celcius_to_kelvin(15.7))
    print(convert_kelvin_to_celcius(302.9))
    print(convert_kelvin_to_fahrenheit(302.9))