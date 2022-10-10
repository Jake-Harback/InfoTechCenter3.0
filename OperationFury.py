
#Welcome Screen
#Developer: Jake Harback
#Version: 1.0

"""
Our Welcome Screen will start our program letting drivers know that the InfoTechCenter OS is Loading
"""

#Import Libraries here
from time import sleep #We imported the sleep function from the time library

print("\n\n\033[1;36m Welcome to Operation Fury InfoTech Center")
sleep(1.5)
print("\n\033[1;36m Operation Fury's Operating System is Booting Up\n\033[0m")
sleep(1.5)

#Code to print a different color
#print("\033[1;36m This text is Bright Green\n\033[0m")


for i in range(8):
    print("OS Booting Up")
    sleep(1)





#Weather
#Developer: Jake Harback
#Version: 1.0

"""
Create a function for our current weather using the random.choice function to determine what the weather is picking
from a list - using If, Elif & Else statements to check the condition and print a print line
"""

#Import Libraries here
import random

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

vehicleResponseSystem()

