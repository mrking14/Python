'''Write a function 
full_name(first, last) that takes first name and last name
as parameters and returns a single string in the format 
"First Last" '''

def full_name(first, last):
    return first +" " +last

firstName = input("Enter First Name: ")
lastName = input("Enter your Last Name : ")

print(full_name(firstName,lastName))

'''Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function'''

def calculate_area(length, width=10):
    return length*width

len = int(input("Enter Lenth of rectange: "))
wid = int(input("Enter width of Rectangle: "))

areaWithWidth = calculate_area(len,wid)
areaWithoutWidth = calculate_area(len)

print("Area Of Rectangle with given width is : ",areaWithWidth)
print("Area Of Rectangle withot width is: ", areaWithoutWidth)



