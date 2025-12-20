

"""
Calculate the area using Heron’s Formula:


# 2️⃣ Heron's Formula - Area of Triangle given sides
# s = (a + b + c) / 2
# Area = sqrt(s * (s - a) * (s - b) * (s - c))

Docstring for basic_program.co-ordinate.triangle_area_coords
"""


import math

def triangle_area_sides(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Example usage
a, b, c = 5, 6, 7
print("Area of triangle:", triangle_area_sides(a, b, c))
