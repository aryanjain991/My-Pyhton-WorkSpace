
age = int(input("please Enter Your Age: "))
flight_type = input("Please Write Flight Type: ")

if age < 25:
    if flight_type == "international":
        price = 5000
        print(f"Flight Type is International so the price is: {price}Rs.")

    else:
        print("Check your program again someting wrone")    

else:
    print("something wrong pls check your code")
