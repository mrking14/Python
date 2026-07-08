# Write a Recursive Function Factorial(n) thats Return factorial of N number.

def factorial(num):
    if(num ==0 |  num ==1):
        return 1
    
    return(factorial(num-1)*num)

number = int(input("Enter number to Get Factorial: "))

print(factorial(number))

