# user puts whatever they want to calculate
# should print it out
# keep going until it says exit

while True:
    user_op = input("Put in your operation (+,-,*,/,% or exit): ")
    if user_op == "exit":
        print("Bye!")
        break

    user_num1 = int(input("Put in your first number: "))

    user_num2 = int(input("Put in your second number: "))

#use switch statement in python instead of if statements when using one variable in this case: user_op
    match user_op:
        case "+":
            result = user_num1 + user_num2
        case "-":
            result = user_num1 - user_num2
        case "*":
            result = user_num1 * user_num2
        case "/":
            result = user_num1 / user_num2
        case "//":
            result = user_num1 + user_num2
        case "%":
            result = user_num1 + user_num2
        case unknown_command:
            print(f"Invalid operation: {unknown_command}")
            continue
    print(f"Result: {result}")

print("Thanks for using this calculator!")




