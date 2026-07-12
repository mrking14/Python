# Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to
# duplicate 3?).

mySet = {1,2,3,3,4}
print(f"Given Set is: {mySet}")

# Add 5 to the set,
mySet.add(5)
print(f"Set after 5 addedf into the Set: {mySet}")

#  remove 2 ,
mySet.remove(2)
print(f"Set After Removed 5from the Set: {mySet}")

# and check if 4 is in the set.
if mySet.__contains__(4):
    print("4 is Persent in the Set.")
else:
    print("4 is not Availabe in the Set.")


