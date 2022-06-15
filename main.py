import math


# Lorentz factor calculation
def lorentz(v):
    c = 3 * 10 ** 8
    return 1 / math.sqrt(1 - (v ** 2 / c ** 2))


# Modes
mode = 0
modes = {
    "Mode 0: Calculate the Lorentz factor with a given speed",
    "Mode 1: Calculate the Lorentz factor with a given light speed multiplier"
}
# Print available modes
for s in modes:
    print(s)
# Get the selected mode
mode = input("Select the desired mode: ")
mode = int(mode)

# Select the mode accordingly to the user input
if mode == 0:
    print("Calculate the Lorentz factor with a given speed")
    vel = input("Insert the speed: ")
    lor = lorentz(float(vel))
    print("The calculated Lorentz factor is: " + str(lor))
if mode == 1:
    lightspeed = 3 * 10 ** 8
    print("Calculate the Lorentz factor with a given light speed multiplier")
    vel = input("Insert the light speed multiplier: ")
    lor = lorentz(float(vel)*lightspeed)
    print("The calculated Lorentz factor is: " + str(lor))
