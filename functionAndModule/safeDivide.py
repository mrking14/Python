def safeDivide(a,b):
    if b==0:
        print("Can not Divide by Zero")
        return
    result = a/b
    print(f"Result is: {result}")

num1 = int(input("Enter Fist Number: "))
num2 = int(input("Enter Second Number: "))

safeDivide(num1,num2)