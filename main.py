# user puts whatever they want to calculate
# should print it out
# keep going until it says exit

#Change it so that user inputs num1 <operator> num2 instead of 3 separate ones

while True:

    calc_single_line = input("Enter the calculation (one-line or exit): ")

    if calc_single_line.lower() == "exit":
        print("Bye!")
        break

    parts = calc_single_line.split() #splits in array of separate items

    # Validate input
    if len(parts) != 3:
        print("Invalid format. Please type: number operator number")
        continue

    # Convert numbers
    try:
        num1 = float(parts[0]) #from parts, index 0 gets num1
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers. Please try again.")
        continue

#use switch statement in python instead of if statements when using one variable in this case: user_op
    match op:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                print("Error: cannot divide by zero")
                continue
            result = num1 / num2
        case "//":
            if num2 == 0:
                print("Error: cannot divide by zero")
                continue #cannot return, we not inside a function
            result = num1 // num2
        case "%":
            result = num1 % num2
        case unknown_command:
            print(f"Invalid operation: {unknown_command}")
            continue
    print(f"Result: {result}")

print("Thanks for using this calculator!")




