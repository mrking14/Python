student = {"name" : "John","age":0,"grade":"A"}

# Print Value of Name
nameValue = student["name"]
print(f"Value of Name is: {nameValue}")

#Change Grade to A+
student["grade"] = "A+"
print(f"New Grade of Students : {student["grade"]}")


# Add a new key "city" with value "Delhi" .
student["city"] = "Delhi"
print(f"Value of City : {student["city"]}")

print(student)
