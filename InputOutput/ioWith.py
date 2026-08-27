with open("./InputOutput/lol.txt", "w") as file:
   file.write("Hello! Masoom Raza this Side.")

with open("InputOutput/lol.txt", "r") as file:
   content = file.read();

print(content)