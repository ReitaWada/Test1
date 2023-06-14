import json
num = 0
max = 0
min = 99999

with open("catalog.json",'r')as file:
    data = json.load(file)
    for info in data:
        name = info["name"]
        price = info["price"]
        if name == "jacket":
            num += 1
            if price > max:
                max = price
            if price < min:
                min = price
print(num)
print(max)
print(min)
            