with open("./InputOutput/mas.txt","w") as file:
    file.write("Helloo!\n")

with open("./InputOutput/mas.txt","r") as file:
    print(file.read())

name = input("Enter your Name: ")

with open("./InputOutput/mas.txt","a") as file:
    file.write(name)

with open("./InputOutput/mas.txt","r") as file:
    print(file.read())