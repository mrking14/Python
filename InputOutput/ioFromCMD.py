name = input("Enter Your Name: ")
contact = input("Enter your Contact:")

file = open("./InputOutput/newTextr.txt", "w")

details = f"Your Name is {name} and Your Contact number is: {contact}"

file.write(details)

file.close()

f = open("./InputOutput/newTextr.txt", "r")
print(f.read())
f.close()

