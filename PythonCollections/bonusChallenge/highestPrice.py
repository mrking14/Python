# Given a dictionary of products and their prices, find the product with the highest price.

prices = {"Banana":50, "Mango" :60, "Guava":30}
print(f"Print Prices of Fruits: {prices}")

maxPrice = max(prices, key=prices.get)
print(maxPrice)
print(prices[maxPrice])


