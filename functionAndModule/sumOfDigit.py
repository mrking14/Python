# Write a recursive function sum_of_digits(n) that returns the sum of all digit of a given number.

def sum_of_digit(num):
    if(num==0):
        return 0
    return num%10 + sum_of_digit(num//10)

number = int(input("Enter Digits to Sum Of them: "))

print(sum_of_digit(number))