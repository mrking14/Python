number = input("Enter Number to Check it is Pelindrome:")
revNumber= number[::-1]

number = int(number)
revNumber= int(revNumber)

if number == revNumber:
    print("This given Number is Pelindrom Number!")
else:
    print("This given Number is not a pelindromre!")