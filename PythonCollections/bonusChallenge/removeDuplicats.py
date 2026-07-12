# Write a program that takes a list of numbers and removes all duplicates using a set.
fruits = ["Apple", "Banana", "Mango", "Apple"]

print(f"Type of Collection: {type(fruits)}")

print(f"Printing Entered List: {fruits}")

# Removing Duplicats From List.
setFruits = set(fruits)
print(f"Type of Collection after coonvering to Set: {type(setFruits)}")
print(f"Print Set of Fruits After Removal of Duplicats: {setFruits}")