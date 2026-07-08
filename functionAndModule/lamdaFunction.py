# Write a lambda function that adds two numbers and test it.

add = lambda num1,num2:num1+num2
result = add(500,100)
print("Addition Of 2 Number is :",result)


# Create a list [1, 2, 3, 4, 5] and use their squares.map() with a lambda function to get.

ls = [1,2,3,4,5]
sqr = lambda num:num*num

print("Square of given List is: ",list(map(sqr,ls)))
