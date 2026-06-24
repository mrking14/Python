# Write a program that keeps asking the user to enter a password until they
# enter the correct one.

password = "8581"

while(True):
    enteredPass = input("Enter your Password:")
    if(password == enteredPass):
        print("Your Password is Matched")
        break
    print("You've Entered wrong Password")