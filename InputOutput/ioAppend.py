file = open("./InputOutput/masoom.txt", "a")
number = 10;
message = f"{number}, I am From Muzaffarpur, Bihar"
number = number+1
file.write(message +"\n")
file.close()

file = open("./InputOutput/masoom.txt", "r")
print(file.read())
file.close()

