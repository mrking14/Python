import os
import shutil

for ls in os.listdir("InputOutput"):
    print(ls)

os.remove("./InputOutput/oSPractice/loll.txt")

os.mkdir("./InputOutput/oSPractice/laala")
os.rmdir("./InputOutput/oSPractice/laala")
shutil.rmtree("./InputOutput/oSPractice/laala")

shutil.copy("./InputOutput/oSPractice/lol.txt", "./InputOutput/oSPractice/lolas.txt")
