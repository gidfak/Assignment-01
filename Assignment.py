#Addition
number1 = int(input("Enter the first number for addition:"))
number2 = int(input("Enter the second number for addition"))
sum_results = number1 + number2
print(f" sum: {number1} + {number2} = {sum_results}")


#substraction
number1 = int(input("Enter first number for substrsction:"))
number2 = int(input("Enter second number for sustraction:"))
sub_result = number1 - number2
print(f"sub: {number1} - {number2} = {sub_result}")


#Division
number1 = int(input("Enter the first number for division:"))
number2 = int(input("Enter the second number for division:"))
if number2 == 0:
    print("Error: division by 0 is not allowed")
else:
    div_result = number1 / number2
    print(F" div: {number1} / {number2} = {div_result}")    




#Multiplication
number1 = int(input("Enter the first number for multiplication:"))
number2 = int(input("Enter the second number for multiplication"))
mult_result = number1 * number2
print(f"mult: {number1} * {number2} = {mult_result}")

#operators
operator_list = ("+", "-", "*" "/")
print(f"sum: {number1} + { number2} - {number1} - {number2}")
