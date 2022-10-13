
#*****************************************************************************************************************
#Import Libraries here
from time import sleep #We imported the sleep function from the time library

import random
#*****************************************************************************************************************

#Welcome Screen
#Developer: Jake Harback
#Version: 1.0

"""
Our Welcome Screen will start our program letting drivers know that the InfoTechCenter OS is Loading
"""


#Code to print a different color
#print("\033[1;36m This text is Bright Green\n\033[0m")

print("\n\n\033[1;36m Welcome to Operation Fury InfoTech Center")
sleep(1.5)
print("\n\033[1;36m Operation Fury's Operating System is Booting Up\n\033[0m")
sleep(1.5)
for i in range(8):
    print("OS Booting Up\n")
    sleep(1)


#Gas
#Developer: Jake Harback
#Version: 1.0

"""
Define a function to check our gas gauge and determine how far we have until we need gas based on an if, elif, else
condition
"""

def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Variable calling the gasLevelGauge function to store value once
gasLevelIndicator = gasLevelGauge()

def listOfGasStations():
    gasStation = ["Shell","Circle K","Marathon","Speed Way","Meijer"]
    gasStationNearby = random.choice(gasStation)
    return gasStationNearby

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarterTank = round(random.uniform(26, 50), 1)
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***\n")
        sleep(1)
        print("Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***Warning***")
        sleep(1)
        print("Your gas tank is extremely low, checking Google Maps for closest gas station")
        sleep(1)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("***Warning***")
        sleep(1)
        print("You only have a Quarter Tank left, checking Google Maps for closest gas station")
        sleep(1)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("You have a half a tank of gas, plenty of gas to get where you need to")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is Three Quarters full, plenty of gas to get where you are going")
    else:
        print("Your gas tank is full, have a nice drive")


#Weather
#Developer: Jake Harback
#Version: 1.0


"""
Create a function for our current weather using the random.choice function to determine what the weather is picking
from a list - using If, Elif & Else statements to check the condition and print a print line
"""

#Weather condition list using the random.choice library to randomly choose a condition and storing it in its brain
def weather():
    weatherForcast = ["Rain","Snow","Sunny","Windy","Foggy","Storming","Icy"]
    weatherCondition = random.choice(weatherForcast)
    print(weatherCondition)
    return weatherCondition

weatherAlert = weather()
def vehicleResponseSystem():
    if weatherAlert == "Icy":
        print("\nVRS has changed your Alarm 30 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snow":
        print("\nVRS has changed your Alarm 15 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    elif weatherAlert == "Rain":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Windy":
        print("\nVRS has not changed your Alarm based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 70MPH")
    elif weatherAlert == "Foggy":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Storming":
        print("\nVRS has changed your Alarm 15 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    else:
        print("\nThe weather today is",weatherAlert, "let's Gooo!")
        print("VRS will only allow your car to go 100MPH")


#*****************************************************************************************************************

#Call Functions Here...


vehicleResponseSystem()
print("")
gasLevelAlert()


