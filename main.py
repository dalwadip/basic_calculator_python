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

    if user_op == "+":
        result = user_num1 + user_num2
    elif user_op == "-":
        result = user_num1 - user_num2
    elif user_op == "*":
        result = user_num1 * user_num2
    elif user_op == "/":
        result = user_num1 / user_num2
    elif user_op == "//":
        result = user_num1 // user_num2
    elif user_op == "%":
        result = user_num1 % user_num2
    else:
        print("Invalid operation")
        continue #skips this iteration and goes back to top of while loop
    print("Result:", result)

print("Thanks for using this calculator!")




