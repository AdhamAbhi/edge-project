def calculator():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("A. Addition")
    print("S. Subtraction")
    print("M. Multiplication")
    print("D. Division")

    while True:
        try:
            # Get user input
            choice = input("Enter the number of the operation you'd like to perform (A/S/M/D): ")

            # Validate input
            if choice not in ('A', 'S', 'M', 'D'):
                print("Invalid input. Please choose a valid operation.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform operations
            if choice == 'A':
                print(f"The result of addition: {num1} + {num2} = {num1 + num2}")
            elif choice == 'S':
                print(f"The result of subtraction: {num1} - {num2} = {num1 - num2}")
            elif choice == 'M':
                print(f"The result of multiplication: {num1} * {num2} = {num1 * num2}")
            elif choice == 'D':
                if num2 == 0:
                    print("Division by zero is not allowed.")
                else:
                    print(f"The result of division: {num1} / {num2} = {num1 / num2}")

            # Ask if the user wants to perform another operation
            next_calculation = input("Would you like to perform another calculation? (yes/no): ").lower()
            if next_calculation != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter numeric values for the numbers.")

if __name__ == "__main__":
    calculator()
