import math

def calculate_moon_circumference():
    radius_moon = 1737.4  # in kilometers
    circumference = 2 * math.pi * radius_moon
    print("The radius of the moon is:", radius_moon, "km")
    print("The circumference of the moon is:", circumference, "km")

calculate_moon_circumference()