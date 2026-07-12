placeList = {"Masoom":"Pakri", "Altaf" : "Paru"}
placeList1 = {"Arif" : "Chamarua"}

print(f"Print First List : {placeList}")
print(f"Print Second List : {placeList1}")

placeList.update(placeList1)
print(f"Place List updated: {placeList}")