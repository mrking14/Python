number1 = int(input("Enter 1st Number to calculate: "))
number2 = int(input("Enter 2st Number to calculate: "))

calculation = input("Enter Expression to calculate: ")

match calculation:
    case '+': print("Addition of Given number is: ",number1+number2)
    case '-': print("Substraction of Given Number is: ",number1-number2)
    case '*': print("Multpication of Given Number is: ",number1*number2)
    case '/': print("Division of Given numbers is: ",number1/number2)
