def find_quadrant(x, y):
    """
    (x, y) কোন quadrant-এ পড়ে তা রিটার্ন করে
    """

    if x > 0 and y > 0:
        return "1st Quadrant"
    elif x < 0 and y > 0:
        return "2nd Quadrant"
    elif x < 0 and y < 0:
        return "3rd Quadrant"
    elif x > 0 and y < 0:
        return "4th Quadrant"
    else:
        return "Point lies on axis"


# ---- main ----
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))
print(find_quadrant(x, y))
