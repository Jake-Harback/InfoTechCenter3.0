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






