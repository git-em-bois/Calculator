while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    selection = input("Please select from the above. \n")

    if selection in ("1", "2", "3", "4", "5"):
        Input1 = input("First number? \n")
        while isinstance(Input1, float):
            print("Not a number. Please try again. \n")
            Input1 = input("First number? \n")
        Input2 = input("Last number? \n")
        while isinstance(Input2, float):
            print("Not a number. Please try again. \n")
            Input2 = input("Last number?")

        Input1 = float(Input1)
        Input2 = float(Input2)
        if selection == "1":
            print("\n", Input1, "+", Input2, "=", Input1 + Input2, "\n")
        elif selection == "2":
            print("\n", Input1, "-", Input2, "=", Input1 - Input2, "\n")
        elif selection == "3":
            print("\n", Input1, "x", Input2, "=", Input1 * Input2, "\n")
        elif selection == "4":
            print("\n", Input1, "÷", Input2, "=", Input1 / Input2, "\n")
        elif selection == "5":
            break
    else:
        print("\nInvalid. Please try again.\n")
