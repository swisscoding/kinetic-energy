#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Calculate kinetic energy | ----\n", fg("red")))

# function
def calculate(mass, velocity):
        return round(1/2*mass*(velocity**2), 1)

# user interaction
mass = float(input("Enter the mass in kg: "))
velocity = float(input("Enter the velocity in m/s: "))

ke = stylize(calculate(mass, velocity), fg("red"))
print(f"\nCalculated kinetic energy in Joules: {ke}\n")
