
try:
    #initialize a variable to store input from the user
    num_1 = int(input("Enter a number: "))
    #checking if the number is an even number or not and printing the result
    if num_1%2 == 0:
        print(f"{num_1} is an even number")

    else:
        print(f"{num_1} is an odd number")
except ValueError:
    print("Error: Please enter a valid integer.")
