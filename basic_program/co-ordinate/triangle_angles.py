


"""
তিনটি বাহু জানা থাকলে Cosine Rule ব্যবহার করে কোণ বের করা যায়।

সূত্র (Cosine Rule)

ধরা যাক বাহু তিনটি a, b, c

কোণ A (a-এর বিপরীতে):

# 1️⃣ Cosine Rule - Find Angles of a Triangle
# Given sides a, b, c:
# Angle A = acos((b^2 + c^2 - a^2) / (2*b*c))
# Angle B = acos((a^2 + c^2 - b^2) / (2*a*c))
# Angle C = acos((a^2 + b^2 - c^2) / (2*a*b))
Docstring for basic_program.co-ordinate.triangle_angles
"""

import math

def triangle_angles(a, b, c):
    A = math.degrees(math.acos((b*b + c*c - a*a) / (2*b*c)))
    B = math.degrees(math.acos((a*a + c*c - b*b) / (2*a*c)))
    C = math.degrees(math.acos((a*a + b*b - c*c) / (2*a*b)))
    return A, B, C

# Example usage
a, b, c = 5, 6, 7
angles = triangle_angles(a, b, c)
print("Angles of triangle:", angles)

