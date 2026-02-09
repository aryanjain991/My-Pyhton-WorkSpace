try:
    num1 = int(input("Pls Enter First Number: "))
    num2 = int(input("Pls Enter second Number: "))

    print("what kind of operation u want to perform options are:\n for addition use + \n for subtraction use - \n for multiplication use * \n and for divide use / \n")

    opt = input("Pls Enter a Operation: ")

    match opt:
        case "+":
            print("Adition is: ", num1 + num2)
        case "-":
            print("subtract is: ", num1 - num2)
        case "*":
            print("multiplication is: ", num1 * num2)
        case "/":
            print("division is: ", num1 / num2)
        case default:
            print("there is an error")

except Exception as e:
    print("pls write a valid ")