cordinats = (10,20)
print(f"Given Tuple: {cordinats}")
print(f"Type of Collection is: {type(cordinats)}")
'''cordinats[1]=50
print(f"Given Tuple: {cordinats}")
object does not support item assignment.'''

'''Convert the tuple to a list, change its first element to 50 , and convert it back
to a tuple.'''

cordList = list(cordinats)
print(f"Tuple converted into the List: {cordList}")

cordList[1] =50
print(f"list Data 20 changed to 50{cordList}")

cordtuple = tuple(cordList)
print(f"List converted into Tuple: {cordtuple}")


