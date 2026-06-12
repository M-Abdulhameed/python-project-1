print("Welcome to digital calculator\n")

while True:
    n1 = float(input("Enter number 1: "))
    n2 = float(input("Enter number 2: "))

    print("\nPress 1 to Add")
    print("Press 2 to Subtract")
    print("Press 3 to Multiply")
    print("Press 4 to Divide")

    a = int(input("Enter your choice: "))

    if a == 1:
        print("Result:", round(n1 + n2, 2))

    elif a == 2:
        print("Result:", round(abs(n1 - n2), 2))

    elif a == 3:
        print("Result:", round(n1 * n2, 2))

    elif a == 4:
        if n2 == 0:
            print("Error: can't divide by zero ❌")
        else:
            print("Result:", round(n1 / n2, 2))

    else:
        print("Please enter a valid choice ❗")
        print("Calculator restarted...\n")
        continue

    again = input("\nDo you want to continue (yes/no): ").lower()

    if again == 'yes':
        print("Continuing...\n")

    elif again == 'no':
        print("Thanks for using the calculator 👋")
        break

    else:
        print("Invalid input, exiting ❌")
        break