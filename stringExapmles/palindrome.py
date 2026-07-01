text = input("Enter word to check Pelindrome: ")
reText = text[::-1]

if text ==reText:
    print("This word is pelindrome!")
else:
    print("This Text is not a pelindrome!")