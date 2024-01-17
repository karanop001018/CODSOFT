def calc(operation, num1, num2):
    if operation == "+":
        return num1+num2;
    elif operation == "-":
        return num1-num2;
    elif operation == "*":
        return num1*num2;
    elif operation == "/":
        return num1/num2;
    elif operation == "%":
        return num1%num2;
    else:
        return "Invalid Operation";
    
    
# Test the function with different operations and numbers.
operation = input('Choose an operation from given:"+,-,*,/,%"');
num1 = float(input("Enter first number:"));
num2 = float(input("Enter second number:"));
print("Result is :",calc(operation,num1,num2));