#Gas
#Developer: Jake Harback
#Version: 1.0

"""
Define a function to check our gas gauge and determine how far we have until we need gas based on an if, elif, else
condition
"""

#import library here
import random

#Gas level function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel 

