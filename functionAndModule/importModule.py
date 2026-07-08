import modulePrac
import requests

num = int(input("Enter First Number: "))
num1 = int(input("Enter Second Number: "))

result =  modulePrac.add(num,num1)

print("Addition of Given Numer is : ",result)

a = requests.get("https://api.github.com")

print(a.json())