
#Task1- perform basic mathematical operation
try:
    # initialize variables and taking inputs from the user
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))

    #performing basic operations
    addition = first_num + second_num
    subtraction = first_num - second_num
    multiplication = first_num * second_num
    division = first_num / second_num

    #displaying the result
    print(f"addition: {addition}")
    print(f"subtraction: {subtraction}")
    print(f"multiplication: {multiplication}")
    print(f"division: {division}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
