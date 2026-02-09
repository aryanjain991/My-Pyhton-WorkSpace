questions = [
    ["What is Python?", "Database", "Programming language", "Hardware device", "Operating system", 2],
    ["Which symbol is used for comments in Python?", "/* */", "//", "<!-- -->", "#", 4],
    ["Which is a valid variable name in Python?", "name-1", "name@", "name_1", "1name", 3],
    ["Which data type stores True or False?", "float", "string", "bool", "int", 3],
    ["Which function takes user input?", "scan()", "input()", "get()", "read()", 2],
    ["Which loop is used when iterations are known?", "do-while", "if", "while", "for", 4],
    ["What is the output of 2 + 3 * 4?", "24", "10", "20", "14", 4],
    ["Which keyword is used to define a function?", "define", "fun", "function", "def", 4],
    ["Which is a mutable data type?", "int", "list", "tuple", "string", 2],
    ["Which operator is used for equality comparison?", "!=", "=", "<=", "==", 4]
]

prizes = [10000, 20000, 50000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
i = 0
for quetion in questions:
    print(quetion[0])
    print(f"a. {quetion[1]}")
    print(f"b. {quetion[2]}")
    print(f"c. {quetion[3]}")
    print(f"d. {quetion[4]}")

    # check whether the answer is correct or not

    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d = " ))

    if (quetion[5] == a):
        print("Correct Answer")
    else:
        print(f"Incorrect, the correct answer was {quetion[5]}")
        print("Better luck next time")
        break
    print(f"You won {prizes[i]}")
    i+=1