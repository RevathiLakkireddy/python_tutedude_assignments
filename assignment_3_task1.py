def factorial(i):
    result = 1
    for num in range(1,i+1):
        result = result*num
    print(f"Factorial of {i} is: {result}")


try:
    i = int(input('Enter a number: '))
    if i<0:
        print("Please enter a valid non-negative integer.")
    else:
        factorial(i)

except ValueError:
    print("Please enter a valid non-negative integer.")

