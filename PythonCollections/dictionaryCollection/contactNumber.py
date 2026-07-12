# Create a dictionary of three friends and their phone numbers. Use:
contactNumbers= {"Altaf":"613456565","Arif" : "5676876762", "Ekramul" : "3856545"}
print(contactNumbers)

# Keys() to get all names
print(f"Printing Keys From Dictionary: {contactNumbers.keys()}")

# values() to get all numbers
print(f"Printing Values From ContactNumber Dictionary: {contactNumbers.values()}")

# items() to loop over key-value pairs and print them
for key,value in contactNumbers.items():
    print(f"key Of Contact NUmber is: {key} and Value is: {value}")
