class Square:
    def area(self, side):
        return side * side
class Circle:
    def area(self, radius):
        return 3.1416 * radius * radius
shape_type = input("Enter shape (square/circle):").strip().lower()
if shape_type == "square":
    s = float(input("Enter side length: "))
    shape = Square()
    print("Area:", shape.area(s))
elif shape_type == "circle":
    r = float(input("Enter radius: "))
    shape = Circle()
    print("Area:", shape.area(r))
else:
    print("Invalid shape")