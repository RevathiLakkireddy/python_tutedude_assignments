import math
try:
    x = int(input("Enter a number: "))
    print(f"square root: {math.sqrt(x)}")
    print(f"logarithm: {math.log(x)}")
    print(f"sine: {math.sin(x)}")

except ValueError:
    print("please enter a valid number")