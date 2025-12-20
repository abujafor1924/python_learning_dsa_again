
# 5️⃣ Shoelace Formula - Area of Triangle given coordinates
# Points: (x1,y1), (x2,y2), (x3,y3)
# Area = 0.5 * | x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) |





def triangle_area_coords(x1, y1, x2, y2, x3, y3):
    area = abs(
        x1*(y2 - y3) +
        x2*(y3 - y1) +
        x3*(y1 - y2)
    ) / 2
    return area

# Example usage
x1, y1 = 1, 2
x2, y2 = 4, 6
x3, y3 = 6, 3
print("Area of triangle:", triangle_area_coords(x1, y1, x2, y2, x3, y3))
