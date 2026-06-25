text = " i love python programming "

# Removing Text from both Side
print(text.strip())


# Convert it to title case
print(text.title())


# Count how many times "o" appears
print(text.count("o"))


# Check if the string "123abc" is alphanumeric.
textStr = "abcd123"
if textStr.isalnum():
    print("Given Text is  Alpha Numiric")