def perimeter(l, b):
    return (l + b) * 2

def area(l, b):
    return l * b
print("Rectangle Calculator")
l = (int(input("Length: ")))
b = (int(input("Breadth: ")))
print(f"Perimeter: {perimeter(l, b)}")
print(f"Area: {area(l, b)}")
