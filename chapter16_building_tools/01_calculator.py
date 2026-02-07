num1 = int(input("Pls Enter the First Num: "))

num2 = int(input("Pls Enter the Second Num: "))

opt = input("pls enter operation: ")


if opt == "+":
    total = num1 + num2
    print(f"addition is {total}")
elif opt == "-":
    total = num1 - num2
    print(f"subtract is {total}")

elif opt == "*":
    total = num1 * num2
    print(f"Multipy is {total}")

elif opt == "/":
    total = num1 / num2
    print(f"divide is {total}")

else:
    print("something wrong pls enter valid entities")

