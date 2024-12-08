# Get2 number
def get_numbers():
    while True:
        try:
            num1 = float(input("Enter num1:"))
            num2 = float(input("Enter num2:"))
            return num1, num2
        except ValueError:
            print("Invalid, please enter only numeric values.")

# operators
def calculator ():
    while True:
        # list of operators
        print("\n select operation:")
        print("1. Addition(+)")
        print("2. Substraction(-)")
        print("3. multiply (*)")
        print("4. Division (/)")
        print("5. exit")
        
        #get user choice
        choice = input("Enter your choice (1-5): ")
        if choice == '5':
            print("Thank you for using calculator")
            break
        
        #validate user choice
        if choice not in {'1', '2', '3', '4'}:
            print("invalid, please try again")
            continue

        #get number from users
        num1, num2 = get_numbers()
    

        #perform calculations
        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")

        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")

        elif choice == '3':
            print(f"Result {num1} * {num2} = {num1 * num2}") 

        elif choice == '4':
            if num2 == 0:
                print("Error: cannot divide by zero")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2} ")

#call calculator to function
calculator()

               
              



  

