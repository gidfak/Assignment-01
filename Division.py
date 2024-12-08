#Division
number1 = int(input("Enter the first number for division:"))
number2 = int(input("Enter the second number for division:"))
if number2 == 0:
    print("Error: division by 0 is not allowed")
else:
    div_result = number1 / number2
    print(F" div: {number1} / {number2} = {div_result}")    
