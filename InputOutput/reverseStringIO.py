text = input("Enter text to save in file: ")


with open("./InputOutput/text.txt","w") as file:
    file.write(text)

with open("./InputOutput/text.txt","r") as ile:
    content = ile.read()

print("You content from file is : "+ content)
revContent = content[::-1]

with open("./InputOutput/revText.txt","w") as file:
    file.write(revContent)



