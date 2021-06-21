# -*- coding: utf-8 -*-
import sys
import os

currDir = os.path.dirname(os.path.abspath(__file__))
print(currDir)
sys.path.append(currDir)
sys.path.append(currDir + "/../" + "functions")

import temperatureFunctions as tf




temperatureC = 15.7
temperatureK = tf.convert_celcius_to_kelvin(temperatureC)
print(f"{temperatureC} degree Celcius is equal to {temperatureK} degree Kelvin")

temperatureK = 302.9
temperatureC = tf.convert_kelvin_to_celcius(temperatureC)
print(f"{temperatureK} degree Kelvin is equal to {temperatureC} degree Celcius")

temperatureF = tf.convert_kelvin_to_fahrenheit(temperatureK)
print(f"{temperatureK} degree Kelvin is equal to {temperatureF} degree Fahrenheit")

