V = int(input("Enter the total vehicles"))
W = int(input("Enter the total wheels"))

y = (W - 2*V)//2
x = V- y
print(f"with this wheels we can make {x} cars and {y} bikes")
