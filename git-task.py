# ****calc_app.py task****

# Infinite loop to repeatedly ask for input until valid input is given
while True:
    try:
        # Ask the user for the first number and convert it to a float
        number_1 = float(input("Enter the first number: "))
        break  # exit the loop if input is valid
    except ValueError:
        # Handles the case where the user enters something that is not a number
        print("Invalid input. Please enter a number.")

# try-except allows the program to continue instead of crashing,
# should the user input a character that is not a number 

# Infinite loop to repeatedly ask for the second number until valid input is given
while True:
    try:
        # Ask the user for the second number and convert it to a float
        number_2 = float(input("Enter the second number: "))
        break  # exit the loop if input is valid
    except ValueError:
        # Handles invalid (non-numeric) input
        print("Invalid input. Please enter a number.")

# Ask the user which mathematical operation they want to perform
operation = input("Enter one of the following operation, '+', '-','x' or /")

# Check if the chosen operation is addition
if operation == "+":
  # Perform addition
  result_1 = number_1 + number_2
  # Display the result
  print(result_1)
  # Open the equations.txt file in append mode
  with open("equations.txt", "a") as file:
    # Write the equation and result to the file
    file.write(f"{number_1} + {number_2} = {result_1}\n")

# Check if the chosen operation is subtraction
elif operation == "-":
    # Perform subtraction
    result_2 = number_1 - number_2
    # Display the result
    print(result_2)
    # Append the equation and result to the file
    with open("equations.txt", "a") as file:
        file.write(f"{number_1} - {number_2} = {result_2}\n")

# Check if the chosen operation is multiplication
elif operation == "x":
    # Perform multiplication
    result_3 = number_1*number_2
    # Display the result
    print(result_3)
    # Append the equation and result to the file
    with open("equations.txt", "a") as file:
        file.write(f"{number_1} x {number_2} = {result_3}\n")
        
# Check if the chosen operation is division
elif operation == "/":
    try:
        # Attempt to divide the two numbers
        result_4 = number_1/number_2
        # Display the result
        print(result_4)
    except ZeroDivisionError:
         # Handles division by zero so the program does not crash
         print("Cannot compute division by zero")
    try:
       # Attempt to write the division result to the file
       with open("equations.txt", "a") as file:
         file.write(f"{number_1}/{number_2} = {result_4}")
    except FileNotFoundError:
        # Handles the case where the result could not be written
        print("Cannot capture, as divison by zero cannot compute")

# Executes if the user enters an invalid operation
else:
    print("Enter a valid operation")