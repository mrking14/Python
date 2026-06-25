text = input("Enter any text to Reverse: ")
revString=""

for i in range(1,len(text)+1):
    revString+=text[-i]

print("Reversed String is : ",revString)


name= input("Enter your Name: ")
revName = name[::-1]

print(revName)

