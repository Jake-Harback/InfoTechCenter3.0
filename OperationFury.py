#Gas
#Developer: Jake Harback
#Version: 1.0

"""
Define a function to check our gas gauge and determine how far we have until we need gas based on an if, elif, else
condition
"""

#import library here
import random
from time import sleep

#Gas level function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Variable calling the gasLevelGauge function to store value once
gasLevelIndicator = gasLevelGauge()

def gasLevelAlert():
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***\n")
        sleep(1)
        print("Calling Emergency Contact")

gasLevelAlert()


